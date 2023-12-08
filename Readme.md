

# Task Manager API

This is a Django REST Framework (DRF) API for managing tasks.

## Features

- Allows CRUD operations for tasks
- Token-based authentication
- Permissions to ensure only owners can modify/delete tasks

## Setup

1. Clone the repository.
2. Install Python (if not already installed).
3. Install dependencies using pip:

   ```bash
   pip install -r requirements.txt
Run migrations:

bash
Copy code
python manage.py migrate
Create a superuser:

bash
Copy code
python manage.py createsuperuser
Start the development server:

bash
Copy code
python manage.py runserver
API Endpoints
/api/v1/tasks/

GET: List all tasks
POST: Create a new task
/api/v1/tasks/<task_id>/

GET: Retrieve a single task
PUT/PATCH: Update an existing task
DELETE: Delete a task
Authentication
Token-based authentication is used for API access. To obtain a token:

Send a POST request to /api/token/ with username and password.
Include the token in the Authorization header of subsequent requests: Authorization: Token <token>.
Permissions
Only authenticated users can perform CRUD operations.
Users can only modify/delete tasks they own.
Testing
To run unit tests:


