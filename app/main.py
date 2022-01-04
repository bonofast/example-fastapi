# V1: CRUD with variable array
# V2: CRUD with traditional SQL
# V3: CRUD with ORM
# V4: Router
from fastapi import FastAPI
from .routers import post, user, auth, vote
#from . import models
#from .database import engine
#from .config import settings
from fastapi.middleware.cors import CORSMiddleware


# models.Base.metadata.create_all(bind=engine)


app = FastAPI() 

origins = []
# origins = ["https://www.google.com", "https://www.youtube.com"]
# origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

# request Get method url: "/"; order matters for functions having the same path
@app.get("/")   #path operation (route) decorator, "/" means root path
def root():
    return {"message": "Hello World"}