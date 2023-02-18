from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
async def welcome():
    return {'Hello': 'First api response'}

if __name__ == '__main__':
    uvicorn.run(app)