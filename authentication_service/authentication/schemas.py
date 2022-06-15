from typing import List, Optional
from uuid import uuid4
from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: str
    password: str
    is_active: bool
    is_staff: bool
    is_superuser: bool

    class Config:
        orm_mode = True


class ChangePassword(BaseModel):
    password: str

    class Config:
        orm_mode = True


class ResetPasswordRequest(BaseModel):
    email: str

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str = None


class UserAuthenticate(UserBase):
    password: str


class RoleBase(BaseModel):
    name: str


class RoleCreate(RoleBase):
    pass


class Role(RoleBase):
    id: int

    class Config:
        orm_mode = True
