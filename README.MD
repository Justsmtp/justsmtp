Number Classification API

A simple API that classifies numbers based on mathematical properties and provides a fun fact!
Features

    Check if a number is prime.
    Determine if a number is perfect.
    Identify Armstrong numbers.
    Return if the number is odd or even.
    Sum of digits.
    Fetch a fun fact from the Numbers API.

Technologies Used

    Python with Flask
    Render for deployment
    Numbers API for fun facts

Getting Started
Prerequisites

Make sure you have Python 3 installed.
Installation

Create a Virtural Environment 
python3 -m venv venv

Activate the Virtual Environment
source venv/bin/activate

    Clone the repository:

git clone git clone https://github.com/Justsmtp/justsmtp.git
cd justsmtp

Install dependencies:

pip install -r requirements.txt


Run the app:


    python app.py



API Usage
Endpoint:

GET /api/classify-number?number=<your-number>

Example:

GET /api/classify-number?number=371

Successful Response:

{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}

Error Response:

{
    "number": "abc",
    "error": true
}

Deployment on Render

    Go to Render.
    Click on New Web Service.
    Connect your GitHub repository.
    Fill in the deployment details:
        Environment: Python
        Build Command: pip install -r requirements.txt
    Click Deploy!

Your API will be available at https://<your-service-name>.onrender.com/api/classify-number?number=371.
License

This project is licensed under the MIT License.

5. Push Your Code to GitHub

    Initialize a Git repository:

git init

git add .

git commit -m "Initial commit for Number Classification API"

git remote add origin https://github.com/Justsmtp/justsmtp.git

git push -u origin master



Create a new repository on GitHub.

Push your code to GitHub:

git remote add origin git clone https://github.com/Justsmtp/justsmtp.git
git branch -M main
git push -u origin main
