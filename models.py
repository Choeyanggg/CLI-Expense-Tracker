from sqlalchemy import ForeignKey
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
    user_id:Mapped[int]=mapped_column(ForeignKey("users.id"))

class Users(Base):
    __tablename__="user"

    id:Mapped[int]=mapped_column(primary_key=True)
    username:Mapped[str]=mapped_column(unique=True)
    password_hash:Mapped[str]
    role:Mapped[str]=mapped_column(default="user")