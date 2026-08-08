from fastapi import FastAPI,Depends
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
