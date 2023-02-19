from fastapi import FastAPI
import uvicorn


app = FastAPI()

message = {'message': 'first API response'}


@app.get('/')
async def welcome():
    return message


if __name__ == '__main__':
    uvicorn.run(app)
