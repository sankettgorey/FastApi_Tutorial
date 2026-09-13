from fastapi import FastAPI, Request, status
import uvicorn

import time


app = FastAPI()

'''
middleware is used to log and check the processing time each api takes.
we also use middleware to validate the incoming request.
call_next param used here sends the request to next function for further processing.
we have to kind of whitelist the incoming request whether its http or https for which
we use middleware
'''

@app.middleware("http")
async def log_middleware(request: Request, call_next):

    start_time = time.time()

    response = await call_next(request)

    processing_time = time.time() - start_time

    print(f"Path: {request.url.path} | Time: {processing_time}")

    return response


if __name__ == "__main__":
    uvicorn.run('middleware_and_logging:app')