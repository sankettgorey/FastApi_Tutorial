from fastapi import FastAPI, Depends, status, Request, Header, HTTPException
from fastapi.responses import JSONResponse

from pydantic import BaseModel

# creating user model
class User(BaseModel):

    # id: int
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


