from sqlalchemy import create_engine
from setting import settings
from sqlalchemy.orm import sessionmaker,declarative_base,Mapped,mapped_column
from datetime import date
# from dotenv import load_dotenv
# import os
#load_dotenv()

engine=create_engine(settings.PG_CONNECTION)

session=sessionmaker(bind=engine)

class Base(declarative_base): #blueprint to create table
    pass

class Expense(Base):
    __tablename__="expenses"

    id:Mapped[int]=mapped_column(primary_key=True)
    amount:Mapped[float]
    category:Mapped[str]
    desc:Mapped[str]
    date:Mapped[date]















#JSON STORAGE
# import json
# from expense import Expense
# FILE_NAME="expenses.json"

# def save_expense(expenses: list):
#     data=[expense.to_dict() for expense in expenses] #convert each expense object to dict
#     with open(FILE_NAME,'w',encoding="utf-8") as file: #open the json file as file
#         json.dump(data,file,indent=4)

# def load_expense():
#     try:
#         with open(FILE_NAME,'r',encoding="utf-8") as file:
#             data=json.load(file)
#     except FileNotFoundError:
#         return []
#     except json.JSONDecodeError: 
#         print(f"Warning: {FILE_NAME} is corrupted or empty. Starting with no expenses.")
#         return []
#     return [Expense.from_dict(item) for item in data] 