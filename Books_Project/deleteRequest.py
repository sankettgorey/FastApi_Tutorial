from fastapi import FastAPI


BOOKS = {
    'book1': {'title': 'title1', 'author': 'author1'},
    'book2': {'title': 'title2', 'author': 'author2'},
    'book3': {'title': 'title3', 'author': 'author3'},
    'book4': {'title': 'title4', 'author': 'author4'},
    'book5': {'title': 'title5', 'author': 'author5'},
}


app = FastAPI()


@app.get('/')
async def books():
    return BOOKS


# deleting the book on request using query param
@app.delete('/deleteBook')
async def deleteBook(bookName: str):
    try:
        del BOOKS[bookName]

        return f'{bookName} is deleted'

    except Exception as e:
        return e


# deleting book using path param
@app.delete('/delete/{bookName}')
async def delete(bookName: str):
    try:
        del BOOKS[bookName]
        return f'{bookName} is deleted'
    except Exception as e:
        return e
