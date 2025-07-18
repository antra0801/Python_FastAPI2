from fastapi import FastAPI
import uvicorn
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Blog(BaseModel):
    title : str
    body :str
    published : Optional[bool]=True

@app.get('/')
def index():
    return {'data':'blog List'}

@app.post('/blog')
def post_method(request_body : Blog):
    return {'response' : f"hello folks request body got me the validated data ,title = {request_body.title}, body = {request_body.body}, published= {request_body.published}"}

@app.get('/blog')
def query_param_func(
    published: bool, 
    limit:int =10, 
    sort : Optional[str] = None ):
    # return published
    if published:
        return {'data' : f'{limit} {published} published blogs from the db'}
    
    else:
        return {'data' : f'{limit} hello blogs from the db' }

@app.get('/blog/{id}')
def show(id : int):
    return {'data' : id}

@app.get('/blog/{id}/comments')
def comments(id):
    return {'data': {'1' , '2'}}


#constant api should not be the under the dynamic ones.
@app.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished blogs'}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000 , reload=True)  