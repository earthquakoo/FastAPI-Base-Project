from fastapi import Depends
from sqlalchemy.orm import Session 
from pydantic import EmailStr
from email_validator import validate_email, EmailNotValidError

import src.models as glob_models
import src.auth.exceptions as exceptions
import src.auth.utils as utils


def get_user_by_email(db: Session, email: EmailStr):
    user = db.query(glob_models.User).filter(glob_models.User.email == email).first()
    return user


def get_password_by_email(db: Session, email: EmailStr):
    user = db.query(glob_models.User).filter(glob_models.User.email == email).first()
    return user.password


def get_current_active_user(db: Session, email: EmailStr, is_activate: bool):
    return db.query(glob_models.User).filter(glob_models.User.email == email, glob_models.User.is_activate == is_activate).first()


def authenticate_user(db: Session, email: str, password: str):
    try:
        validation = validate_email(email)
        email = validation.email
    except EmailNotValidError as e:
        raise exceptions.EmailNotValidException()
    
    user = db.query(glob_models.User).filter(glob_models.User.email == email).first()
    if not user:
        return False
    if not utils.verify_password(password, user.password):
        return False
    return user