from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from models import Expense,Users
from schemas import ExpenseIn,ExpenseOut,ExpenseUpdate
from database import Base,engine,get_db
from routes import auth,user
from auth import get_current_user

Base.metadata.create_all(bind=engine)

app=FastAPI()

app.include_router(auth.router)
app.include_router(user.router)


@app.post("/expenses",response_model=ExpenseOut)
def add_expenses(expense:ExpenseIn,db:Session=Depends(get_db),user:Users=Depends(get_current_user)): #pydantic object for validation
    db_expense=Expense(**expense.model_dump(),user_id=user.id) #converts pydantic into dic, unpack(**) the dic to create alchemy object 
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

@app.get("/expenses", response_model=list[ExpenseOut])
def sort_expenses(sort_by:str|None=None, db:Session=Depends(get_db),user:Users=Depends(get_current_user)):
    query=db.query(Expense).filter(Expense.user_id==user.id)
    if sort_by=="amount":
        query=query.order_by(Expense.amount)
    elif sort_by=="year":
        query=query.order_by(Expense.date)
    expenses=query.all()
    return expenses

@app.get("/expenses/summary")
def expenses_summary(db:Session=Depends(get_db),user:Users=Depends(get_current_user)):
    expenses=db.query(Expense).filter(Expense.user_id==user.id).all()
    if not expenses:
        return{
            "count":0,
            "total":0,
            "average":0,
            "by_category":{}
        }
    
    total=sum(expense.amount for expense in expenses)
    by_category={}
    for expense in expenses:
        if expense.category in by_category:
            by_category[expense.category]+=expense.amount
        else:
            by_category[expense.category]=expense.amount

    return{
        "count": len(expenses),
        "total": total,
        "average": total/len(expenses),
        "by_category":by_category        
    }

@app.get("/expenses/{expense_id}")
def search_expense(expense_id:int,db:Session=Depends(get_db),user:Users=Depends(get_current_user)):
    expense=db.query(Expense).filter(expense_id==Expense.id,Expense.user_id==user.id).first()
    if not expense:
        raise HTTPException(status_code=404, detail="Item not found")
    return expense

@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id:int, db:Session=Depends(get_db),user:Users=Depends(get_current_user)):
    expense=db.query(Expense).filter(Expense.id==expense_id,Expense.user_id==user.id).first()
    if not expense:
        raise HTTPException(status_code=404,detail="Item not found")
    db.delete(expense)
    db.commit()
    return {"message": "Expense deleted"}

@app.patch("/expenses/{expense_id}",response_model=ExpenseOut)
def modify_expense(expense_id:int,expense:ExpenseUpdate,db:Session=Depends(get_db),user:Users=Depends(get_current_user)):
    db_expense=db.query(Expense).filter(Expense.id==expense_id,Expense.user_id==user.id).first()
    if not db_expense:
        raise HTTPException(status_code=404, detail="Item not found")
    update_data=expense.model_dump(exclude_unset=True)
    for key,value in update_data.items():
        setattr(db_expense,key,value)
    db.commit()
    db.refresh(db_expense)
    return db_expense