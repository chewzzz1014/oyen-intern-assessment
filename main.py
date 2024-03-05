from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from utils import get_current_user, fake_hash_password

# db
from sqlalchemy.orm import Session
from utils import get_db
from db.crud import create_user, get_user_by_username
from db.models import User
from db.schemas import UserCreateSchema, UserSchema
from db.database import engine, Base

app = FastAPI()
app.mount("/static", StaticFiles(directory="static", html=True), name="static")

Base.metadata.create_all(bind=engine)


@app.get("/")
async def root(current_user: Annotated[str, Depends(get_current_user)]):
    # TODO: check whether user is login, if yes to main page else to login
    print(current_user)
    return RedirectResponse("/login")

# TODO: resolve redirectresponse using get and change back this to GET
@app.get("/home")
async def home(current_user: Annotated[str, Depends(get_current_user)]):
    print('at home')
    return FileResponse("static/home.html")

@app.get("/login")
async def login_get():
    return FileResponse("static/login.html")

@app.post("/login", response_class=RedirectResponse)
async def login_post(user: UserCreateSchema, db: Session = Depends(get_db)):
    print(user)
    found_user = get_user_by_username(db, username=user.username)
    if not found_user:
        raise HTTPException(status_code=400, detail="Account Not Exist or Wrong Login Credential")
    return RedirectResponse("/home", 302)

@app.get("/register")
async def register_get():
    return FileResponse("static/register.html")

@app.post("/register", response_model=UserSchema)
async def register_post(user: UserCreateSchema, db: Session = Depends(get_db)):
    print(user)
    found_user = get_user_by_username(db, username=user.username)
    if found_user:
        raise HTTPException(status_code=400, detail="Account Already Registered")
    return create_user(db=db, user=user)