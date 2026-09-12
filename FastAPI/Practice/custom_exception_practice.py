from fastapi import FastAPI, status, HTTPException, Request
from fastapi.responses import JSONResponse

from pydantic import BaseModel


class User(BaseModel):

    id: int
    name: str
    age: int
    email: str
    password: str


class UserResponse(BaseModel):

    id: int
    name: str
    age: int
    email: str



class UserResponseList(BaseModel):

    message: str
    users: list[UserResponse]


users = []

class AppError(Exception):

    status_code = 400
    error_code = "APP ERROR"
    message = "Something went wrong"

    def __init__(self, message = None):
        if message:
            self.message = message


class NotFoundError(AppError):

    status_code=404
    error_code="not found"
    message="Resource not found"


class ConflictError(AppError):

    status_code=409
    error_code="conflict"
    message='Resource already exists'


class ValidationError(AppError):
    status_code=422
    error_code="validation error"
    message="invalid input"


users = []

app = FastAPI()

@app.exception_handler(AppError)
def custom_exception(request: Request, exc: AppError):

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error_code": exc.error_code,
            "message": exc.message
        }
    )


# get all users list
@app.get("/get-users", status_code=status.HTTP_200_OK, response_model=UserResponseList)
def get_users():

    return {
        "message": "List of all users",
        "users": users
    }


# create new user
@app.post("/create-user", status_code=201, response_model=UserResponse)
def create_user(user: User):

    for each_user in users:
        if each_user.name == user.name:
            raise ConflictError("User already exists")

    users.append(user)

    return user



# get user by name
@app.get("/get-user/{name}", status_code=200, response_model=UserResponseList)
def get_user(name: str):

    for user in users:
        if user.name == name:
            return {
                "message": "User found",
                "users": [user]
            }

    raise NotFoundError(f"User named {name} not found in the db")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run('custom_exception_practice:app', reload=True)