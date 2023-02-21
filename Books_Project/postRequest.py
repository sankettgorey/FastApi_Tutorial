from fastapi import FastAPI

app = FastAPI()

BOOKS = {
    'book1': {'title': 'title1', 'author': 'author1'},
    'book2': {'title': 'title2', 'author': 'author2'},
    'book3': {'title': 'title3', 'author': 'author3'},
    'book4': {'title': 'title4', 'author': 'author4'},
    'book5': {'title': 'title5', 'author': 'author5'},
}

# getting all books using get method


@app.get('/books')
async def welcome():
    return BOOKS

# post method to create a new book


@app.post('/createBook')
async def createBook(title: str, author: str):
    bookId = 0
    if len(BOOKS) > 0:
        for book in BOOKS:
            x = int(book[-1])

            bookId = x
    bookId = bookId + 1

    BOOKS[f'book{bookId}'] = {'title': title, 'author': author}

    return BOOKS[f'book{bookId}']


