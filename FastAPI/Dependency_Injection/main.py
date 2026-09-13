from fastapi import FastAPI, Depends
import uvicorn



def common_function():

    return {
        "message": "common function executed"
    }


app = FastAPI()


@app.get("/profile")
def profile(output = Depends(common_function)):

    return output



@app.get("/home")
def home(output = Depends(common_function)):

    return output




if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)