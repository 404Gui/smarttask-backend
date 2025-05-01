from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    password: str

# schema para login
class UserLogin(BaseModel):
    username: str
    password: str

# Dados retornados (sem senha)
class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True
