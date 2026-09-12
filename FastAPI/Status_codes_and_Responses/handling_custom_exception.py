from fastapi import FastAPI, status, HTTPException, Request
from fastapi.responses import JSONResponse
import uvicorn

from pydantic import BaseModel


class User(BaseModel):

    id: int
    name: str
    age: int
    email: str
    password: str

users = []

app = FastAPI()


class UserAlreadyExistsException(Exception):
    pass



@app.exception_handler(UserAlreadyExistsException)
def user_already_exists(request: Request, exec: UserAlreadyExistsException):

    return JSONResponse(
        status_code=409,
        content={
            "message": "User alreadye exists"
        }
    )

@app.post("/create-user", status_code=status.HTTP_201_CREATED)
def create_user(user: User):

    for existing_user in users:
        if existing_user.name == user.name:
            raise UserAlreadyExistsException()

    users.append(user)

    return user


if __name__ == "__main__":
    uvicorn.run('handling_custom_exception:app')