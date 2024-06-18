# Fast Api Authentication and Authorization Project

## Description
This project is a FastAPI-based API that allows users to manage and interact with a collection of rants. It provides endpoints for creating new rants, retrieving all rants, and fetching a single rant by its ID. The project utilizes Pydantic for data validation and serialization.

## Features
- Create new rants with unique IDs
- Retrieve all existing rants
- Fetch a single rant by its ID
- Secure endpoints using PyJWT and Pydantic for data validation

## Setup Instructions
1. Clone the repository
2. Install the required dependencies using `pip install -r requirements.txt`
3. Run the project with `uvicorn main:app --reload`

## Project Structure
- **app/api.py**: Contains the FastAPI endpoints for rants management
- **app/model.py**: Defines the data models using Pydantic
- **app/auth/auth_handler.py**: Manages JWT token signing and decoding

## Dependencies
- FastAPI
- Pydantic
- PyJWT
- uvicorn
- decouple

## Known Issues
- None at the moment

## Contribution Guidelines
1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Make your changes and submit a pull request
