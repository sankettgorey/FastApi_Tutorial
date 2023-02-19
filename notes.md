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