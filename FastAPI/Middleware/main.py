from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.middleware("http")
async def middleware(request: Request, call_next):

    print('request received')

    resposne = await call_next(request)

    print('response sent')

    return resposne


if __name__ == "__main__":
    uvicorn.run('main:app')