from cli.expense import Expense
from cli.expense_manager import ExpenseManager
from cli.storage import save_expense
from datetime import date
import sys

manager=ExpenseManager()

categories = [
    "Food",
    "Transport",
    "Shopping",
    "Bills",
    "Entertainment",
    "Other"
]

def main():
    while True: # unless we choose the right option
        options = [add_expense, list_expense, get_summary, modify_expense, exit_program]
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
    

def category_choice(current=None):
    while True:
        print("=======Categories=======")
        for i, category in enumerate(categories, start=1):
            print(f"{i}. {category}")
        if current:
            print("(Press Enter to keep current: " + current + ")")
 
        raw = input("Enter choice no: ")
        if current and raw.strip() == "":
            return current
 
        try:
            choice = int(raw) - 1
        except ValueError:
            print("Invalid")
            continue
 
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
        curr_date=date.today().isoformat()
        expense=Expense(amount,category,desc,curr_date) #in class object format
        manager.add_append(expense)
        print(f"{amount}||{category}||{desc}||{curr_date}")
        break # if condition all works, close the loop
    

def list_expense():
    expenses=manager.list()
    if not expenses:
        print("No expenses")
        return
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense}")

def get_summary():
    expenses=manager.summary()
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
    expenses:list[Expense] = manager.list() 
    if not expenses:
        print("No expenses")
        return
 
    options = ["Edit", "Remove", "Search", "Sort"]
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    try:
        select = int(input("Enter choice: ")) - 1
    except ValueError:
        print("Invalid choice")
        return
 
    if select == 0:
        _edit_expense(expenses)
    elif select == 1:
        _remove_expense(expenses)
    elif select == 2:
        _search_expense(expenses)
    elif select == 3:
        _sort_expense(expenses)
    else:
        print("Invalid choice")

def _edit_expense(expenses):
    for i, expense in enumerate(expenses,start=1):
        print(f"{i}. {expense}")
    try:
        choice=int(input("Enter expense to change: "))-1
    except ValueError:
        print("Invalid choice")
        return
    if not (0<=choice<=len(expenses)):
        print("Invalid choice")
        return
    expense=expenses[choice]
    print("Press Enter to keep the current value")
    amount=input("Enter amount: ")
    if amount.strip():
        try:
            expense.amount=float(amount)
            print(f"Changed amount: {amount}")
        except ValueError:
            print("Invalid value, keeping old value")

    category=category_choice(current=expense.category)
    if category!=expense.category:
        expense.category=category
        print(f"Changed category: {category}")

    desc=input("Enter description: ")
    if desc.strip():
        expense.desc=desc
        print(f"Changed description: {desc}")

    date=input("Enter date: ")
    if date.strip():
        expense.date=date
        print(f"Changed date: {date}")

def _remove_expense(expenses):
    for i, expense in enumerate(expenses,start=1):
            print(f"{i}. {expense}")
    try:
        choice=int(input("Enter expense to change: "))-1
    except ValueError:
        print("Invalid choice")
        return
    if (0<=choice<len(expenses)):
        expenses.pop(choice)
        save_expense(expenses)
        print("Removed")
    else:
        print("Invalid choice")
        
def _search_expense(expenses):
    search=input("Search by description: ").lower()
    flag=False
    for expense in expenses:
        if search in expense.desc.lower():
            flag= True
            print(expense)
    if not flag:
        print("Not found")

def _sort_expense(expenses):
    print("1. Amount\n2. Date")
    try:
        choice=int(input("Choice: "))
    except ValueError:
        print("Invalid Value")
        return
    if choice==1:
        expenses.sort(key=lambda x:x.amount)
    elif choice==2:
        expenses.sort(key=lambda x:x.date)
    else:
        print("Invalid choice")
        return 
    save_expense(expenses)

def exit_program():
    sys.exit()

if __name__=="__main__":
    main()