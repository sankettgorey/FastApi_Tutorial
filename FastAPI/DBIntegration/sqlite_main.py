'''
in this file, we will use sqlite to create the db, conncet with it
and create table, and fetch the data from it
'''

import sqlite3

from fastapi import FastAPI, status

app = FastAPI()

# setting up connection and creating db
conn = sqlite3.connect("test.db", check_same_thread=False)

# connecting with the db
cursor = conn.cursor()

# executing the query

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS todos(
    id INTEGER PRIMARY KEY,
    title TEXT,
    completed TEXT
    )
    """
)

# saving the change
conn.commit()



@app.get("/home", status_code=status.HTTP_200_OK)
def home():

    return {
        "message": "db conncetion successful"
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run('main:app', reload=True)