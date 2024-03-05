from fastapi import FastAPI, Depends
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from models.user import UserLoginForm

app = FastAPI()
app.mount("/static", StaticFiles(directory="static", html=True), name="static")

@app.get("/")
async def home():
    return RedirectResponse("/login")

@app.get("/login")
async def login_get():
    return FileResponse("static/login.html")

@app.post("/login")
async def login_post(login_form: UserLoginForm):
    print(login_form)
    return {"data": login_form}

@app.get("/error")
async def error():
    return {"message": "Error"}