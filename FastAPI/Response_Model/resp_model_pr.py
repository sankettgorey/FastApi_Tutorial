from fastapi import FastAPI
import uvicorn

from pydantic import BaseModel


app = FastAPI()

users = []

class User(BaseModel):

    name: str
    age: int
    email: str
    password: str


class UserResponse(BaseModel):

    name: str
    age: int
    email: str


class UserResponseList(BaseModel):

    users: list[UserResponse]


class UserResponseOutput(BaseModel):
    user: UserResponse
    message: str


@app.get('/users-list', response_model=UserResponseList)
def get_users():

    return {
        "users": users
    }


@app.post('/create-user', response_model=UserResponseOutput)
def create_user(user: User):

    users.append(user)

    return {
        "message": "user created",
        "user": user
    }
    


if __name__ == "__main__":
    uvicorn.run('resp_model_pr:app')