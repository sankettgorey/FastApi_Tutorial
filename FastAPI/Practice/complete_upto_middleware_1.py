from fastapi import FastAPI, status, Depends, Header, Request, HTTPException
from fastapi.responses import JSONResponse

import uvicorn

import time
from pydantic import BaseModel

# defining eception class
class AppError(Exception):

    status_code = 422
    error_code = 'NOT ABLE TO PROCESS'

    def __init__(self, message):
        self.message = message
        super().__init__(message)


class NotFOundError(AppError):

    status_code=404
    error_code='RESOURCE NOT FOUND'


class DUplicateError(AppError):

    status_code=409
    error_code='RESOURCE EXISTS'


class ValidationError(AppError):

    status_code=401
    error_code='NOT ABLE TO PROCESS'


# defining response models
class User(BaseModel):

    id: int
    name: int
    age: int
    email: str
    password: str


class UserCreated(BaseModel):

    id: int
    name: str
    age: int
    email: str


class UserList(BaseModel):

    message: str
    users: list[UserCreated]




users = []

app = FastAPI()

@app.exception_handler(AppError)
def exception(request: Request, exc: AppError):

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error_code": exc.error_code,
            "message": exc.message
        }
    )


# ceating dependency injection
def authentication(token = Header(...)):

    if token != 'myaccesstoken':
        raise ValidationError("Not able to authenticate")

    return {
        "message": "auth successful"
    }


# defining middleware
@app.middleware("http")
async def middleware(request: Request, create_next):

    print(f'request entered into {request.url}')

    response = await create_next(request)

    print(f'request processing completed')

    return response



@app.get("/get-users", status_code=status.HTTP_200_OK, response_model=UserList)
def get_users():

    return {
        "message": "list of users",
        "users": users
    }


if __name__ == "__main__":
    uvicorn.run('complete_upto_middleware_1:app')