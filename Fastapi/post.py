from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app=FastAPI();

# class User(BaseModel):
#     name : str
#     email : str
#     age : int



# @app.post('/user')
# def create_user(user : User):
#     return {
#         "message" : "User created",
#         "user":User
#     }    



class Item(BaseModel):
    name : str
    description : Optional[str]
    price : float
    tax : float = 0.0


@app.post('/items')
def create_item(item : Item):
    total = item.price + item.tax
    return {"item" : item , "total" : total}    




# Fastapi validates automatically 


class User(BaseModel):
    name : str
    email : str
    age : int


@app.post('/users')
def create_user(user : User):
    # Validates itself
    return {"message" : "User created" , "user" : User}