from sqlalchemy.orm import Mapped,mapped_column
from database import Base
from datetime import date

class Expense(Base):
    __tablename__="expenses"

    id:Mapped[int]=mapped_column(primary_key=True)
    amount:Mapped[float]
    category:Mapped[str]
    desc:Mapped[str]
    date:Mapped[date]