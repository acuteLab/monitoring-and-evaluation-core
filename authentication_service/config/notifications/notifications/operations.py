from fastapi import FastAPI, File, UploadFile, HTTPException
from utils.notifications import schemas
from utils.notifications.models import *
import os, shutil
from sqlalchemy.orm import Session


def create_message(db: Session, message_details: schemas.MessageCreate):
    try:
        message_data = message_details.dict()
        create_message = SystemMessage(**message_data)
        db.add(create_message)
        db.commit()
        return create_message

    except:
        raise HTTPException(status_code=400, detail="connection problem try again!!")


def create_notification(db: Session, notification_details: schemas.NotificationCreate):
    try:
        notification_data = notification_details.dict()
        create_notification = SystemNotification(**notification_data)
        db.add(create_notification)
        db.commit()
        return create_notification

    except:
        raise HTTPException(status_code=400, detail="connection problem try again!!")


def get_messages(db: Session):
    try:
        return db.query(SystemMessage).all()
    except:
        raise HTTPException(status_code=400, detail="connection problem try again!!")


def get_notifications(db: Session, user_id: int):
    try:
        return (
            db.query(SystemNotification)
            .filter(SystemNotification.receiver_id == user_id)
            .all()
        )
    except:
        raise HTTPException(status_code=400, detail="connection problem try again!!")


def delete_notification(db: Session, notification_ids: schemas.DeleteMessage):
    # try:
    for notification_id in notification_ids.ids:
        print(notification_id)
        notification = db.query(SystemNotification).get(notification_id)
        db.delete(notification)
    db.commit()
    return {"status_code": 200, "message": "Notification has been deleted"}


# except:
#     raise HTTPException(
#         status_code=400, detail="connection problem try again!!"
#     )
