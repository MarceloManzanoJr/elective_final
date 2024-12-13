# CUSTOMER AND HEALTH_CENTER

## Description
Brief description of your system

## Installation
```cmd
pip install -r requirements.txt

## Configuration
Environment variables needed:

DATABASE_URL
SECRET_KEY

## API Endpoints

| Endpoint       | Method | Description              |
|----------------|--------|--------------------------|
| /api/auth/login| POST   | AUTHENTICATION ROUTES    |
| /api/admin     | GET    | Protected Admin route    |
| /api/patients  | GET    | Check patients data      |
| /api/patients  | POST   | Add new health center
|/api/patients/<int:patient_id> |GET    |
|/api/patients/<int:patient_id> |PUT    |
|/api/patients/<int:patient_id> |DELETE |

## Testing
 Instructions for running tests
…

## Git Commit Guidelines

Use conventional commits:
```bash
feat: add user authentication
fix: resolve database connection issue
docs: update API documentation
test: add user registration tests
