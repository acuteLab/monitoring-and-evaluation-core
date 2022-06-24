from datetime import date, datetime
from sqlalchemy.orm import Session
from authentication import models, schemas as user_schemas
from config.notifications.emails import send_email
from fastapi import Depends, HTTPException
from authentication.auth_token import (
    create_token_from_email,
    decode_access_token,
    get_id_from_token,
)
from config.database import get_tenant
import bcrypt

from starlette.requests import Request


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.email == username).first()


def check_username_password(db: Session, user: user_schemas.UserAuthenticate):
    db_user_info: models.UserInfo = get_user_by_username(db, username=user.email)
    return bcrypt.checkpw(
        user.password.encode("utf-8"), db_user_info.password.encode("utf-8")
    )


def get_users(db: Session):
    return db.query(models.User).all()


def create_user(db: Session, user: user_schemas.UserCreate):
    try:
        hash_password = bcrypt.hashpw(user.password.encode("utf-8"), bcrypt.gensalt())
        hashed_password = hash_password.decode("utf8")
        user = dict(user)
        user["password"] = hashed_password
        db_user = models.User(**user)
        db_user.created_on = datetime.now()
        db.add(db_user)
        db.commit()
        return {
            "status_code": 200,
            "message": "User account successfully created",
        }
    except:
        raise HTTPException(
            status_code=500, detail="Connection problems occured pls try again"
        )


def change_username(db: Session, username: str, user_id: int):
    try:
        user = db.query(models.User).filter(models.User.id == user_id).first()
        user.email = username
        db.add(user)
        db.commit()
        return {
            "status_code": 200,
            "message": "Your account username has successfully changed",
        }
    except:
        raise HTTPException(
            status_code=400, detail="Connection problems occurred pls try again"
        )


def request_reset_password(db: Session, email: str, background, request):

    get_user = db.query(models.User).filter(models.User.email == email).first()

    if not get_user:
        raise HTTPException(
            status_code=400,
            detail="Sorry your  email address is not registered on this system",
        )
    username = (
        db.query(models.User).filter(models.User.id == get_user.id).first().full_name
    )
    try:
        token = create_token_from_email(email)
        url = "https:/ismohamedi.dev" + "/reset-password/" + token
        to_email = email
        subject = "RESET PASSWORD"
        body = (
            """Hello """
            + username
            + ","
            + """
                <p />You can reset your password by clicking the bellow link" .
                <p /> click this link to reset your password <a href="{}">{}</a>
                """.format(
                url, url
            )
        )
        background.add_task(send_email, to_email, subject, body)
        return {
            "status_code": 200,
            "message": f"Reset password link has been sent to {email} email address",
        }

    except:
        raise HTTPException(
            status_code=400, detail="Connection problems occured pls try again"
        )


def reset_password(db: Session, password: str, token):
    token_data = decode_access_token(data=token)
    try:
        user = (
            db.query(models.User)
            .filter(models.User.email == token_data.get("email"))
            .first()
        )
        hash_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        hashed_password = hash_password.decode("utf8")
        user.password = hashed_password
        db.add(user)
        db.commit()
        return {
            "status_code": 200,
            "message": "Your Password successfully reseted, use your new password to login",
        }

    except:

        raise HTTPException(
            status_code=400, detail="Connection problems occured pls try again"
        )


def change_password(db: Session, password: str, user_id: int, background):

    try:
        user = db.query(models.User).filter(models.User.id == user_id).first()
        hash_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        hashed_password = hash_password.decode("utf8")
        user.password = hashed_password
        db.add(user)
        db.commit()
        username = (
            db.query(models.User).filter(models.User.id == user_id).first().full_name
        )
        to_email = user.email
        subject = "CHANGE PASSWORD"
        body = (
            """Hello """
            + username
            + ","
            + """
                <p />Your Account password has been changed" .
                <p /> if was not you please communicate with your Administrator
                """
        )
        background.add_task(send_email, to_email, subject, body)
        return {
            "status_code": 200,
            "message": "Your Password has been successfully changed",
        }

    except:
        raise HTTPException(
            status_code=400, detail="Connection problems occured pls try again"
        )


def deactivate_user(db: Session, user_id: int, background):

    try:
        user = db.query(models.User).filter(models.User.id == user_id).first()
        username = (
            db.query(models.Employee)
            .filter(models.Employee.user_id == user_id)
            .first()
            .full_name
        )
        user.is_active = False
        db.add(user)
        to_email = user.email
        subject = "ACCOUNT DEACTIVATION"
        body = (
            """Hello """
            + username
            + ","
            + """
                <p />Your account has been deactivated, you can not be able to login to the system.
                <p /> Communicate with your Adminstrator for more info
                """
        )

        background.add_task(send_email, to_email, subject, body)
        db.commit()
        return {
            "status_code": 200,
            "message": "Account of User "
            + username
            + "  has successfully deactivated/Suspended",
        }

    except:
        raise HTTPException(
            status_code=400, detail="Connection problems occured pls try again"
        )


def activate_user(db: Session, user_id: int, background):

    try:
        user = db.query(models.User).get(user_id)
        username = (
            db.query(models.Employee)
            .filter(models.Employee.user_id == user_id)
            .first()
            .full_name
        )
        deactivate_user = user.is_active = True
        url = get_tenant()
        db.add(user)
        to_email = user.email
        subject = "ACCOUNT ACTIVATION"
        body = (
            """Hello """
            + username
            + ","
            + """
                <p />Your account has been activated, now you are able to login to the system.
                <p /> Use this link to login:  <a href="{}">{}</a>
                """.format(
                url, url
            )
        )

        background.add_task(send_email, to_email, subject, body)
        db.commit()
        return {
            "status_code": 200,
            "message": "Account of User " + username + "  has successfully activated",
        }

    except:
        raise HTTPException(
            status_code=400, detail="Connection problems occured pls try again"
        )


def mark_account_as_verified_and_active(db_session: Session, token: str):
    """Mark an account as verified and active."""
    user_id = get_id_from_token(token)
    if not user_id:
        raise HTTPException(status_code=400, detail="Invalid token")
    user_obj = db_session.query(models.User).get(user_id)
    # Mark account as active.
    user_obj.is_active = True

    db_session.add(user_obj)
    db_session.commit()
    return {"status": "Account verified successfully"}


def delete_user(db: Session, user_id: int, background):

    try:
        user = db.query(models.User).get(user_id)
        username = (
            db.query(models.Employee)
            .filter(models.Employee.user_id == user_id)
            .first()
            .full_name
        )
        email = user.email
        delete_user = db.delete(user)
        to_email = email
        subject = "ACCOUNT DELETION"
        body = (
            """Hello """
            + username
            + ","
            + """
                <p />Your account has been deleted, you can not be able to login to the system." .
                <p /> Communicate with your Adminstrator for more info
                """
        )
        background.add_task(send_email, to_email, subject, body)
        db.commit()
        return {
            "status_code": 200,
            "message": "User " + username + " successfully removed from the system",
        }

    except:
        raise HTTPException(
            status_code=400, detail="Connection problems occured pls try again"
        )


def create_user_global(db, email: str, password: str):
    hash_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    hashed_password = hash_password.decode("utf8")
    db_user = models.User(email=email, password=hashed_password)
    db.add(db_user)
    db.flush()
    return db_user


def create_employee_global(
    db, first_name: str, middle_name: str, surname: str, user_id: int
):
    db_employee = models.Employee(
        user_id=user_id, first_name=first_name, middle_name=middle_name, surname=surname
    )
    db.add(db_employee)
    db.flush()
    return db_employee


def create_role(db: Session, role: user_schemas.RoleCreate):
    role = models.Role(name=role.name)
    db.add(role)
    db.commit()
    db.refresh(role)
    return role


def get_role_by_name(db: Session, name: str):
    return db.query(models.Role).filter(models.Role.name == name).first()


def roles(db: Session, skip: int = 0, limit: int = 100000):
    return db.query(models.Role).offset(skip).limit(limit).all()


def create_employee_role(db: Session, employee_id: int, role_id: int):
    employee_role = models.EmployeeRole(role_id=role_id, employee_id=employee_id)
    db.add(employee_role)
    db.flush()
    return employee_role


def edit_phone(db: Session, user: user_schemas, user_id):
    get_phone = db.query(models.User).filter(user.id == user_id).first()
    try:
        get_phone.phone_number = user.phone_number
        db.add(get_phone)
        db.commit()
        return {"status": 200, "message": "phone number  has been changed"}
    except:
        raise HTTPException(status_code=400, detail="Failed to update phone try again")
