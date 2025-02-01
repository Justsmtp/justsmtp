from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app) 

@app.route('/', methods=['GET'])
def get_info():
    response = {
        "email": "smtpwtf@gmail.com",
        "current_datetime": datetime.utcnow().isoformat() + "Z",
        "github_url": "https://github.com/Justsmtp/justsmtp.git"
    } 
    return jsonify(response), 200

# This should be at the same indentation level as the route
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
