from pydantic import BaseModel

# use this instead when create new user
class UserCreateSchema(BaseModel):
    username: str
    password: str

# use this when read data
class UserSchema(UserCreateSchema):
    id: int
    class Config:
        orm_mode = True