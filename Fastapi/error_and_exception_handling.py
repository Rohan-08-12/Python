from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

from Python.Fastapi import status_code

app=FastAPI()


# faske database

users={
    1:{"id":1,"name":"Jake"},
    2:{"id":2,"name":"Alice"}
}




@app.get('/users/{user_id}')
def get_user(user_id:int):
    if user_id not in users:
        raise HTTPException(status_code=404,detail="User not found")
        return users[user_id]







# Success codes


# status.HTTP_200_OK              # Success
# status.HTTP_201_CREATED         # Created new resource
# status.HTTP_204_NO_CONTENT      # Success, no content to return

# # Client error codes
# status.HTTP_400_BAD_REQUEST     # Invalid request
# status.HTTP_401_UNAUTHORIZED    # Not authenticated
# status.HTTP_403_FORBIDDEN       # Authenticated but no permission
# status.HTTP_404_NOT_FOUND       # Resource not found
# status.HTTP_409_CONFLICT        # Conflict (e.g., duplicate)

# # Server error codes
# status.HTTP_500_INTERNAL_SERVER_ERROR  # Server error



class User(BaseModel):
    username:str
    email:str


users_db=[]

@app.post('/users',status_code=status.HTTP_201_CREATED)
def create_user(user:User):
    # check for existing user
    for existing_user in users_db:
        if existing_user.username==user.username:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Username '{user.username}' already exists"
            )

    users_db.append(user)
    return user      



@app.get('/users/{username}')
def get_user(username:str):
    for user in users_db:
        if user.username == username:
            return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User '{username}' not found"
    )    


@app.delete('/users/{username}')
def delete_user(username:str):
    for i,user in enumerate(users_db):
        if user.username == username:
            users_db.pop(i)
            return None

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User '{username}' not found"
    )      



# Custom Error Message

app.get("/items")
def create_item(name:str,price:float):
    if price < 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Price cannot be negative",
            headers={"X-Error":"Invalid-Price"}
        )

    if len(name) <3:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Name must be at least 3 characters"
        )

    return {"name":name,"price":price}        



