# 1. GET /add/{a}/{b} 
#    Returns {"a": a, "b": b, "result": a+b}
#    Example: /add/5/3 → {"a": 5, "b": 3, "result": 8}

# 2. GET /multiply
#    Query params: num1, num2
#    Returns {"num1": num1, "num2": num2, "result": num1*num2}
#    Example: /multiply?num1=4&num2=5 → {"num1": 4, "num2": 5, "result": 20}

# 3. GET /power
#    Query params: base, exponent (exponent default=2)
#    Returns {"base": base, "exponent": exp, "result": base**exp}
#    Example: /power?base=3 → {"base": 3, "exponent": 2, "result": 9}
#    Example: /power?base=2&exponent=5 → {"base": 2, "exponent": 5, "result": 32}

from fastapi import FastAPI

app = FastAPI()

# Your code here


@app.get('/add/{a}/{b}')
def add_num(a:int , b:int):
    return {"a":a,"b":b,"a+b":a + b}



@app.get('/multiply')
def multiply(num1 : int , num2 : int):
    return {"num1" : num1 , "num2" : num2 , "result" : num1 * num2}    



@app.get('power')
def power(base : int , exponent : int = 2):
    return {"base" : base , "exponent" : exponent , "result" : base ** exponent}    