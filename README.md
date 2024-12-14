# CUSTOMER AND HEALTH_CENTER

## Description
This project appears to be a Python-based backend API for a health center system. It includes route handlers, database models, schemas, and testing components

## Installation
pip install -r requirements.txt

## Configuration
https://marcelo1234.pythonanywhere.com/ 
Environment variables needed:

DATABASE_URL = 'mysql+pymysql://root:root@localhost/health_center'
SECRET_KEY = os.getenv

## API Endpoints

| Endpoint       | Method | Description              |
|----------------|--------|--------------------------|
| /api/auth/login| POST   | AUTHENTICATION ROUTES    |
| /api/admin     | GET    | Protected Admin route    |
| /api/patients  | GET    | Check patients data      |
| /api/patients  | POST   | Add new health center
|/api/patients/<int:patient_id> |GET    | get specific id |
|/api/patients/<int:patient_id> |PUT    | update the table|
|/api/patients/<int:patient_id> |DELETE | delete the table|

## Testing
it test the get and delete of my petients table

## Git Commit Guidelines

Use conventional commits:
```bash
feat: add user authentication
fix: resolve database connection issue
docs: update API documentation
test: add user registration tests
