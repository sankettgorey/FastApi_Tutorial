from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get('/users', description='gives the info of user based on name')
async def get_user(name: str = None):

    return {'name': name}



if __name__ == "__main__":
    uvicorn.run('query_param:app', reload=True)