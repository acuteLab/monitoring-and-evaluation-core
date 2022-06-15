from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from authentication.authenticate import get_db
from utils.languages import schemas
from utils.languages.operations import *

router = APIRouter()


@router.post("/language", response_model=Language)
def add_new_language(language: LanguageCreate, db_session: Session = Depends(get_db)):
    db_language = (
        db_session.query(SystemLanguage)
        .filter(
            SystemLanguage.name == language.name or SystemLanguage.code == language.code
        )
        .first()
    )
    if db_language:
        raise HTTPException(
            status_code=400, detail="Sorry Language name already exists"
        )
    return add_language(db_session, language)


@router.put("/edit-language/{language_id}", response_model=Language)
def update_lang(
    language_id: int, update_details: LanguageCreate, db: Session = Depends(get_db)
):
    return update_language(db, update_details, language_id)


@router.delete("/delete-language/{language_id}")
def delete_lang(language_id: int, db: Session = Depends(get_db)):
    return delete_language(db, language_id)


@router.get("/languages", response_model=List[Language])
async def languages(db: Session = Depends(get_db)):
    return get_languages(db)
