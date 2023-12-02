import re

from fastapi import HTTPException
from pydantic import BaseModel, validator

USERNAME_CHECK = re.compile(r"^[a-zA-Zа-яА-Я-]{1,50}$")
NAME_CHECK = re.compile(r"^[а-яА-Я-]{1,25}$")
PHONE_NUMBER_CHECK = re.compile(
    r"^\+?\d{1,4}\s?\-?\(?\d{1,3}\)?[\s.-]?\d{1,4}\s?\-?\d{1,4}\s?\-?\d{1,9}$")
PASSWORD_CHECK = re.compile(r"^(?=.*[a-zа-я])(?=.*[A-ZА-Я])(?=.*\d).{8,}$")


class UserRegister(BaseModel):
    username: str
    name: str
    phone_number: str
    password: str

    @validator("username")
    def validate_username(cls, value):
        if not USERNAME_CHECK.match(value):
            raise HTTPException(
                status_code=422,
                detail="Userame should contains only letters and\
                    be no longer than 50 characters."
            )
        return value

    @validator("name")
    def validate_name(cls, value):
        if not NAME_CHECK.match(value):
            raise HTTPException(
                status_code=422,
                detail="Name should contains only russian letters and\
be no longer than 25 characters."
            )
        return value

    @validator("phone_number")
    def validate_phone_number(cls, value):
        if not PHONE_NUMBER_CHECK.match(value):
            raise HTTPException(
                status_code=422,
                detail="Phone number should not contains letters."
            )
        return value

    @validator("password")
    def validate_password(cls, value):
        if not PASSWORD_CHECK.match(value):
            raise HTTPException(
                status_code=422,
                detail="Password must contains letters of both cases and\
digits and special symbol and be longer than 8 characters."
            )
        return value


class UserLogin(BaseModel):
    username: str
    password: str


class User(BaseModel):
    id: int
    username: str
    password: str
    name: str
    phone_number: str
    user_type: str
    user_image: str
