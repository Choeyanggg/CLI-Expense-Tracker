from sqlalchemy import create_engine
from setting import settings
from sqlalchemy.orm import sessionmaker,declarative_base

engine=create_engine(settings.DB_CONNECTION)

session=sessionmaker(bind=engine)

Base=declarative_base() #blueprint to create table

def get_db():
    db=session() #create session
    try:
        yield db #provide it to the fastapi route
    finally:
        db.close() #close it after use



