from __future__ import absolute_import
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Text
from config.database import Base
from datetime import datetime
from uuid import uuid4, SafeUUID

# Adding Authentication related models
class User(Base):
    __tablename__ = "users"

    id = Column(String, default=uuid4, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True)
    password = Column(String, nullable=True)
    photo = Column(String, default="user.png")
    first_name = Column(String(234))
    middle_name = Column(String, nullable=True)
    last_name = Column(String(300))
    phone_number = Column(String)
    is_staff = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    is_superuser = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    created_on = Column(DateTime)
    updated_on = Column(DateTime, default=datetime.now())

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    @property
    def get_phone(self):
        return self.phone_number

    @property
    def get_email(self):
        self.email


class Role(Base):
    __tablename__ = "roles"
    id = Column(String, default=uuid4, primary_key=True, index=True)
    name = Column(String, nullable=True)
    created_on = Column(DateTime, default=datetime.now())
    updated_on = Column(DateTime, default=datetime.now())
