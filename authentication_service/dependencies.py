from typing import Generator
import jwt
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from config.database import engine, SessionLocal
from pydantic import ValidationError
from authentication.authenticate import get_db
from authentication.auth_token import decode_access_token
from authentication.models import Base, User
from config.database import Base


reusable_oauth2 = OAuth2PasswordBearer(tokenUrl="authenticate")


def create_tables():
    return Base.metadata.create_all(engine)


def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(reusable_oauth2)
):
    try:
        token_data = decode_access_token(data=token)
    except:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid token ware given",
        )
    user = db.query(User).filter(User.email == token_data.get("sub")).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if user.is_active == False:
        raise HTTPException(status_code=400, detail="Inactive user")
    return user


def get_current_active_superuser(current_user: User = Depends(get_current_user),):
    if current_user.is_system_admin == False:
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return current_user
