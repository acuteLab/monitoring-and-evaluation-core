from typing import List
from fastapi import FastAPI, File, UploadFile, Request
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from utils.notifications import models
from utils.notifications import schemas
from utils.notifications.operations import *
from authentication.authenticate import get_db
from dependencies import get_current_user


router = APIRouter()


@router.post("/create_message", response_model=schemas.Message)
def create_messages(
    message_details: schemas.MessageCreate, db: Session = Depends(get_db)
):
    check_name_and_lang = (
        db.query(models.SystemMessage)
        .filter(
            SystemMessage.name == message_details.name
            and SystemMessage.language_id == message_details.laguage_id
        )
        .first()
    )
    if check_name_and_lang:
        raise HTTPException(status_code=400, detail="Sorry message already exist")
    return create_message(db, message_details)


@router.get("/messages", response_model=List[schemas.Message])
def messages(db: Session = Depends(get_db)):
    return get_messages(db)


@router.post("/create_notification", response_model=schemas.Notification)
def notification_create(
    notification_details: schemas.NotificationCreate, db: Session = Depends(get_db)
):
    return create_notification(db, notification_details)


@router.get("/notifications/{token}", response_model=List[schemas.Notification])
def notifications(token: str, db: Session = Depends(get_db)):
    current_user = get_current_user(db, token)
    return get_notifications(db, current_user.id)


@router.delete("/delete_notification")
def delete_notifications(
    notification_ids: schemas.DeleteMessage, db: Session = Depends(get_db)
):
    return delete_notification(db, notification_ids)
