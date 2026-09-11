''' this file creates a path parameter dynamically '''

'''
here because we are using data type validation, we dont 
need to separately handle exception related to data type 
coming from user
'''


from fastapi import FastAPI
import uvicorn


app = FastAPI()

@app.get("/users/{user_id}", description="gives user details based on user id")
async def get_user(user_id: int, name: str = None):

    return {
        'user_id': user_id,
        'name': name,
        "total_expense": 12345
    }




if __name__ == "__main__":
    uvicorn.run("dynamic_path_param:app", reload=True)