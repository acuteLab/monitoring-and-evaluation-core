from datetime import timedelta, datetime
import jwt
from fastapi import Depends, APIRouter, HTTPException, status, Header
from authentication.models import User
from sqlalchemy.orm import Session
from fastapi.security.utils import get_authorization_scheme_param
from settings import (
    SECRET_KEY as secret_key,
    ALGORITHM as algorithm,
    RESET_PASSWORD_TOKEN_TIME,
)
from pydantic import ValidationError


def create_access_token(*, data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=60)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=algorithm)
    return encoded_jwt


def create_token_from_email(email: str):
    """
    Create a token that can be used to verify a reset password.

    Expires in 15 minutes.
    """
    to_encode = {
        "email": email,
    }
    expire = datetime.utcnow() + timedelta(minutes=RESET_PASSWORD_TOKEN_TIME)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=algorithm)
    return encoded_jwt


def decode_access_token(*, data: str):
    # try:
        to_decode = data
        return jwt.decode(to_decode, secret_key, algorithm)
    # except:
    #     raise HTTPException(status_code=400, detail="Token has been expired")


def get_account(db_session: Session, id: int):
    return db_session.query(User).filter(User.id == id).first()


def authenticate_request(db, authorization: str = Header(None)):
    print("The function Hitted")
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = decode_access_token(data=authorization)
        try:
            token_data = db.query(User).filter(User.email == payload.get("sub")).first()
            return token_data
        except ValidationError:
            raise credentials_exception
    except jwt.PyJWTError:
        raise credentials_exception


def get_id_from_token(token):
    """Get an id from a signed token."""
    try:
        token = jwt.decode(token, secret_key, algorithms=[algorithm])
    except jwt.ExpiredSignatureError:
        # Signature has expired
        return False
    except Exception:
        return False

    return token.get("id")
