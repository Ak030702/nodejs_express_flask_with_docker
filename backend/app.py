from flask import Flask, request
from flask_cors import CORS  # To allow frontend to access backend

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route('/submit', methods=['POST'])
def submit_form():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    print(f"Received: Name = {name}, Email = {email}")
    return {'message': 'Form submitted successfully'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
