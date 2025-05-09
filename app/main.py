from fastapi import FastAPI, Depends
from app.routes import users, tasks, auth_google
from app.auth import oauth2_scheme
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

origins = os.getenv("CORS_ALLOWED_ORIGINS", "").split(',')

app.include_router(users.router)
app.include_router(tasks.router)
app.include_router(auth_google.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
