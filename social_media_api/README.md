# Social Media API

This is a Django REST API for a social media application with user authentication.

## Setup

1. Install dependencies:
   ```
   pip install django djangorestframework django-rest-framework-authtoken Pillow
   ```

2. Run migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

3. Start the server:
   ```
   python manage.py runserver
   ```

## User Model

The custom user model extends Django's AbstractUser with:
- bio: Text field for user biography
- profile_picture: CharField for profile picture URL
- followers: Many-to-many relationship for following other users

## Authentication

Uses Django REST Framework's token authentication.

### Register a new user

POST to `/api/register/`

Body:
```json
{
    "username": "testuser",
    "email": "test@example.com",
    "password": "password123",
    "bio": "Optional bio",
    "profile_picture": "http://example.com/pic.jpg"
}
```

Response:
```json
{
    "user": {...},
    "token": "token_key"
}
```

### Login

POST to `/api/login/`

Body:
```json
{
    "username": "testuser",
    "password": "password123"
}
```

Response:
```json
{
    "user": {...},
    "token": "token_key"
}
```

### Get/Update Profile

GET/PUT to `/api/profile/`

Requires authentication header: `Authorization: Token <token>`

## Testing

Use Postman or similar to test the endpoints.