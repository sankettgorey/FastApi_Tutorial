from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def hello(name):
    return {f'welcome {name}'}