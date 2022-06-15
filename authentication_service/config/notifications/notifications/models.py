from __future__ import absolute_import
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Text
from sqlalchemy.orm import relationship
from config.database import Base
from datetime import datetime
from utils.languages.models import SystemLanguage


class SystemNotification(Base):
    __tablename__ = "system_notifications"

    id = Column(Integer, primary_key=True, index=True)
    message_id = Column(Integer, ForeignKey("system_messages.id", ondelete="CASCADE"))
    is_deleted = Column(Boolean, default=False)
    receiver_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    is_sent = Column(Boolean, default=False)
    is_received = Column(Boolean, default=False)
    created_on = Column(DateTime, default=datetime.now())
    updated_on = Column(DateTime, default=datetime.now())

    user = relationship("User", back_populates="notifications")
    message = relationship("SystemMessage", back_populates="notifications")


class SystemMessage(Base):
    __tablename__ = "system_messages"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    message_body = Column(Text)
    language_id = Column(Integer, ForeignKey("system_languages.id", ondelete="CASCADE"))
    created_on = Column(DateTime, default=datetime.now())

    notifications = relationship("SystemNotification", back_populates="message")
    language = relationship("SystemLanguage", back_populates="message")
