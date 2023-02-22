'''
this program will take query param from user and return only that many no of books
here query param is optional and if its not entered, it will return 
all the books
'''


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

    if booksToReturn:
        return BOOKS[: booksToReturn]

    return BOOKS


'''
this API will get us the book when we enter UUID
this UUID can be replaced by any other parameters
'''


@app.get('/getBook/{bookId}')
async def getBook(bookId: UUID):
    for book in BOOKS:
        if book.id == bookId:
            return book


@app.get('/getBookbyAuthor/{author}')
async def getBook(author: str):
    for book in BOOKS:
        # if book['author'] == author:
        if book.author == author:
            return book
