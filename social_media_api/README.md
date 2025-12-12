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
- profile_picture: Image field for profile picture
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
    "profile_picture": null
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

## Posts and Comments API

### Posts

- **GET /api/posts/**: List all posts (paginated, filterable by author, searchable by title/content)
- **POST /api/posts/**: Create a new post (authenticated users only)
- **GET /api/posts/{id}/**: Retrieve a specific post
- **PUT /api/posts/{id}/**: Update a post (owner only)
- **DELETE /api/posts/{id}/**: Delete a post (owner only)

### Comments

- **GET /api/comments/**: List all comments (paginated, filterable by post/author)
- **POST /api/comments/**: Create a new comment (authenticated users only)
- **GET /api/comments/{id}/**: Retrieve a specific comment
- **PUT /api/comments/{id}/**: Update a comment (owner only)
- **DELETE /api/comments/{id}/**: Delete a comment (owner only)

### Filtering and Pagination

- Pagination: Page-based with 10 items per page
- Post filters: ?author=username, ?search=keyword
- Comment filters: ?post=post_id, ?author=username

### Example Requests

Create a post:
```json
POST /api/posts/
Authorization: Token <token>
{
    "title": "My First Post",
    "content": "This is the content of my post."
}
```

Create a comment:
```json
POST /api/comments/
Authorization: Token <token>
{
    "post": 1,
    "content": "This is a comment on the post."
}
```