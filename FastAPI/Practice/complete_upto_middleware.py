from fastapi import FastAPI, Request, HTTPException, status, Header, Depends
from fastapi.responses import JSONResponse
import uvicorn

import time
from pydantic import BaseModel


users = []

app=FastAPI(title="FastAPI Practice Modules")

# defining custom exception classes
class AppError(Exception):

    status_code = 400
    error_code = "Not able to process"

    def __init__(self, message):
        self.message = message
        super().__init__(message)


class NotFoundError(AppError):

    status_code=404
    error_code="RESOURCE NOT FOUND"


class ConflictError(AppError):

    status_code=409
    error_code='DUPLICATE ENTRY'


# creating custom exception handler
@app.exception_handler(AppError)
def exception_handler(request: Request, exc: AppError):

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "message": exc.message,
            "error_code": exc.error_code
        }
    )


# ----------------------------------------------------------------------------

# creating dependency injection
def authentication(token = Header(...)):

    if token == "myauthtoken":
        return {
            "message": "user verified",
            "status_code": "authtication successful"
        }

    raise HTTPException(status_code=422, detail="Auth not successful")

# ----------------------------------------------------------------------------

# creating middleare
@app.middleware("http")
async def middleware(request: Request, create_next):

    start_time = time.time()

    response = await create_next(request)

    print(f"Processing time for the request {request.url} is: {time.time() - start_time}")

    return response

# ----------------------------------------------------------------------------

# creating response models

class User(BaseModel):

    id: int
    name: str
    age: int
    email: str
    password: str


class UserCreated(BaseModel):

    name: str
    age: int
    email: str
    # password: str


class UserList(BaseModel):

    message: str
    users: list[UserCreated]



@app.get("/get-users", status_code=status.HTTP_200_OK, response_model=UserList)
def get_users(token = Depends(authentication)):

    return {
        "message": "List of all users",
        "users": users
    }


@app.post("/create-user", status_code=201)
def create_user(user: User, token = Depends(authentication)):

    for each_user in users:
        if each_user.name == user.name:
            raise ConflictError(f"User with the name {user.name} already exists in the DB")

    users.append(user)

    return {
        "message": "User created successfully",
        "user": [user]
    }


@app.get("/get-user/{name}", status_code=200, response_model=UserList)
def get_user(name: str, token = Depends(authentication)):

    for user in users:
        if user.name == name:
            return {
                "message": "User found",
                "users": [user]
            }

    raise NotFoundError(f"User with the name {name} not found in the DB")


@app.delete("/delete-user/{name}", response_model=UserList, status_code=status.HTTP_200_OK)
def delete_user(name: str, token = Depends(authentication)):

    for index, user in enumerate(users):
        if user.name == name:
            users.pop(index)

            return {
                "message": "User deleted successfully",
                "users": [user]
            }

    raise NotFoundError(f"User with the name {name} not fuond in the DB")


if __name__ == "__main__":
    uvicorn.run("complete_upto_middleware:app", reload=True)