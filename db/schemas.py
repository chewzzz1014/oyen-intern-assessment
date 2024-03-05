from pydantic import BaseModel

# use this so that can inherit from this
class UserBase(BaseModel):
    username: str

# use this instead when create new user
class UserCreateSchema(UserBase):
    password: str

# use this when read data
class UserSchema(UserBase):
    id: int
    class Config:
        orm_mode = True