from fastapi import FastAPI, status, HTTPException
import uvicorn

from pydantic import BaseModel


app = FastAPI()


# sending customied response to frontend
'''
here fastapi will create http status code on its own
even if we dont specify explicitely
'''
@app.get("/get-all-users", status_code=status.HTTP_200_OK)
def get_all_users():

    return {
        "message": "all users data fetched",
        "status": "success",
        "data": {
                    "name": "sanket",
                    "age": 33
                }
    }


@app.post("/create-user", status_code=status.HTTP_201_CREATED)
def create_user():

    return {
        "message": "user created",
    }



@app.get("/get-user/{id}", status_code=status.HTTP_200_OK)
def get_user(id: int):

    if id != 1:
        raise HTTPException(status_code=404, detail='user not found')

    return {
        "message": "user found",
        "data": {
            "name": "sanket",
            "age": 33
        }
    }






if __name__ == "__main__":
    uvicorn.run('main:app', reload=True)