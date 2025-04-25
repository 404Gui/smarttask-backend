from pydantic import BaseModel, EmailStr

# Dados base (usado como base para criação e leitura)
class UserBase(BaseModel):
    username: str
    email: EmailStr


# Dados recebidos na criação de um usuário (tem senha)
class UserCreate(UserBase):
    password: str


# Dados retornados (sem senha)
class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True
