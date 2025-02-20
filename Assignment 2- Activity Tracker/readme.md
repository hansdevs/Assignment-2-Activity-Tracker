# Assignment 2: Activity Tracker

Hans Gamlien

Spring 2025 CS-2610 Developing Dynamic, Database-Driven Web Application

## Description
This is a Django-based Activity Tracker that allows users to create activities and log time spent on them.  
The app provides an overview of all activities and calculates the total time spent on each.

---
## Installation & Setup

```
### 1. Create and activate a virtual environment

#### For zsh (macOS/Linux default shell)
```sh
python3 -m venv venv
source venv/bin/activate
```

#### For bash (Linux/macOS)
```sh
python3 -m venv venv
source venv/bin/activate
```

#### For Windows (cmd or PowerShell)
```sh
python -m venv venv
venv\Scripts\activate
```

### 2. Install dependencies
```sh
pip install -r ect...
```

### 3. Apply migrations
```sh
python3 manage.py migrate
```

### 4. Run the development server
```sh
python3 manage.py runserver
```

### 5. Open a browser and navigate to:
```sh
http://127.0.0.1:8000/
```

## Features
- ✅ Create new activities
- ✅ Log time for activities
- ✅ View total time spent on an activity
- ✅ Simple and intuitive interface

## Work Log
| Date           | Time Spent  | Events                                             |
|----------------|-------------|----------------------------------------------------|
| 02/13/2025     | ~2 hours    | Initial setup, watch tutorial, create stack        |
| 02/15/2025     | ~4 hours    | Fix Django setup, so many errors                   |
| 02/17/2025     | ~2 hours    | Test some CSS styling and update tracker folder    |
| 02/18/2025     | ~1.5 hours  | Initial final setup, revise manage.py              |
| 02/18/2025     | ~2.5 hours  | Fix bugs and final fancy stuff, clear pycache      |