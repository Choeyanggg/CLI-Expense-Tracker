class Expense:
    def __init__(self,category:str,desc: str,price:int,date:str):
        self.price=price
        self.category=category
        self.desc=desc
        self.date=date

    def __str__(self):
        return(
            f"${self.price:.2f} | "
            f"{self.category} | "
            f"{self.desc} | "
            f"{self.date}"
        )