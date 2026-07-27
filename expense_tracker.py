from expense import Expense
from storage import save_expense,load_expense
import sys

expenses:Expense=load_expense() # load the object from json file (wont get lost after system down)

def main():
    while True: # unless we choose the right option
        options=[add_expense,list_expense,get_summary,Exit]
        for i,fun in enumerate(options):
            print(f"{i+1} {fun.__name__}")
        try: # exception handelling
            choice=int(input("Enter option: "))-1
            if choice in range (len(options)):
                options[choice]()
            else:  
                print("Invalid Option, try again")
        except ValueError:
            print("Invalid Option, try again")
    
categories=["Food",
        "Transport",
        "Shopping",
        "Bills",
        "Entertainment",
        "Other"
    ]
def category_choice():
    while True:
        for i,category in enumerate(categories,start=1):
                    print(f"{i}. {category}")
        
        choice=int(input("Enter choice no: "))-1
        if choice not in range(len(categories)):
            print("Invalid")
            continue
        return categories[choice]

def add_expense(): #add manual expenses
    while True:
        try:
            amount=float(input("Enter amount: "))
        except ValueError:
            print("Invalid")
            continue
        category=category_choice()
        desc=input("Enter the description: ")
        date=input("Date (YYYY-MM-DD): ")
        expense=Expense(amount,category,desc,date) #in class object format
        expenses.append(expense) #add to load fun
        save_expense(expenses) #to save permanent , convert object to dict to save in json
        print(amount,category,desc,date)
        break # if condition all works, close the loop
    

def list_expense():
    if not expenses:
        print("No expenses")
        return
    for i, expense in enumerate(expenses,start=1):
        print(f"{i}. {expense}")


def get_summary():
    if not expenses:
        print("No expenses")
        return
    print("===== Summary =====")
    print(f"No of expense: {len(expenses)}")
    amount=sum(expense.amount for expense in expenses)
    print(f"Total amount {amount}")
    print(f"Avg expense: {amount/len(expenses):.2f}")
    expense_cat={}
    print("By Category")
    for expense in expenses: 
        if expense.category in expense_cat:
            expense_cat[expense.category]+=expense.amount
        else:
            expense_cat[expense.category]=expense.amount
    for category,total in expense_cat.items():
        print(f"{category}: ${total}")

def modify_expense():
    options=[
        "Edit",
        "Remove",
        "Search",
        "Sort"
    ]
    for i,option in enumerate(options,start=1):
        print(f"{i}. {option}")
    select=int(input("Enter choice: "))-1
    if(choice==0):
        for i, expense in enumerate(expenses,start=1):
            print(f"{i}. {expense}")
        choice=int(input("Enter choice no: "))-1
        if choice in range (len(expenses))-1:
            expense=expenses[choice]
            print("Press Enter to keep the current value")
            price=int(input("Enter price: "))
            if price:
                expense.price=price
                print(f"Changed price: {price}")
            category=category_choice()
            if category:
                expense.category=category

            


    elif(select==1):
        for i, expense in enumerate(expenses,start=1):
            print(f"{i}. {expense}")
        choice=int(input("Enter choice no: "))-1
        if choice in range (len(expenses))-1:
                expense.pop(choice)
        save_expense(expenses)
    

def Exit():
    sys.exit()

if __name__=="__main__":
    main()