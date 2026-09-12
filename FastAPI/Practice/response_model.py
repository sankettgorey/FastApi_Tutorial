from fastapi import FastAPI
import uvicorn

from pydantic import BaseModel, Field
from typing import Annotated, List, Optional


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

    users: List[UserResponse]


users = []

app = FastAPI(title="User Response Model")


@app.get("/get-all-users", description="gives the list of all users", response_model=UserResponseList)
def get_all_users():

    return {
        "users": users
    }


@app.post("/create-user", response_model=UserResponse)
def create_user(user: User):

    users.append(user)

    return user


@app.get("/get-user/{name}", response_model=UserResponse)
def get_user(name: str):

    for index, item in enumerate(users):
        if item.name == name:
            return users[index]

    return {'error': "No name in the db"}



if __name__ == "__main__":
    uvicorn.run('response_model:app', reload=True)