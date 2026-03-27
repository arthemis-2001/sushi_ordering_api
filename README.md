# Sushi Ordering API 🍣

A production-ready backend API for managing sushi orders, built with Django and Django REST Framework.

## Table of Contents

- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Features](#features)
- [Getting Started](#getting-started)
- [API Documentation](#api-documentation)
- [Testing](#testing)
- [CI/CD](#cicd)
- [License](#license)


## Overview
This API allows customers to order sushi online. It provides endpoints for managing customers, sushi items, and orders. It uses JWT authentication for secure access. The API documentation is available via Swagger/OpenAPI at `/api/docs/`.

## Tech Stack

- **Backend:** Python, Django, Django REST Framework  
- **Authentication:** JWT  
- **API Docs:** DRF Spectacular (Swagger/OpenAPI)  
- **Database:** SQLite (PostgreSQL for production)  
- **CI/CD:** GitHub Actions  
- **Dependency Management:** UV  

## Features

- ✅ User registration and JWT authentication  
- ✅ CRUD endpoints for orders and sushi items  
- ✅ Swagger UI documentation for all endpoints  
- ✅ GitHub Actions for automated testing  
- ✅ Environment-based configuration

## Getting Started

### Prerequisites
- Python 3.12+
- UV (for dependency management)

### Installation
1. Clone the repository
2. Install dependencies: `uv sync`
3. Run migrations: `python manage.py migrate`
4. Start the development server: `python manage.py runserver`

Your API will be available at `http://127.0.0.1:8000/`

## API Documentation

The API documentation is available at `/api/docs/` when the development server is running.

## Testing
Run tests with: `python manage.py test`

GitHub Actions automatically runs tests on every push to the repository.

## CI/CD

GitHub Actions automatically runs tests on every push to the repository.

## License

This project is licensed under the MIT License.
