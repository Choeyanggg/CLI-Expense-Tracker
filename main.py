from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from models import Expense
from schemas import ExpenseIn,ExpenseOut,ExpenseUpdate
from database import Base,engine,get_db


Base.metadata.create_all(bind=engine)

app=FastAPI()

@app.post("/expenses",response_model=ExpenseOut)
def add_expenses(expense:ExpenseIn,db:Session=Depends(get_db)): #pydantic object for validation
    db_expense=Expense(**expense.model_dump()) #converts pydantic into dic, unpack(**) the dic to create alchemy object 
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

@app.get("/expenses/{expense_id}",response_model=ExpenseOut)
def search_expense(expense_id:int,db:Session=Depends(get_db)):
    expense=db.get(Expense,expense_id)
    if not expense:
        raise HTTPException(status_code=404, detail="Item not found")
    return expense

@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id:int, db:Session=Depends(get_db)):
    expense=db.get(Expense,expense_id)
    if not expense:
        raise HTTPException(status_code=404,detail="Item not found")
    db.delete(expense)
    db.commit()
    return {"message": "Expense deleted"}

@app.get("/expenses", response_model=list[ExpenseOut])
def sort_expenses(sort_by:str|None=None, db:Session=Depends(get_db)):
    query=select(Expense)
    if sort_by=="amount":
        query=query.order_by(Expense.amount)
    elif sort_by=="year":
        query=query.order_by(Expense.date)
    expenses=db.execute(query).scalars().all()
    return expenses
