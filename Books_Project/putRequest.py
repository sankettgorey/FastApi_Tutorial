from fastapi import FastAPI

app = FastAPI()

BOOKS = {
    'book1': {'title': 'title1', 'author': 'author1'},
    'book2': {'title': 'title2', 'author': 'author2'},
    'book3': {'title': 'title3', 'author': 'author3'},
    'book4': {'title': 'title4', 'author': 'author4'},
    'book5': {'title': 'title5', 'author': 'author5'},
}


@app.get('/')
async def books():
    return BOOKS


@app.put('/updateBook/{bookName}')
async def updateBook(bookName: str, bookTitle: str, bookAuthor: str):
    bookDetails = {'title': bookTitle, 'author': bookAuthor}

    # updating the books dictionary
    BOOKS[bookName] = bookDetails

    return bookDetails
