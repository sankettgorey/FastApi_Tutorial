from fastapi import FastAPI
import uvicorn

from pydantic import BaseModel


app = FastAPI()


# simple way of accepting data from user in post method
@app.post("/create-user")
async def create_user(name: str, age: int):

    return {
        "message": 'user created',
        "details": {
            'name': name,
            'age': age
        }
    }
#######################################################

# second way of accepting data from user: using dict param
@app.post("/create-user1")
async def create_user(user: dict):

    return {
        'message': 'user create successfully',
        "data": user
    }
#######################################################

# third wasy of accepting data from user using pydantic models. 
# this is the recommeded method as it validates data by default


class User(BaseModel):

    name: str
    age: int
    email: str


@app.post("/create-user2")
def create_user(user: User):

    return {
        "message": "user created successfully",
        "data": user
    }


if __name__ == "__main__":
    uvicorn.run('first_post:app', reload= True)