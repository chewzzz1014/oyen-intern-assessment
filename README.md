## Introduction
For Oyen's Software Engineering Intern Assessment, a simple login system with frontend and backend. User must register an account and login to access any path (including /). The JWT token is stored on cookie and is expired after 30 minutes. This project contains:


- Login Page
- Register Page
- Other Pages (Display current path and current login user's username)

![image](https://github.com/chewzzz1014/oyen-intern-assessment/assets/92832451/61d8cc7a-a4c5-43d8-9fad-6a4a463eaed9)
![image](https://github.com/chewzzz1014/oyen-intern-assessment/assets/92832451/a5d45543-4964-4867-8930-efc300ffe654)
![image](https://github.com/chewzzz1014/oyen-intern-assessment/assets/92832451/1fe02059-e9a8-4d7a-9b3b-34d0d8f25136)


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
2. (Optional) Create a virtual environment and active it by running `python -m venv venv` follows by `.\\venv\Scripts\activate` (on Windows's cmd) or `source venv/bin/activate` (Mac or Linux)
3. To install all packages, run `pip install -r requirements.txt`
4. To run the server, run `uvicorn main:app`
