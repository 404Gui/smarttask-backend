from app.db import engine
from app.models.task import Task

Task.metadata.create_all(bind=engine)
