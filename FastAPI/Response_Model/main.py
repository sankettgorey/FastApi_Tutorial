'''
using response model we decide which info to show to client 
and which info to hide
'''


from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel


class User(BaseModel):

    name: str
    age: int
    password: str


class UserResponse(BaseModel):

    name: str
    age: int




app = FastAPI()

@app.get("/get-user", response_model= UserResponse)
def get_user():

    return {
        "name": 'sanket',
        'age': 33,
        'password': 12345
    }



if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)