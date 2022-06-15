from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session

from utils.languages.models import *
from utils.languages.schemas import *


def add_language(db: Session, language: LanguageCreate):
    language_create = SystemLanguage(name=language.name, code=language.code)
    db.add(language_create)
    db.commit()
    db.refresh(language_create)
    return language_create


def get_language_by_name_or_code(db: Session, name: str, code: str):
    return (
        db.query(SystemLanguage)
        .filter(Language.name == name or Language.code == code)
        .first()
    )


def update_language(db: Session, update_details, language_id):
    try:
        get_language = db.query(SystemLanguage).get(language_id)
        get_language.name = update_details.name
        get_language.code = update_details.code
        db.add(get_language)
        db.commit()
        return get_language
    except:
        raise HTTPException(
            status_code=400, detail="Language changes has been failed try again"
        )


def get_languages(db: Session):
    return db.query(SystemLanguage).all()


def delete_language(db: Session, language_id):
    get_language = (
        db.query(SystemLanguage).filter(SystemLanguage.id == language_id).first()
    )
    language_name = get_language.name
    if not get_language:
        raise HTTPException(
            status_code=404, detail="Sorry that Language already deleted"
        )
    delete_language = db.delete(get_language)
    db.commit()
    return {
        "status": 200,
        "message": language_name + " language has been successful deleted",
    }
