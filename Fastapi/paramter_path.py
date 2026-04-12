from fastapi import FastAPI


app=FastAPI();

@app.get('/user/{user_id}')
def get_user(user_id:int):
    return {"user_id": user_id, "name": "Alice"}



@app.get('/posts/{post_id}/comments/{comment_id}')    
def get_comment(post_id : int , comment_id : int):
        return {
        "post_id": post_id,
        "comment_id": comment_id,
        "text": "Great post!"
    }