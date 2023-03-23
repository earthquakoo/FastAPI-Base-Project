from typing import Union

from email_validator import validate_email, EmailNotValidError
from pydantic import BaseModel, validator, Field

import src.auth.exceptions as exceptions
import src.auth.exceptions as auth_exceptions

class UserBase(BaseModel):
    email: str
    
    @validator('email')
    def email_must_be_valid(cls, v):
        try:
            validation = validate_email(v)
            email = validation.email
        except EmailNotValidError as e:
            raise auth_exceptions.EmailNotValidException()
        return email

class User(UserBase):
    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str = Field(default=..., min_length=4, max_length=30)
    

class UserCreateOut(UserBase):
    user_id: int
    
    class Config:
        orm_mode = True


class VerificationCode(BaseModel):
    email: str
    verification_code: str = Field(default=..., max_length=6)
    

class VerifyEmail(BaseModel):
    email: str
    
    @validator('email')
    def email_must_be_valid(cls, v):
        try:
            validation = validate_email(v)
            email = validation.email
        except EmailNotValidError as e:
            raise exceptions.EmailNotValidException()
        return email
    
    
class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None
    
    
class ResetPasswordIn(BaseModel):
    new_password: str