from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Request
import jwt
from jwt import PyJWTError
from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter, HTTPException, BackgroundTasks
from starlette import status
from starlette.status import (
    HTTP_200_OK,
    HTTP_401_UNAUTHORIZED,
    HTTP_201_CREATED,
    HTTP_409_CONFLICT,
)
from datetime import timedelta
from config.database import engine, SessionLocal
from authentication.auth_token import (
    secret_key as SECRET_KEY,
    algorithm as ALGORITHM,
    get_account,
)
from authentication.schemas import TokenData
from authentication.schemas import Token
from authentication import models, schemas, operations
from authentication.auth_token import (
    decode_access_token,
    create_access_token,
    authenticate_request,
)


ACCESS_TOKEN_EXPIRE_MINUTES = 60

router = APIRouter()


# Dependency


def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# Session.execute("SET search_path TO client1")


# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="authenticate")


@router.post("/login", response_model=schemas.Token)
def authenticate_user(user: schemas.UserAuthenticate, db: Session = Depends(get_db)):
    db_user = operations.get_user_by_username(db, username=user.email)
    if db_user is None:
        raise HTTPException(
            status_code=400,
            detail="There is no user with this email Address please Register",
        )
    elif db_user.is_active == False:
        raise HTTPException(
            status_code=400,
            detail="Sorry the user Account is not active please communicate with your adminstartor to activate your account !!!",
        )
    else:
        is_password_correct = operations.check_username_password(db, user)
        if is_password_correct is False:
            raise HTTPException(
                status_code=400, detail="Sorry Incorrect Credentials ware given !!!"
            )
        else:
            access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

            access_token = create_access_token(
                data={"sub": user.email}, expires_delta=access_token_expires
            )
            return {"access_token": access_token, "token_type": "Bearer"}


@router.post("/verify", status_code=HTTP_200_OK)
def verify_account(token: str = "", db_session: Session = Depends(get_db)):
    return operations.mark_account_as_verified_and_active(db_session, token)


@router.post("/authenticate", status_code=HTTP_200_OK)
def authenticate(token: str = "", db_session: Session = Depends(get_db)):
    return authenticate_request(db_session, token)

