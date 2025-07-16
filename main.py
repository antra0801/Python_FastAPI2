from fastapi import FastAPI

app = FastAPI()

print("hello")

@app.get('/')
def index():
    return {'data':{'name':'antra'}}



