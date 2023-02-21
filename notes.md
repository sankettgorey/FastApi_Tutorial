- To see the swaggerUI for fastapi: localhost:8000/docs
- To see the openapi stndards: localhost:8000/openapi.json

- Types of methods in API:
    - get: method that retrives the data
    - post: method that creates the data or whic submits the data
    - put: method that updates the data 
    - patch: method that updates part of the data
    - delete: method that deletes the data
These operations are also called CRUD operations.

- Types of status codes:
    - 1xx: request processing
    - 2xx: request successfully completed
    - 3xx: redirection: further action must be completed.
    - 4xx: client side error in request
    - 5xx: server side error

PROJECT_1: BOOKS PROJECT
- Path Parameters: This is a way to add additional variable to the API call. This is used to get custom information upon request.
sytax: 
    @app.get('/books/{pathParameter'})
    async def func1(pathParameter):
        return your response

WHEN YOU HAVE API WITH PATH PARAMETERS, MAKE SURE TO ADD THIS IN THE END OTHERWISE IT WILL CREATE ERROR.

enumeration with path paramters:
    This is used when we want user to enter only specific set of values from drop down menu. Follow enumPathParam.py file from BooksProject folder for demo.

TO USE BOTH QUERY AND PATH PARAMETERS IN A SINGLE API, FIRST GIVE QUERY PARAM AND THEN GIVE PATH PARAM.

to gethe list of dropdown menu in the frontend/swagger UI, use Enum while defining the class.


QUERY PARAMETER
we can give query parameter in the API in the following way:

@app.get('/apiName')
async def func(queryParam):
    return response

Query param help us to get the certain output upon request.
we can enhance the query param in the following way:

@app.get('/')
async def welcome(name: str = None):
    if name:
        return {f'Hello {name}'}
    return {'Hello default'}

here, name is query param which is set to str dtype and its set to None. When its set None, it becomes optional


### POST REQUEST
- This method is used to create new data.
Syntax:

lst = []
@app.post('/')
async def createData(queryParam):
    lst.append(queryParam)
    return lst

## PUT REQUEST
- This method updates the already existing data

@app.put('/updateBook/{bookName}')
async def updateBook(bookName: str, bookTitle: str, bookAuthor: str):
    bookDetails = {'title': bookTitle, 'author': bookAuthor}

    # updating the books dictionary
    BOOKS[bookName] = bookDetails

    return bookDetails

