from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get('/users/{user_id}')
async def get_user(user_id: int):
    return {'user_id': user_id}



if __name__ == "__main__":
    uvicorn.run('dynamic_path_param:app')