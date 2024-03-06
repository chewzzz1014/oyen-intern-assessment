from fastapi import FastAPI, Depends, HTTPException, Cookie
from fastapi.responses import FileResponse, RedirectResponse, Response, HTMLResponse
from fastapi.staticfiles import StaticFiles
from typing import Annotated
from utils import generate_template
# db
from sqlalchemy.orm import Session
from utils import get_db
from db.crud import create_user, get_user_by_username
from db.schemas import UserCreateSchema, UserSchema
from db.database import engine, Base
# auth
from datetime import timedelta
from auth.token import ACCESS_TOKEN_EXPIRE_MINUTES
from auth.token import get_hashed_password, verify_password, create_access_token
from auth.auth import get_current_user


app = FastAPI()
app.mount("/static", StaticFiles(directory="static", html=True), name="static")

# create db
Base.metadata.create_all(bind=engine)


@app.get("/", response_class=HTMLResponse)
async def root_get(login_session : Annotated[str | None, Cookie()]=None, db: Session = Depends(get_db)):
    if login_session is None:
        return RedirectResponse('/login')
    user = await get_current_user(login_session, db)
    return generate_template('static/home.html', {'user': user.username})

@app.get("/login")
async def login_get(login_session : Annotated[str | None, Cookie()]=None):
    if login_session is not None:
        return RedirectResponse('/')
    return FileResponse("static/login.html")


@app.post("/login")
async def login_post(user: UserCreateSchema, db: Session = Depends(get_db)):
    found_user = get_user_by_username(db, username=user.username)
    if not found_user:
        raise HTTPException(status_code=404, detail="Account Not Exist")
    if not verify_password(user.password, found_user.password):
        raise HTTPException(status_code=400, detail="Incorrect Username or Password")
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    response = Response()
    response.set_cookie(key="login_session", value=access_token, expires=ACCESS_TOKEN_EXPIRE_MINUTES*60, samesite='lax')
    return response


@app.get("/register")
async def register_get(login_session : Annotated[str | None, Cookie()]=None):
    if login_session is not None:
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
    response = Response()
    response.set_cookie(key="login_session", value=access_token, expires=ACCESS_TOKEN_EXPIRE_MINUTES*60, samesite='lax')
    return response


@app.get("/{any_path}", response_class=HTMLResponse)
async def handle_all_path(any_path: str, login_session : Annotated[str | None, Cookie()]=None, db: Session = Depends(get_db)):
    if login_session is None:
        return RedirectResponse('/login')
    user = await get_current_user(login_session, db)
    return generate_template('static/template.html', {'user': user.username, 'path': any_path})