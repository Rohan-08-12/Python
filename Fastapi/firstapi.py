# 1. GET / - Return {"status": "API is running"}

# 2. GET /greet/{name} - Return {"greeting": "Hello {name}!"}

# 3. GET /square/{number} - Return {"number": number, "square": number*number}
#    Example: /square/5 returns {"number": 5, "square": 25}

# Your code here:
from fastapi import FastAPI

app = FastAPI()

# Write your routes here


@app.get('/')
def read_root():
    return {"status":"API is running"}

@app.get('/greet/{name}')
def greet(name:str):
    return {"greeting":f"Hello {name}"}    


@app.get('/square/{number}')
def square_num(number:int):
    return {"number" : number , "square" : number * number}