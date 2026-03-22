
This is a REST API built with FASTAPI that provides authentication, user management and item management with role-based permission

Features:

JWT authentication

User registration and Login

Admin and user roles

item CRUD operations

Admin and user protection

item deletion monitoring or verification

Password hashing with bcrypt


Tech Stack:

FastAPI

SQLALCHEMY

JWT authentication


Endpoints:

POST/ user
Creates a user

GET/ user/{id}
fetches a user

POST/ item
created an item

GET/ item/{id}

fetches or basically searches for an item

DELETE/item
deleted an items of the user's choice
