# Library Management System


This is a simple Django project for managing a library of books. It allows you to categorize books into 'Art' and 
'Technology' shelves and perform basic CRUD operations (Create, Read, Update, Delete) on book entries.


## Table of Contents
1. Requirements
2. Installation
3. Usage


## Requirements
Before you begin, ensure you have met the following requirements:

1. Python 3.x installed.
2. Django framework installed (pip install Django).
3. Basic understanding of Django and web development.

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/hanan000/library-management.git

cd library
```
2. Create a virtual environment (recommended):
```bash
python -m venv venv
```
3. Activate the virtual environment:

On Windows:

```bash
venv\Scripts\activate
```
On macOS and Linux:

```bash
source venv/bin/activate
```

4. Install project dependencies:
```bash
pip install -r requirements.txt
```

5. Apply database migrations:
```bash
python manage.py migrate
```
6. Create a superuser account to access the Django admin panel:
```bash
python manage.py createsuperuser
```
7. Start the development server:
```bash
python manage.py runserver
```
## Usage

1. Access the admin panel by navigating to [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) and log in with the superuser credentials created earlier.

2. Add books by going to the "Books" section in the admin panel.

3. Access the main application at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

