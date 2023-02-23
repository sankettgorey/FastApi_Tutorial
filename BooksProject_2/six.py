from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel, Field
from uuid import UUID


app = FastAPI()


class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1)
    rating: int = Field(gt=-1, lt=11)


BOOKS = []


def createBook():
    book1 = Book(id='40c06c9c-770a-4f7b-9450-efca205503d6',
                 title='title1',
                 author='author1',
                 description='description1',
                 rating=10)

    book2 = Book(id='50c06c9c-770a-4f7b-9450-efca205503d6',
                 title='title2',
                 author='author2',
                 description='description2',
                 rating=1)

    book3 = Book(id='60c06c9c-770a-4f7b-9450-efca205503d6',
                 title='title3',
                 author='author3',
                 description='description3',
                 rating=5)

    book4 = Book(id='70c06c9c-770a-4f7b-9450-efca205503d6',
                 title='title4',
                 author='author4',
                 description='description4',
                 rating=7)

    BOOKS.append(book1)
    BOOKS.append(book2)
    BOOKS.append(book3)
    BOOKS.append(book4)


@app.get('/')
async def getAllBooks(booksToReturn: Optional[int] = None):
    if len(BOOKS) < 1:
        createBook()
    return BOOKS


@app.get('/return')
async def getBooks():
    return BOOKS


@app.put('/update/{bookId}')
async def update(bookId: UUID, book: Book):
    counter = 0
    for b in BOOKS:
        # counter += 1
        if b.id == bookId:
            BOOKS[counter] = book
            counter += 1
        return BOOKS[counter - 1]
