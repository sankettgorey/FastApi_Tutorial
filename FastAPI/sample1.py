from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get("/", description='sample api', )
async def hello():
    return {"message": "this is first api"}


@app.get('/content', description='gives list of items')
async def show_content():
    return {
        "content": ['apple', 'orange', 'watermelon']
    }


if __name__ == "__main__":
    uvicorn.run("sample1:app", reload=True)