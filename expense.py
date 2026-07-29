from storage import save_expense,load_expense

class Expense:
    def __init__(self,amount:int,category:str,desc: str,date:str):
        self.amount=amount
        self.category=category
        self.desc=desc
        self.date=date

    def __str__(self):
        return(
            f"${self.amount:.2f} | "
            f"{self.category} | "
            f"{self.desc} | "
            f"{self.date}"
        )

    def to_dict(self)->dict: # fun use to convert object to dict
        return{
            "amount":self.amount,
            "category":self.category,
            "description":self.desc,
            "date":self.date
        }

    @classmethod # class is use as no object exist, dict to object
    def from_dict(cls,data:dict)->"Expense": #fun use to convert dict to object
        return cls(
            amount=data["amount"],
            category=data["category"],
            desc=data["desc"],
            date=data["date"],
        )

class ExpenseManager:
    def __init__(self):
        self.expenses=load_expense()

    def add_append(self,expense):
        self.expenses.append(expense)