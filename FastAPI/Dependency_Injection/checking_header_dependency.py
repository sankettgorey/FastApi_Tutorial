from fastapi import FastAPI, HTTPException, Header, Depends
import uvicorn


def verify_token(token: str = Header(...)):

    if token != 'myaccesstoken':
        raise HTTPException(status_code=401, detail="unauthorized user")

    return {
        "user": "Authorized"
    }


app = FastAPI()

@app.get("/verify")
def varify(user = Depends(verify_token)):

    return {
        "message": "user verified",
        "user": user
    }


if __name__ == "__main__":
    uvicorn.run('checking_header_dependency:app', reload=True)