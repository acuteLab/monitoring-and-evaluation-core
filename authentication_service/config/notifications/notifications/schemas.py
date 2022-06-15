from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime


class NotificationeBase(BaseModel):
    message_id: int
    is_deleted: bool
    receiver_id: int
    is_sent: bool
    is_received: bool
    created_on: datetime


class NotificationCreate(NotificationeBase):
    pass


class Notification(NotificationeBase):
    id: int

    class Config:
        orm_mode = True


class MessageBase(BaseModel):
    name: str
    message_body: str
    language_id: int
    created_on: datetime


class MessageCreate(MessageBase):
    pass


class Message(MessageBase):
    id: int

    class Config:
        orm_mode = True


class DeleteMessage(BaseModel):
    ids: list

    class Config:
        orm_mode = True
