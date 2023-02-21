from fastapi import FastAPI
from typing import Optional
from enum import Enum
import uvicorn

app = FastAPI()

BOOKS = {
    'book1': {'title': 'title1', 'author': 'author1'},
    'book2': {'title': 'title2', 'author': 'author2'},
    'book3': {'title': 'title3', 'author': 'author3'},
    'book4': {'title': 'title4', 'author': 'author4'},
    'book5': {'title': 'title5', 'author': 'author5'},
}


@app.get('/')
async def welcome():
    return {'message': 'welcome to Books Project'}


@app.get('/books')
async def books():
    return BOOKS


# path parater
@app.get('/param/{bookTitle}')
async def pathParam(bookTitle: str):
    return {'bookTitle': bookTitle}


# path paramter as integer
@app.get('/intParam/{bookTitle}')
async def intParam(id: int, bookTitle: str):
    return {'bookTitle': bookTitle, 'id': id}


# api to take query parameter and return its respective book
# enhancing books api with path parameter
@app.get('/bookName')
async def bookName(book_name: str = None):
    try:
        return BOOKS[book_name]
    except:  # Exception as e:
        return {'Book not in the dictionary'}
