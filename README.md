# [WIP] En Salud Optima (ESO) - Server Side (Django version)

[This project is still a WIP]  
En Salud Optima (ESO) Server is a Django-based project that provides a RESTful API for fitness-related data. It includes models for exercises, muscles, equipment, workouts, and programs. The project uses PostgreSQL as its database and is configured to run in a Docker container.

## Project Structure

The project is divided into two main Django apps: `core` and `fitness`.

- `core`: Contains the User model and related authentication functionality.
- `fitness`: Contains models and views related to fitness data, such as Equipment, Muscle, Exercise, Workout, and Program.

The project's settings are divided into `common`, `dev`, and `prod` to facilitate different configurations for different environments.

## Getting Started

To get started with the project, clone the repository:

```
git clone https://github.com/angelmortiz/eso_server.git
cd eso-server
```

## Setup

1. Install the project dependencies listed in `requirements.txt` using pip:  
`pip install -r requirements.txt`

2. Set up the database using the provided Docker Compose file:  
`docker-compose up`


3. Run the Django server:  
`python manage.py runserver`


## API Endpoints

The API endpoints are defined in `fitness/urls.py` and include:

- `equipments`: CRUD operations for Equipment
- `muscles`: CRUD operations for Muscle
- `exercises`: CRUD operations for Exercise
- `exercises-detailed`: Retrieve detailed information for Exercise
- `workouts`: CRUD operations for Workout
- `workouts-routines`: Retrieve Workout with routines
- `programs`: CRUD operations for Program
- `programs-routines`: Retrieve Program with routines


## Logging

Logging is configured in `eso_server/settings/common.py`. The logs are outputted to the console and a file named `general.log`.