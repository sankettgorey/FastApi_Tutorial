from pydantic import BaseModel
from fastapi import FastAPI
from uuid import UUID
import uvicorn

app = FastAPI()

# creating class for data validation using pydantic BaseModel


class Book(BaseModel):
    id: UUID
    title: str
    author: str
    description: str
    rating: int


BOOKS = []


# api to return empty books list
@app.get('/')
async def returnAllBooks():
    return BOOKS


# post api to append all class variables
@app.post('/')
async def createBook(book: Book):
    BOOKS.append(book)
    return book

# post api to append all class variables
@app.post('/book')
async def createBook(book: Book):
    BOOKS.append(book)
    return book