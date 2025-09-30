# Document Management System (DMS) - Flask Project

## Overview
This is a Flask-based Document Management System (DMS) that allows users to upload, manage, and download documents. It includes user authentication, version control, and file storage.

## Features
- User registration and login/logout using Flask-Login  
- Upload, download, update, and delete documents  
- Version control for uploaded documents  
- Secure form handling with CSRF protection (Flask-WTF)  
- Database management with Flask-SQLAlchemy + Flask-Migrate  
- Search and pagination for documents  
- JSON API endpoint for documents  
- Frontend templates with HTML & CSS  

## Folder Structure
DMS Project/
├── backend/ # Flask backend code
│ ├── app.py # Main Flask app
│ ├── uploads/ # Uploaded documents
│ ├── helpers/ # (extra utils if any)
│ ├── iterators/ # (practice code)
│ ├── members/ # (practice code)
│ ├── models/ # (practice code)
│ └── ...
├── frontend/ # Frontend templates & static files
│ ├── templates/ # HTML files
│ └── static/ # CSS, JS, images
├── database/ # SQLite database
├── migrations/ # Alembic migrations
├── practice/ # Python practice exercises
├── storage/ # Internal storage
├── venv/ # Virtual environment
├── requirements.txt # Python dependencies
└── README.md.txt # Project documentation

csharp
Copy code

## Installation
1. Clone the repository and navigate into the project folder.  
2. Create a virtual environment:  
   ```bash
   python -m venv venv
Activate virtual environment:

Windows: venv\Scripts\activate

Mac/Linux: source venv/bin/activate

Install dependencies:

bash
Copy code
pip install -r requirements.txt
Running the App
Run the Flask app with:

bash
Copy code
python backend/app.py
Then open your browser at:
👉 http://127.0.0.1:5000

Notes
Templates: frontend/templates/

Static files: frontend/static/

Uploaded documents: backend/uploads/

Database: database/app.db (managed by Flask-Migrate)

License
Open-source and free to use.