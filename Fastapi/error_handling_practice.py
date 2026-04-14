# Create a simple task management API with error handling

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List

from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND

app = FastAPI()

class Task(BaseModel):
    id: int
    title: str
    completed: bool = False

tasks: List[Task] = []

# TODO: Implement these endpoints with proper error handling:

# 1. POST /tasks - Create task
#    - Return 409 if task with same ID exists
#    - Return 201 on success


@app.post('/tasks',status_code=HTTP_201_CREATED)
def create_task(task:Task):
    for existing_task in task:
        if existing_task.id == task.id:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                details=f"Task with ID {task.id} already exists"
            )
    tasks.append(task)
    return task        

   

# 2. GET /tasks/{task_id} - Get task
#    - Return 404 if not found


@app.get('/tasks/{task_id}')
def get_task(task_id:int):
    for task in tasks:
        if task.id == task_id:
            return task

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Task {task_id} not found"
    )        

# 3. PUT /tasks/{task_id} - Update task
#    - Return 404 if not found
#    - Return 200 on success


@app.put('/tasks/{task_id}')
def update_task(task_id : int , updated_task=Task):
    for i , task in enumerate(tasks):
        if task.id == task_id:
            task[i] =updated_task
            return updated_task

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Task {task_id} not found"
    )        


# 4. DELETE /tasks/{task_id} - Delete task
#    - Return 404 if not found
#    - Return 204 on success


@app.delete('/tasks/{task_id}',status_code=HTTP_404_NOT_FOUND)
def delete_task(task_id : int) :
    for i , task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(i)
            return None
    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = f"Task {task_id} not found"
    )        
# Your code here



