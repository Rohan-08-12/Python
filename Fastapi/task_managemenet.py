# Models:
# TaskIn: title (str), description (str), priority (int, default=1)
# TaskOut: id (int), title (str), description (str), priority (int), completed (bool)

# Endpoints:

# 1. POST /tasks (status 201)
#    Body: TaskIn
#    Returns: TaskOut with id=1 and completed=False
#    (For now, always return id=1, we'll add database later)

# 2. GET /tasks/{task_id} (status 200)
#    Returns: TaskOut
#    (For now, return dummy data with the given task_id)

# 3. DELETE /tasks/{task_id} (status 204)
#    Returns: None

from asyncio import Task
from re import S
from fastapi import FastAPI, status
from pydantic import BaseModel
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

app = FastAPI()

# Your code here



class TaskIn(BaseModel):
    title:str
    description:str
    priority:int=1


class TaskOut(BaseModel):
    id:int
    title:str
    description:str
    priority:int
    completed:bool


@app.post('/tasls',status_code=HTTP_201_CREATED,response_model=TaskOut)
def create_user(task:TaskIn):
        return TaskOut(
        id=1,
        title=task.title,
        description=task.description,
        priority=task.priority,
        completed=False
    )   




@app.get('/tasks/{task_id}',status_code=HTTP_200_OK,response_model=TaskOut)
def get_task(task_id:int):
        return TaskOut(
        id=task_id,
        title="Sample Task",
        description="This is a sample task",
        priority=1,
        completed=False
    )



@app.delete('/task,{task_id}',status_code=HTTP_204_NO_CONTENT)
def delete_post(task_id:int):
    return None