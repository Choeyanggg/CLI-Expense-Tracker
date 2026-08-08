from sqlalchemy import create_engine
from setting import settings
from sqlalchemy.orm import sessionmaker,declarative_base,Mapped,mapped_column

engine=create_engine(settings.DB_CONNECTION)

session=sessionmaker(bind=engine)

Base=declarative_base() #blueprint to create table

def get_db():
    db=session()
    try:
        yield db
    finally:
        db.close()



