from enum import Enum
from pydantic import BaseModel,Field,ConfigDict
import datetime 

class Category(str,Enum):
    food = "Food"
    transport = "Transport"
    shopping = "Shopping"
    bills = "Bills"
    entertainment = "Entertainment"
    other = "Other"

class ExpenseIn(BaseModel):
    amount:float=Field(gt=0)
    category:Category
    desc:str
    date:datetime.date

class ExpenseUpdate(BaseModel):
    amount:float | None=None
    category:str | None=None
    desc:str | None=None
    date: datetime.date | None=None # type: ignore

class ExpenseOut(ExpenseIn):
    id:int
    model_config=ConfigDict(from_attributes=True) #SQLalchmey to pydantic