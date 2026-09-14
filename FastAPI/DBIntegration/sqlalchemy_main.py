"""
this file shows the connection to db using sqlalchemy.
when we handle db using python, we use sqlalchemy

sqlalchemy is the ORM (object relational mapper)  built
on top of sqlite which we conncet with fastapi to perform 
our job
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from sqlalchemy import Column, Integer, String

from fastapi import FastAPI, status, Depends

DATABASE_URL = "sqlite:///./sqlalchemy_db.db"

engine = create_engine(
    url=DATABASE_URL,
    connect_args= {"check_same_thread": False}
    )

sessionLocal = sessionmaker(bind=engine)

base = declarative_base()


# now creating the model to create table

class TODO(base):

    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    completed = Column(String)


base.metadata.create_all(bind=engine)


def get_db():

    db = sessionLocal()

    try:
        yield db

    finally:
        db.close()


app = FastAPI()


@app.get('/fetch-db', status_code=200)
def creatae_db(db: Session = Depends(get_db)):

    return {
        "message": "db created and connected successfully"
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run('sqlalchemy_main:app', reload=True)