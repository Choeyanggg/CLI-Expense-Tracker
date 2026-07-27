import json
from expense import Expense
FILE_NAME="expenses.json"

def save_expense(expenses: list):
    data=[expense.to_dict() for expense in expenses] #convert each expense object to dict
    with open(FILE_NAME,'w') as file: #open the json file as file
        json.dump(data,file,indent=4)

def load_expense():
    with open(FILE_NAME,'r') as file:
        data=json.load(file)
    return [Expense.from_dict(item) for item in data] 