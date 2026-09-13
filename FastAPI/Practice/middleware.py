from fastapi import FastAPI, Request, HTTPException
import uvicorn

app = FastAPI(title="Middleware Demo")


@app.middleware("http")
async def track_incoming_request(request: Request, call_next):

    print('before calling main fucntion')

    response = await call_next(request)

    print('adter calling main function')

    # response = f"This is the modified response: {response}"

    return response


if __name__ == '__main__':
    uvicorn.run('middleware:app', reload=True)