#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import Flask, request, jsonify
from flask_restful import Resource
from config import app, db, bcrypt
from models import User, Game, Rating, Favorite


# Add your model imports


# Views go here!

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
        # This is where you can generate and return a JWT token or set a session, etc.
        return jsonify({"message": "Login successful!"}), 200
    else:
        return jsonify({"message": "Invalid credentials!"}), 401


if __name__ == '__main__':
    app.run(port=5555, debug=True)

#testing my branch