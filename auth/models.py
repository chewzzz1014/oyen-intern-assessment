from pydantic import BaseModel
from db.schemas import UserCreateSchema

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None

class UserInDB(UserCreateSchema):
    hashed_password: str
