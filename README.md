E-commerce API

This project is a RESTful API for an e-commerce platform. It provides endpoints for managing customers, products, and orders, as well as an authentication system with JWT. The application leverages Flask with various extensions for database interaction, caching, rate limiting, and authentication.

# Features

>>Customer Management: Create, read, update, and delete customer data.
>>Product Management: Create, read, update, and delete product data.
>>Order Management: Place orders associated with customers and products.
>>Authentication: Secure routes with JSON Web Token (JWT) authentication.
>>Rate Limiting: Limit the number of API calls per user.
>>Caching: Improve performance with response caching.
>>Admin Initialization: Automatically create a default admin user if none exists.

# Setup and Installation

Prerequisites
>>Python 3.8+
>>pip
>>PostgreSQL or an alternative database (configured in Config)

# Installation
Clone the repository:

>>git clone <repository_url>
>>cd e-commerce-api

# Create a virtual environment:

python3 -m venv venv
source venv/bin/activate

# Install dependencies:
>>pip install -r requirements.txt
>>Configure environment variables: Modify config.py with your >>database URL and JWT secret key.

# Initialize the Database:
>>flask db init
>>flask db migrate
>>flask db upgrade

# Run the application:
>>flask run
>>The application will run on http://localhost:5000.

API Endpoints

# Authentication
-POST /login: Authenticate and receive a JWT token.

# Customers
>>POST /customers: Create a new customer (requires JWT).
>>GET /customers/<id>: Retrieve a customer's details (requires JWT).
>>PUT /customers/<id>: Update a customer (requires JWT).
>>DELETE /customers/<id>: Delete a customer (requires JWT).

# Products
>>POST /products: Create a new product (requires JWT).
>>GET /products/<id>: Retrieve a product's details (requires JWT).
>>PUT /products/<id>: Update a product (requires JWT).
>>DELETE /products/<id>: Delete a product (requires JWT).

# Orders
>>POST /orders: Place an order (requires JWT).
>>GET /orders/<id>: Retrieve an order's details (requires JWT).

# Configuration
Configurations are stored in config.py, including:

-Database URI: Specifies the database location.
-JWT Secret Key: Secret for signing JWT tokens.
-Caching and Rate Limits: Settings for caching and API call limitations.

Testing

# Unit tests are written using unittest for endpoints. Run tests with:

python -m unittest discover -s tests

# Dependencies
Flask
Flask-RESTful
Flask-JWT-Extended
Flask-SQLAlchemy
Flask-Caching
Flask-Limiter
psycopg2 for PostgreSQL
Refer to requirements.txt for the full list of dependencies.