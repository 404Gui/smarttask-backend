from fastapi import FastAPI, Depends
from app.routes import users, tasks
from app.auth import oauth2_scheme

app = FastAPI()

app.include_router(users.router)
app.include_router(tasks.router)
