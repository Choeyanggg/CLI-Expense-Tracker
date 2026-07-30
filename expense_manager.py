from storage import save_expense,load_expense

class ExpenseManager:
    def __init__(self):
        self.expenses=load_expense()

    def add_append(self,expense):
        self.expenses.append(expense)
        save_expense(self.expenses)

    def list(self):
        return self.expenses

    def delete(self,index):
        self.expenses.pop(index)
        save_expense(self.expenses)

    def summary(self):
        return self.expenses