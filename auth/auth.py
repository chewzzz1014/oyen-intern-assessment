from db.schemas import UserCreateSchema
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from .token import JWT_SECRET_KEY, ALGORITHM
from jose import jwt, JWTError
from db.crud import get_user_by_username
from .models import TokenData
from sqlalchemy.orm import Session
from utils import get_db


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def fake_decode_token(token):
    return UserCreateSchema(
        username=token + "fakedecoded", password='testing123'
    )

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        print(payload)
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user_by_username(db, token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(
    current_user: Annotated[UserCreateSchema, Depends(get_current_user)]
):
    return current_user