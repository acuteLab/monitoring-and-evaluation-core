from typing import List, Optional
from pydantic import BaseModel


class LanguageBase(BaseModel):
    name: str
    code: str


class LanguageCreate(LanguageBase):
    pass


class Language(LanguageBase):
    id: int

    class Config:
        orm_mode = True
