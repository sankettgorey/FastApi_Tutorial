from fastapi import FastAPI
import uvicorn

from pydantic import BaseModel


app = FastAPI()


todo_list = []



class Create(BaseModel):

    id: int
    title: str
    completed: bool



# api to create todo list
@app.post("/create-todo")
def create(todo: Create):

    todo_list.append(todo)

    return {
        "message": "TODO created successfully",
        "data": todo
    }



# api to fetch all todo data
@app.get("/get-todo")
def get_todo():

    return todo_list


# api to get only only todo task
@app.get("/get-todo/{todo_id}")
def get_todo_id(todo_id: int):

    for todo in todo_list:

        if todo.id == todo_id:
            return todo

    return {'error': "data not found"}




@app.put("/update-todo/{todo_id}")
def update(todo_id: int, updated: Create):

    for index, todo in enumerate(todo_list):
        if todo.id == todo_id:
            todo_list[index] = updated

            return {'message': 'data updated successfully',
                    'data': updated}

    return {"error": "data not found"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)