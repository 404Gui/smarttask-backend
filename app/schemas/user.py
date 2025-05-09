from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    password: str

# schema para login
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Dados retornados (sem senha)
class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True
