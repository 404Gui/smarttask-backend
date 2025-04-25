from app.db import engine
from app.models.task import Task
from app.models.user import User

Task.metadata.create_all(bind=engine)
User.metadata.create_all(bind=engine)
