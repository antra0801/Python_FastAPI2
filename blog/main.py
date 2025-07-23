from fastapi import FastAPI
from . import schemas

app = FastAPI()


@app.post('/blog1')
def create(request_body : schemas.BlogClass):
    return request_body

