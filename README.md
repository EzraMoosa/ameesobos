# Amee & The Sobos - Django Full Stack Project

This project is a Django web application created for a fictional band "Amee & The Sobos". The application includes features such member profiles, songs and upcoming events. This guide will provide steps to build and run the app either in a Python virtual enviroment or with Docker.

## Prerequisites

### venv:
- Python 3.x
- `pip` package manager.
- Virtualenv (`python -m venv` or `python3 -m venv`)

### Docker:
- Docker (latest version recommended)

---

## Running the Application using `venv`

### 1. Clone Repository

* Use `git clone https://github.com/EzraMoosa/ameesobos.git`  
* Change into repository directory using `cd ameesobos`

### 2. Setting up virtual enviroment

Use `python -m venv .venv` or `python3 -m venv .venv` (You can replace '.venv' with a name of your own.)

Activate virtual enviroment

Use `source .venv/bin/activate` for (MacOS and Linux) or use `.venv\Scripts\activate` for (Windows)

### 3. Install dependencies

Use `pip install -r requirements.txt` or `pip3 install -r requirements.txt`

### 4. Set up database

Use `python manage.py migrate` or `python3 manage.py migrate`

### 5. Run development server

Use `python manage.py runserver` or `python3 manage.py runserver`

## Running the Application using Docker

### 1. Clone Repository

* Use `git clone https://github.com/EzraMoosa/ameesobos.git`  
* Change into repository directory using `cd ameesobos`

### 2. Build Docker image

`docker build -t django-app .` (You can replace 'django-app' with a name of your own)

### 3. Run Docker container

`docker run -d -p 8000:8000 django-app` (You must replace 'django-app' with the name you defined above)

### 4. Access the application in browser

Visit `http://localhost:8000` in your browser of choice.

## Credits

[Ezra Moosa](https://github.com/ezramoosa)
