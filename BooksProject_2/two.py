'''
this file will give Field addition from 
pydantic which will add extra validation
'''

from pydantic import BaseModel, Field
from fastapi import FastAPI
from typing import Optional
from uuid import UUID


app = FastAPI()


class Book(BaseModel):
    id: UUID
    title: str = Field(title='title of the book',
                       min_length=4,
                       max_length=10)

    # field will make sure that min length of the author MUST be 4
    author: str = Field(min_length=4, max_length=10)
    description: str


BOOKS = []


@app.get('/')
async def getAllBooks():
    return BOOKS


@app.post('/book',)
async def book(book: Book):
    BOOKS.append(book)
    return book

