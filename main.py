from typing import Optional
from fastapi import FastAPI

app=FastAPI()

@app.get('/')
def index():
    return {'data':{'name':'Suhaas'}}


@app.get('/blog')
def index(limit = 10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data':f'{limit} published blogs from the db'}
    else:
        return {'data':f'{limit} blogs from the db'}


@app.get('/about')
def about():
    return {'data':'about page'}


@app.get('/blog/{id}')
def show_blog(id: int):
    return {'data':id}


@app.get('/blog/{id}/comments')
def comments(id):
    return {'data':{'comment 1','comment 2'}}