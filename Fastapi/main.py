from fastapi import FastAPI;

# Create app instance

app=FastAPI();

# get-route

@app.get('/')
def read_root():
    return {"message": "Hello World"}


@app.get('/hello/{name}')
def say_hello(name: str):
    return {"message": f"Hello {name}!"}  