from fastapi import FastAPI, Depends, Request, HTTPException, status, Header
from fastapi.responses import JSONResponse

import uvicorn

from data_models import User, UserCreated, UserResponseList


# creating custom exception handling classes

class AppError(Exception):

    status_code = 400
    error_code = "not able to process"
    message = "something went wrong"

    def __init__(self, message):
        if message:
            self.message = message


class NotFoundError(AppError):

    status_code = 404
    error_code = "NOT FOUND ERROR"
    message = "Resource not found"


class ConflictError(AppError):

    status_code=409
    error_code="DUPLICATE ENTRY"
    message="Resousce already exists"


class ValidationError(AppError):

    status_code=422
    error_code="Invalid Input"
    message="Given input is invalid"

class AuthenticationError(AppError):

    status_code = 401
    error_code = "UNAUTHORIZED"
    message = "Authentication failed"




def authenticate(token = Header(...)):

    if token == "myaccesstoken":
        return {
            "message": "valid user"
        }

    raise AuthenticationError("Invalid token")

users = []

app = FastAPI()

# creating custom exception handler
@app.exception_handler(AppError)
def handle_exception(request: Request, exc: AppError):

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "message": exc.message,
            "error_code": exc.error_code
        }
    )


@app.get("/all-users", status_code=status.HTTP_200_OK, response_model=UserResponseList)
def get_users(token = Depends(authenticate)):

    return {
        "message": "List of all users",
        "users": users
    }


@app.post("/crete-user", status_code=status.HTTP_201_CREATED, response_model=UserCreated)
def create_user(user: User, token = Depends(authenticate)):

    for existing_user in users:
        if existing_user.name == user.name:
            raise ConflictError("User with this name already exists")

    users.append(user)

    return user


@app.get("/get-user-by-name/{name}", status_code=201)
def get_user(name: str, token = Depends(authenticate)):

    for user in users:
        if user.name == name:
            return {
                "message": "User found",
                "user": user
            }

    raise NotFoundError(f"User with name {name} not found in the database")







if __name__ == "__main__":
    uvicorn.run("dependency_injection:app", reload=True)
