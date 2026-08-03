from fastapi import FastAPI

app = FastAPI()

# @app.get('/')
# def index():

#     return 'hi'


@app.get('/')
def index():

    return {
        'data':
        {
            'name': 'Sanket'
        }
    }


@app.get('/about')
def about():
    return {
        "data": "about page"
    }