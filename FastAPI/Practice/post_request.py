from pydantic import BaseModel

from fastapi import FastAPI
import uvicorn


users = []

app = FastAPI()


class User(BaseModel):

    id: int
    name: str
    age: int
    email: str


@app.post("/create-user")
def create_user(user: User):

    users.append(user)

    return {
        "messages": "user created successfully",
        "data": user
    }


# get all users
@app.get("/get-users")
def get_users():

    return {
        "message": "list of users",
        "data": users
    }


# get specific user using path param
@app.get("/get-user/{user_id}")
def get_user(user_id: int):

    for index, user in enumerate(users):
        if user.id == user_id:
            return {
                "message": "User found",
                "details": users[index]
            }

    return {"error": "user not found"}



@app.put("/update-user/{user_id}")
def update_user(user_id: int, new_user: User, notify: bool = False):

    for index, user in enumerate(users):
        if user.id == user_id:
            users[index] = new_user
            return {
                "message": "user updated",
                "notify": notify,
                "data": new_user
            }


if __name__ == "__main__":
    uvicorn.run("post_request:app", reload= True)