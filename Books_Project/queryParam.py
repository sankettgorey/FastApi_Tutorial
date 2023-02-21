from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get('/')
async def welcome(name: str = None):
    if name:
        return {f'Hello {name}'}
    return {'Hello default'}


@app.get('/welcome')
async def welcome(name:str = None):
    if name:
        return {f'Hello {name}'}
    return {'Hello default'}
