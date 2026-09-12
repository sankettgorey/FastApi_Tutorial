from fastapi import FastAPI, status, HTTPException
import uvicorn

from pydantic import BaseModel


class User(BaseModel):

    id: int
    name: str
    age: int
    email: str
    password: str



class UserResponse(BaseModel):

    id: int
    name: str
    age: int
    email: str

class UserCreated(BaseModel):

    message: str
    data: UserResponse


class UserList(BaseModel):

    message: str
    users: list[UserResponse]


users = []

app = FastAPI(title="CRUD operations with status codes")

@app.post("/create-user", response_model=UserCreated, status_code=status.HTTP_201_CREATED)
def create_user(user: User):

    for existing_user in users:
        if existing_user.id == user.id:
            raise HTTPException(
                status_code=409,
                detail="User with the id already exists"
            )

    users.append(user)

    return {
        "message": "user created successfully",
        "data": user
    }


@app.get("/get-users", response_model=UserList, status_code=status.HTTP_200_OK)
def get_users():

    return {
        "message": "List of users",
        "users": users
    }

# get user by name
@app.get("/get-user-by-name/{name}", response_model=UserCreated, status_code=status.HTTP_200_OK)
def get_user(name: str):

    for user in users:
        if user.name == name:
            return {
                "message": "User Found",
                "data": user
            }

    raise HTTPException(status_code=404, detail="User not found")


@app.delete("/delete-user/{name}", response_model=UserCreated, status_code=status.HTTP_200_OK)
def delete_user(name: str):

    for index, user in enumerate(users):
        if user.name == name:
            users.pop(index)

            print(f"deleted: {user}")
            print(f'users: {users}')

            return {
                "message": "user deleted successfully",
                "data": user
            }

    raise HTTPException(status_code=404, detail="User not found")


if __name__ == "__main__":
    uvicorn.run("http_exception_with_crud:app")