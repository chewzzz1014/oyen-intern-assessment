## Introduction

## TODO
1. Setup virtual env and install FastAPI
2. Create endpoints
3. Serve Static files
4. DB
5. Interaction w/ frontend, etc, session


## Setup
1. Create a Github repository and clone this empty repository in local environment, then cd into it
2. Create a virtual environment 
    `python -m venv venv`
3. Active the virtual environment (on cmd)
    `.\\venv\Scripts\activate`
4. Install FastAPI and all its related dependencies 
    `pip install fastapi[all]`
5. To export the list of installed packages into **requirements.txt**, run
    `pip freeze > requirements.txt`
6. Run `uvicorn main:app --reload` to run the project

## How to run
1. Clone this repository. Make sure that Python and virtual environment are installed on your desktop.
2. (Optional) Create a virtual environment and active it by running
    `python -m venv venv`
    `.\\venv\Scripts\activate`
3. To install all packages, run `pip install -r requirements.txt`
4. To run the server, run `uvicorn main:app --reload`