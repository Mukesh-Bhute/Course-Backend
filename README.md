# Courses and Instances Management System

This project implements a backend API using Django and Django REST framework for managing courses and their delivery instances. It also includes a frontend application using Angular to consume the API and provide a user-friendly interface for interacting with the system.

## Features

- **Courses Management:**
  - Create a new course
  - List all available courses
  - View detailed information about a specific course
  - Delete a course

- **Course Instances Management:**
  - Create a new instance of a course delivery
  - List courses delivered in a particular year and semester
  - View detailed information about a specific course instance
  - Delete a course instance

## API Endpoints

### Courses API

- **POST /api/courses**: Create a new course
- **GET /api/courses**: List all available courses
- **GET /api/courses/{id}**: View detailed information about a course with ID = `{id}`
- **DELETE /api/courses/{id}**: Delete a course with ID = `{id}`

### Course Instances API

- **POST /api/instances**: Create a new instance of a course delivery
- **GET /api/instances/{year}/{semester}**: List courses delivered in year = `{year}`, and semester = `{semester}`
- **GET /api/instances/{year}/{semester}/{id}**: View detailed information about an instance of a course with ID = `{id}`, delivered in year = `{year}`, and semester = `{semester}`
- **DELETE /api/instances/{year}/{semester}/{id}**: Delete an instance of a course with ID = `{id}`, delivered in year = `{year}`, and semester = `{semester}`

## Frontend User Interface

- **Create a course**
- **Create an instance of a course delivery**
- **List all courses**
- **View details of a particular course**
- **Delete a particular course**
- **List course delivery instances for a particular year and semester**
- **View details of a particular course instance**
- **Delete a particular course instance**

## Technologies Used

### Backend
- **Django**: Python web framework used to build the backend API.
- **Django REST Framework**: Toolkit for building Web APIs in Django.

### Frontend
- **Angular**: JavaScript framework used to build the frontend application.
- **Angular Material**: UI component library for Angular.

## Setup Instructions

### Backend

1. Clone the repository:
    ```bash
    git clone https://github.com/Mukesh-Bhute/Course-Backend
    cd Courses_backend
    ```

2. To run project:
    ```bash
    docker compose up
    ```

2. To stop project:
    ```bash
    docker compose down
    ```
