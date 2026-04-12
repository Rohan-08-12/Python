from fastapi import FastAPI, status

app = FastAPI()

@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    return user

@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    return None  # 204 = No content





# status.HTTP_200_OK          # Success
# status.HTTP_201_CREATED     # Created
# status.HTTP_204_NO_CONTENT  # Deleted
# status.HTTP_400_BAD_REQUEST # Client error
# status.HTTP_404_NOT_FOUND   # Not found
# status.HTTP_500_INTERNAL_SERVER_ERROR  # Server error


