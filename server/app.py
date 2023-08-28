#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import Flask, request, jsonify
from flask_restful import Resource
from flask_sqlalchemy import SQLAlchemy  
from flask_bcrypt import Bcrypt          
from flask_jwt_extended import create_access_token
from flask_migrate import Migrate

# Create the Flask app and set the configuration:
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./gameranker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # recommended

# Now initialize the extensions:
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)

# Import models and possibly routes (after initializing the app and db to avoid circular imports):
from models import User, Game, Rating, Favorite


@app.route('/')
def index():
    return '<h1>Phase 4 Project Server</h1>'

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = data['password']

    # Check if the user already exists
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({"message": "User already exists!"}), 400

    new_user = User(username=username)
    new_user.password = password

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully!"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):
        # User is authenticated
        access_token = create_access_token(identity=username)
        return jsonify({"message": "Login successful!", "access_token": access_token}), 200
    else:
        return jsonify({"message": "Invalid credentials!"}), 401


if __name__ == '__main__':
    app.run(port=5555, debug=True)

