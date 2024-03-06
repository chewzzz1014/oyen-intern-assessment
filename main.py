from fastapi import FastAPI, Depends, HTTPException, Cookie
from fastapi.responses import FileResponse, RedirectResponse, Response
from fastapi.staticfiles import StaticFiles
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# db
from sqlalchemy.orm import Session
from utils import get_db
from db.crud import create_user, get_user_by_username
from db.models import User
from db.schemas import UserCreateSchema, UserSchema
from db.database import engine, Base
# auth
from auth.models import Token
from datetime import timedelta
from auth.token import ACCESS_TOKEN_EXPIRE_MINUTES
from auth.auth import get_current_active_user
from auth.token import get_hashed_password, verify_password, create_access_token


app = FastAPI()
app.mount("/static", StaticFiles(directory="static", html=True), name="static")

# create db
Base.metadata.create_all(bind=engine)


@app.get("/")
async def root_get(session : Annotated[str | None, Cookie()]=None):
    if session is None:
        return RedirectResponse('/login')
    return FileResponse("static/home.html")

@app.get("/login")
async def login_get(session : Annotated[str | None, Cookie()]=None):
    if session is not None:
        return RedirectResponse('/')
    return FileResponse("static/login.html")


@app.post("/login")
async def login_post(user: UserCreateSchema, db: Session = Depends(get_db)):
    print(user)
    found_user = get_user_by_username(db, username=user.username)
    if not found_user:
        raise HTTPException(status_code=404, detail="Account Not Exist")
    if not verify_password(user.password, found_user.password):
        raise HTTPException(status_code=400, detail="Incorrect Username or Password")
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    content = {"access_token": access_token, "token_type": "bearer"}
    response = Response(content=content)
    response.set_cookie(key="session", value='bearer ' + access_token, samesite='lax')
    return response


@app.get("/register")
async def register_get(session : Annotated[str | None, Cookie()]=None):
    if session is not None:
        return RedirectResponse('/')
    return FileResponse("static/register.html")

@app.post("/register", response_model=UserSchema)
async def register_post(user: UserCreateSchema, db: Session = Depends(get_db)):
    found_user = get_user_by_username(db, username=user.username)
    if found_user:
        raise HTTPException(status_code=400, detail="Account Already Registered")
    create_user(db=db, user=user, hashed_password=get_hashed_password(user.password))
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    content = {"access_token": access_token, "token_type": "bearer"}
    response = Response(content=content)
    response.set_cookie(key="session", value='bearer ' + access_token, samesite='lax')
    return response

@app.get("/{any_path:path}")
async def root_get(any_path: str, session : Annotated[str | None, Cookie()]=None):
    if session is None:
        return RedirectResponse('/login')
    return any_path

# TODO: for all endpoints, display username, current path and logout btn