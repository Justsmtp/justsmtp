# Stage 0 Public API

## Description
This is a simple public API developed as part of the HNG12 Stage 0 Backend task. The API returns basic information such as the registered email, current date-time in ISO 8601 format, and the GitHub repository link for the project.

## Technologies
- **Python 3.x**
- **Flask** (Web framework)
- **Flask-CORS** (For handling Cross-Origin Resource Sharing)
- **Git** (Version control)
- **Render** (For deployment)

## Features
- **GET /**: Returns a JSON response with the following information:
  - Registered email address
  - Current date and time in ISO 8601 format (UTC)
  - GitHub repository link
