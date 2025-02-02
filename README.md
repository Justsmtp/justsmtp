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

## Setup Instructions

To set up this project locally, follow the steps below:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Justsmtp/justsmtp.git
   cd justsmtp

2. **Navigate to the project directory:**
   
cd justsmtp

4. **Set up a Virtual Environment:**

python3 -m venv venv

5. **Activate the Virtual Environment:**
Once the virtual environment is created, activate it:

    On Linux/MacOS:

source venv/bin/activate

On Windows:

    venv\Scripts\activate

After activation, you should see (venv) in your terminal prompt, indicating you’re working inside the virtual environment.

5. **Install the Required Dependencies:**
Next, install the required Python dependencies for the project. These are listed in the requirements.txt file:

pip install -r requirements.txt

This will install the necessary libraries, such as Flask and Flask-CORS, which are required to run the project.

6. **Run the App Locally:**
python app.py

If everything is set up correctly, you should see output similar to this:

 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit

 7. **Test the API:**

 http://127.0.0.1:5000
 
 8. **Deactivate the Virtual Environment (Optional):**
 Once you are done working on the project, deactivate the virtual environment by running:
 deactivate

 
 API Documentation

    Endpoint: GET /
    Request:
        No parameters required.
    Response:
        The API will return a JSON response in the following format:

    {
      "email": "smtpwtf@gmail.com",
      "current_datetime": "2025-01-30T09:30:00Z",
      "github_url": "https://github.com/Justsmtp/justsmtp.git"
    }

Deployment

This API is deployed at Render and can be accessed publicly:

    Deployed URL: 
    https://justsmtp.onrender.com

License

This project is licensed under the MIT License - see the LICENSE file for details.


### **Key Sections**:
1. **Description**: Brief overview of the project’s purpose.
2. **Technologies**: Lists the technologies used.
3. **Features**: Describes the available API endpoint and the data it returns.
4. **Setup Instructions**: Detailed steps to clone, set up the environment, install dependencies, and run the project locally.
5. **API Documentation**: Describes the API endpoint and its expected request/response.
6. **Deployment**: Includes the deployed URL and deployment platform.
7. **License**: Optional section for licensing details.

This complete `README.md` should now have all the information needed for someone to understand, set up, and run your project. Let me know if you need any further help!

