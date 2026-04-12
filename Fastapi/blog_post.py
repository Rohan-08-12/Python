# Create a BlogPost model with:
# - title: str
# - content: str
# - author: str
# - tags: list of strings (optional, default empty list)
# - published: bool (optional, default False)

# Create these endpoints:

# 1. POST /posts
#    Accepts BlogPost in body
#    Returns {"message": "Post created", "post": post_data}

# 2. POST /posts/{post_id}/comment
#    Path param: post_id (int)
#    Body: {"author": str, "text": str}
#    Returns {"post_id": post_id, "comment": comment_data}

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Your code here


class BlogPost(BaseModel):
    title:str
    content:str
    author:str
    tags:List[str] = []
    published : bool = False


class Comment(BaseModel):
    author:str
    content:str


@app.post('posts')
def create_post(post:BlogPost):
    return {"message": "Post created", "post": post}



@app.post('/posts/{post_id}/comment')
def add_comment(post_id : int , comment:Comment):
    return {"post_id": post_id, "comment": comment}
