from fastapi import FastAPI, status, Request, Depends, Header
from fastapi.responses import JSONResponse

import uvicorn

from pydantic import BaseModel


class User(BaseModel):

    id: int
    name: str
    age: int
    email: str
    password: str


class UserCreated(BaseModel):

    name: str
    age: int
    email: str


class UserResponseList(BaseModel):

    message: str
    users: list[UserCreated]


class AppError(Exception):

    status_code = 401
    error_code = "NOT ABLE TO PROCESS"

    def __init__(self, message = "something went wrong"):

        self.message = message
        super().__init__(message)


class NotFoundError(AppError):

    status_code=404
    error_code="NOT FOUND"



class ConflictError(AppError):

    status_code=409
    error_code="RESOURCE EXISTS"


class ValidationError(AppError):

    status_code=422
    error_code='NOT ABLE TO PROCESS'



def authenticate(token = Header(...)):

    if token == "myaccesstoken":

        return {
            "message": "authentication successful",
            "status": "success"
        }

    raise ValidationError("Not able to Authenticate")


users = []

app=FastAPI()

# creating custom error hander
@app.exception_handler(AppError)
def error(request: Request, exc: AppError):

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "message": exc.message,
            "error_code": exc.error_code
        }
    )


@app.get('/get-users', status_code=200, response_model=UserResponseList)
def get_users(token = Depends(authenticate)):

    return {
        "message": "List of all users",
        "users": users
    }


@app.get("/get-user/{name}", status_code=status.HTTP_200_OK, response_model=UserResponseList)
def get_user(name: str, token = Depends(authenticate)):

    for user in users:
        if user.name == name:
            return {
                "message": "user found",
                "users": [user]
            }

    raise NotFoundError(f"User with name {name} not found in the database")



@app.post("/create-user", response_model=UserCreated, status_code=201)
def create_user(user: User, token = Depends(authenticate)):

    for each_user in users:
        if each_user.name == user.name:
            raise ConflictError(f"User with name {user.name} already exists in the database")

    users.append(user)

    return user



if __name__ == "__main__":
    uvicorn.run('practice:app', reload=True)