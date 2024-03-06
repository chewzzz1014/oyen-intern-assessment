from passlib.context import CryptContext
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
from jose import jwt

load_dotenv()

# hashing
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_hashed_password(password):
    return password_context.hash(password)

def verify_password(password, hashed_str):
    return password_context.verify(password, hashed_str)

# generate JWT tokens
ACCESS_TOKEN_EXPIRE_MINUTES = 30
ALGORITHM = 'HS256'
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt