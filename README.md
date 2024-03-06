## Introduction
For Oyen's Software Engineering Intern Assessment, a simple login system with frontend and backend. User must register an account and login to access any path (including /). The JWT token is stored on cookie and is expired after 30 minutes. This project contains:
- Login Page
- Register Page
- Other Pages (Display current path and current login user's username)


## Setup
1. Create a Github repository and clone this empty repository in local environment, then cd into it
2. Create a virtual environment 
    `python -m venv venv`
3. Active the virtual environment (on cmd)
    `.\\venv\Scripts\activate`
4. Install FastAPI and all its related dependencies 
    `pip install fastapi[all]`
5. Run `uvicorn main:app --reload` to run the project
6. To export the list of installed packages into **requirements.txt**, run
    `pip freeze > requirements.txt`

## How to run
1. Clone this repository. Make sure that Python and virtual environment are installed on your desktop.
2. (Optional) Create a virtual environment and active it by running
    `python -m venv venv`
    `.\\venv\Scripts\activate` (on Windows's cmd) or `source venv/bin/activate` (Mac or Linux)
3. To install all packages, run `pip install -r requirements.txt`
4. To run the server, run `uvicorn main:app`