from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    description: str
    piblished_at: Optional[bool]

app = FastAPI()

@app.get('/')
def index():
    return {'data':{'name':'Test)'}}

@app.get('/about')
def about():
    return {'data':{'about page'}}

@app.post('/blog')
def create_blog(blog: Blog):
    return{'data':blog}

# @app.get('/blog/{id}')
# def show(id:int):
#     return{'data': id}

# @app.get('/blog/category')
# def category():
#     return {'data':'all category'}


# @app.get('/blog')
# def item(limit,published:bool=True):
#     return published

#     if published:
#         return{'data' :f'{limit}件'}
#     else:
#         return{'data':'非公開'}
    



