from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Hardcoded credentials for demo purposes
DEMO_USER = "admin"
DEMO_PASS = "password123"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    
    if not data:
        return jsonify({"message": "Invalid request payload"}), 400
        
    username = data.get('username')
    password = data.get('password')

    # Server-side validation check
    if not username or not password:
        return jsonify({"message": "Username and password cannot be empty"}), 400

    # Authentication matching logic
    if username == DEMO_USER and password == DEMO_PASS:
        # Correct credentials -> Returns status code 200
        return jsonify({"message": "Login Successful! Welcome back."}), 200
    else:
        # WRONG credentials -> Explicitly returns status code 401 (Unauthorized)
        return jsonify({"message": "Invalid username or password."}), 401

if __name__ == '__main__':
    app.run(debug=True)