# V1: CRUD with variable array
from random import randrange
from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body


app = FastAPI() 


class Post(BaseModel):
    title: str
    content: str
    published:  bool = True
    rating: Optional[int] = None


my_posts = [{"title": "title of post1", "content": "content of post1", "id": 1}, {"title": "favorite food", "content": "I like pizza", "id": 2}]


def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p


def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i
            

# request Get method url: "/"; order matters for functions having the same path
@app.get("/")   #path operation (route) decorator, "/" means root path
def root():
    return {"message": "Hello World"}


@app.get("/posts")  #get is the method; "/" is the path
def get_posts():    #get_posts is a function
    return {"data": my_posts}


#@app.post("/createposts")
#def create_posts(payload: dict = Body(...)):    #tab Body would auto import the Body library at the top of this file
#    print(payload)
#    return {"new_post": f"title {payload['title']} content: {payload['content']}"}

#add schema: title str, content str

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    #print(post)
    #print(post.dict())
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}


@app.get("/posts/{id}") #{id} represents a path parameter
# def get_post(id: int, response: Response):
def get_post(id: int):
    post = find_post(id)
    if not post:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"post with id: {id} was not found"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
    return {"post_details": post} 


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    # deleting posts
    # find the index in the array that has required ID
    # my_post.pop(index)
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")
    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict
    return {"data": post_dict}