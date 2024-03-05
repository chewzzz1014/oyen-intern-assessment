from db.database import SessionLocal
from db.schemas import UserCreateSchema
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def fake_decode_token(token):
    return UserCreateSchema(
        username=token + "fakedecoded", password='testing123'
    )

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    return user

def fake_hash_password(password: str):
    return "fakehashed" + password