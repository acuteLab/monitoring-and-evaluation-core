from typing import List
from fastapi import Depends, APIRouter, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from authentication import operations, models, schemas
from config.database import SessionLocal, engine
from dependencies import get_current_user
from starlette.requests import Request


from .authenticate import create_access_token,authenticate_user

router = APIRouter()

# Dependency
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/user")
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = operations.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return operations.create_user(db=db, user=user)


@router.get("/users", response_model=List[schemas.User])
async def read_users(db: Session = Depends(get_db)):
    users = operations.get_users(db)
    return users


@router.get("/user", response_model=schemas.User)
async def get_user_by_id(user_id: str, db: Session = Depends(get_db)):
    db_user = operations.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.put("/change-username")
async def change_user_name(
    token: str, details: schemas.UserBase, db: Session = Depends(get_db)
):
    current_user = get_current_user(db, token)
    return operations.change_username(db, details.email, current_user.id)


@router.put("/activate-user")
async def activate_user_account(
    user_id: str, background: BackgroundTasks, db: Session = Depends(get_db)
):
    return operations.activate_user(db, user_id, background)


@router.put("/deactivate-user")
async def deactivate_user_account(
    user_id: str, background: BackgroundTasks, db: Session = Depends(get_db)
):
    return operations.deactivate_user(db, user_id, background)


@router.delete("/delete-user")
async def delete_user_account(
    user_id: str, background: BackgroundTasks, db: Session = Depends(get_db)
):
    return operations.delete_user(db, user_id, background)


@router.post("/request-reset-password")
async def request_password_reset(
    request_email: schemas.ResetPasswordRequest,
    background: BackgroundTasks,
    db: Session = Depends(get_db),
):
    request = Request
    return operations.request_reset_password(
        db, request_email.email, background, request
    )


@router.put("/reset-password")
async def reset_user_password(
    token: str, details: schemas.ChangePassword, db: Session = Depends(get_db)
):
    return operations.reset_password(db, details.password, token)


@router.put("/change-password")
async def change_user_password(
    token: str,
    background: BackgroundTasks,
    details: schemas.ChangePassword,
    db: Session = Depends(get_db),
):
    current_user = get_current_user(db, token)
    return operations.change_password(db, details.password, current_user.id, background)
