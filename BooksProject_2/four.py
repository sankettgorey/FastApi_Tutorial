'''
this program will create a predefined values in the swagger UI
if we don't enter any values while creating a post request.
this is done by creating class inside the BaseModel class using pydantic
'''

from uuid import UUID
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()


class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1)
    rating: int = Field(gt=-1, lt=11)

    class Config:
        schemaExtra = {
            "example": {
                "id": '90c06c9c-770a-4f7b-9450-efca205503d6',
                "title": 'title1',
                "author": 'author1',
                "description": 'descr1',
                "rating": 10
            }
        }


BOOKS = []


@app.get('/')
async def getBooks():
    return BOOKS


@app.post('/')
async def createBook(book: Book):
    BOOKS.append(book)
    return book
