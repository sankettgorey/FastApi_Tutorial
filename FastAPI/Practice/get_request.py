from fastapi import FastAPI 
import uvicorn


app = FastAPI()


# greet api
@app.get('/')
def greet():

    return {'message': 'Welcome to demo appliation for API testing'}


@app.get('/user/{user_id}')
async def get_user(user_id: int):

    return {
        'name': 'Sanket',
        'user_id': user_id,
        'total_expense': 100000
    }


# get products info based on name
@app.get('/products')
async def get_products(name: str, limit: int = 10):

    return {
        'name': name,
        'user_id': 11,
        'limit': limit
    }


if __name__ == "__main__":
    uvicorn.run('get_request:app')