import json
from expense import Expense
FILE_NAME="expenses.json"

def save_expense(expenses: list):
    data=[expense.to_dict() for expense in expenses] #convert each expense object to dict
    with open(FILE_NAME,'w',encoding="utf-8") as file: #open the json file as file
        json.dump(data,file,indent=4)

def load_expense():
    try:
        with open(FILE_NAME,'r',encoding="utf-8") as file:
            data=json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError: 
        print(f"Warning: {FILE_NAME} is corrupted or empty. Starting with no expenses.")
        return []
    return [Expense.from_dict(item) for item in data] 