from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Helper Functions
def is_prime(n):
    if n <= 1:
        return False
    return all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

def is_perfect(n):
    return n == sum(i for i in range(1, n) if n % i == 0)

def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    return n == sum(d ** len(digits) for d in digits)

def digit_sum(n):
    return sum(int(d) for d in str(n))

def get_fun_fact(n):
    try:
        response = requests.get(f"http://numbersapi.com/{n}?json")
        response.raise_for_status()
        return response.json().get('text', 'No fun fact available.')
    except requests.RequestException:
        return 'No fun fact available.'

# API Route
@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number = request.args.get('number')
    if not number or not number.lstrip('-').isdigit():
        return jsonify({"number": number, "error": True}), 400

    num = int(number)
    properties = []

    # Ensure "armstrong" comes first if applicable
    if is_armstrong(num):
        properties.append("armstrong")

    # Then add "even" or "odd"
    properties.append("even" if num % 2 == 0 else "odd")

    result = {
        "number": num,
        "is_prime": is_prime(num),
        "is_perfect": is_perfect(num),
        "properties": properties,
        "digit_sum": digit_sum(num),
        "fun_fact": get_fun_fact(num)
    }

    return jsonify(result), 200

# Run the Flask app
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)

