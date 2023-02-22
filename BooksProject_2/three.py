'''
here custom function is created to append books into the BOOKS list and its called using get method API.
So, when the API is called, it will automatically append books into the books list and new books will
be created and appended in the books list
'''


from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID


BOOKS = []

app = FastAPI()


class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: str = Field(title='additional info of the book',
                             min_length=1,
                             max_length=100)
    rating: int = Field(gt=-1,
                        lt=11)

    


@app.get('/')
async def books():
    if len(BOOKS) < 1:
        createBook()
    return BOOKS


@app.post('/createBook')
async def createBook(book: Book):
    BOOKS.append(book)

    return book


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
