from fastapi import FastAPI
import uvicorn

from pydantic import BaseModel
from typing import List


class User(BaseModel):

    id: int
    name: str
    email: str
    age: int
    password: str


class UserResponse(BaseModel):

    id: int
    name: str
    email: str
    age: int


class UserResponseList(BaseModel):

    users: list[UserResponse]

users = []

app = FastAPI()


@app.post('/create-user', response_model=UserResponse)
def create_user(user: User):

    users.append(user)

    return user

@app.get('/get-users', response_model=UserResponseList)
def get_users():

    return {
        'message': 'data of all users',
        "users": users
    }

@app.get('/get-single-user/{user_id}', response_model=UserResponse)
def get_single_user(user_id: int):

    if user_id < len(users):
        return users[user_id]

    return {'error': 'user not found'}


if __name__ == "__main__":
    uvicorn.run('create_resp_model:app', reload=True)