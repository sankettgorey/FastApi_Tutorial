from fastapi import FastAPI, status, HTTPException, Request
from fastapi.responses import JSONResponse

import uvicorn

class UserNotFound(Exception):
    pass

users = []
app = FastAPI()

@app.exception_handler(UserNotFound)
def user_not_found(request:Request, exec: UserNotFound):

    return JSONResponse(
        status_code=404,
        content={
            "status": "error",
            "message": "user not found"
        }
    )


@app.get("/get-user/{name}", status_code=status.HTTP_200_OK)
def get_user(name: str):

    for user in users:
        if user.name == name:
            return {
                "message": "user found",
                "data": user
            }

    raise UserNotFound()


if __name__ == "__main__":
    uvicorn.run('custom_exception:app')
