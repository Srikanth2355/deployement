from flask import Flask, jsonify, request, session
import os
from dotenv import load_dotenv
from flask_migrate import Migrate
from extensions import db
from models import User
from werkzeug.security import generate_password_hash, check_password_hash
import re
from datetime import timedelta


load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=1)

migrate = Migrate(app, db)

db.init_app(app)

# Utility function to validate email
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email)

def setsession(user):
    session['user_id'] = user.id
    session['email'] = user.email
    session['name'] = user.name
    session['role'] = user.role
    return 


@app.route('/api/login', methods=['POST'])
def login():
    data = request.json 

    # Extract the fields
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify(ok='False', message='Email and password are required.'), 400

    # 2. Check if email exists in the database
    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({'ok': False, 'message': "Email Doesn't Exists.Please Register First"}), 401 
    
    # 3. Verify the password
    if not check_password_hash(user.password, password):
        return jsonify({'ok': False, 'message': 'Password is incorrect.'}), 401
    
    # 4. Create a session
    setsession(user)

    # 5. Prepare user dictionary to send to the frontend
    user_data = {
        'id': user.id,
        'name': user.name,
        'email': user.email,
        'role': user.role
    }

    return jsonify(ok=True, message='User logged in successfully.', user=user_data)


@app.route('/api/register', methods=['POST'])
def register():
    data = request.json

    # Extract the fields
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    confirm_password = data.get('confirmPassword')

    # 1. Check if all fields are provided
    if not all([name, email, password, confirm_password]):
        return jsonify({'ok': False, 'message': 'All fields are required.'}), 400

    # 2. Validate the email
    if not is_valid_email(email):
        return jsonify({'ok': False, 'message': 'Invalid email address.'}), 400

    # 3. Check if passwords match
    if password != confirm_password:
        return jsonify({'ok': False, 'message': 'Passwords do not match.'}), 400

    # 4. Check if email already exists in the database
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({'ok': False, 'message': 'Email already exists.'}), 400
    
    # 5. Hash the password
    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

    # 6. Save user to the database
    new_user = User(name=name, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify(ok=True,message="User have been created successfully")

@app.route('/api/logout', methods=['GET'])
def logout():
    # Check if a user is logged in
    session.clear()  # Clear all session data
    return jsonify(ok=True, message="Logout successful"), 200

@app.route('/api/is_logged_in', methods=['GET'])
def is_logged_in():
    # Check if user data exists in session
    if 'email' in session and 'user_id' in session:
        # Construct user data to send to the frontend
        user_data = {
            "id": session.get('user_id'),
            "email": session.get('email'),
            "role": session.get('role'),
            "name": session.get('name')  
        }
        return jsonify(ok=True, user=user_data), 200
    else:
        # User is not logged in
        return jsonify(ok=False, message="User not logged in"), 401
    

if __name__ == '__main__':
    app.run(debug=True,port=5000)