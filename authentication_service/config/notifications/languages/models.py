from __future__ import absolute_import
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Text
from sqlalchemy.orm import relationship
from config.database import Base
from datetime import datetime


class SystemLanguage(Base):
    __tablename__ = "system_languages"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    code = Column(String)
    created_on = Column(DateTime, default=datetime.now())
    message = relationship("SystemMessage", back_populates="language")

    def __str__(self):
        return self.code
