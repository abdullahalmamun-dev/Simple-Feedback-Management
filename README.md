# Simple-Feedback-Management

A Django REST API for managing user feedback with authentication and role-based access control.

## Overview

This project provides a basic framework for creating, reading, updating, and deleting (CRUD) feedback entries. It uses Django's built-in user model extended with a role field to differentiate between regular users and administrators. The API is secured with JWT authentication.

## Features

- **User Registration**: Users can register with a username, email, and password.
- **JWT Authentication**: Users can log in to receive a JWT token for accessing protected endpoints.
- **Feedback CRUD Operations**:
  - **Create**: Users can create new feedback entries.
  - **Read**: Users can view their own feedback. Admins can view all feedback.
  - **Update**: Users can update their own feedback. Admins can update any feedback.
  - **Delete**: Users can delete their own feedback. Admins can delete any feedback.
- **Role-Based Access Control**: Admins have elevated permissions to manage all feedback.

## Setup Instructions

### Prerequisites

- Python 3.8+
- PostgreSQL/MySQL/SQLite

### Installation Steps

1. **Clone the Repository**

2. **Create a Virtual Environment**

3. **Install Dependencies**

4. **Configure Database**
Update `DATABASES` settings in `feedback_system/settings.py`.

5. **Run Migrations**

6. **Create a Superuser**

7. **Run Development Server**

### API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/register/` | POST | Register a new user |
| `/api/login/` | POST | Login to receive JWT token |
| `/api/feedback/` | POST | Create new feedback (authenticated users) |
| `/api/feedback/` | GET | List all feedback (admins only) |
| `/api/feedback/{id}/` | GET | Retrieve a single feedback |
| `/api/feedback/{id}/` | PUT | Update feedback (creator or admin) |
| `/api/feedback/{id}/` | DELETE | Delete feedback (creator or admin) |

### API Usage Examples

1. **Get JWT Token**
curl -X POST http://localhost:8000/api/login/
-H "Content-Type: application/json"
-d '{"username": "admin", "password": "admin123"}'

2. **Create Feedback**
curl -X POST http://localhost:8000/api/feedback/
-H "Authorization: Bearer YOUR_TOKEN"
-H "Content-Type: application/json"
-d '{"title": "Bug Report", "description": "Critical error", "category": "bug"}'

## Testing

To run unit tests: python manage.py test feedback


## Contributing

Contributions are welcome! Please submit pull requests with detailed descriptions of changes.

## License

[MIT License](https://opensource.org/licenses/MIT)
