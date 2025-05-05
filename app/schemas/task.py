from pydantic import BaseModel
from typing import Optional, Literal
from datetime import datetime

class TaskBase(BaseModel):
    title: str
    description: str | None = None
    priority: Optional[Literal['baixa', 'média', 'alta']] = 'média'
    due_date: Optional[datetime] = None


class TaskCreate(TaskBase):
    pass

class TaskRead(TaskBase):
    id: int
    completed: bool
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True



class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None
    priority: Optional[Literal['baixa', 'média', 'alta']] = None
    due_date: Optional[datetime] = None


