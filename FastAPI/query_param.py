from fastapi import FastAPI
import uvicorn

app = FastAPI(summary='# this is the app for query param demo',
              description='multiple query param')


# combinaation of both path param and query param
@app.get('/users/{user_id}')
async def get_user(name: str = None):

    if name:

        return {
            # 'user_id': user_id,
            'name': name,
            'total_expense': 12000
        }

    return {
        'user_id': 4,
        'name': None,
        'total_expense': None
    }



# query param with default value
@app.get('/products')
async def products(limit: int = 10, name: str = None, ):
    return {'products': limit}



if __name__ == "__main__":
    uvicorn.run('query_param:app', reload=True)