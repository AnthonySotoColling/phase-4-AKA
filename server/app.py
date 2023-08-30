#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import Flask, request, jsonify, render_template, redirect, url_for
from extensions import db, bcrypt
from flask_jwt_extended import create_access_token, JWTManager
from flask_migrate import Migrate
from flask_cors import CORS



app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)
bcrypt.init_app(app)
jwt = JWTManager(app)
migrate = Migrate(app, db)
CORS(app)

from models import User, Game, Rating, Favorite


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        data = request.get_json()
        
        if not data:
            # Assume HTML form submission and get form data
            username = request.form['username']
            password = request.form['password']
        else:
            # API json submission
            username = data['username']
            password = data['password']

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            # User is authenticated
            access_token = create_access_token(identity=username)
            if data:
                return jsonify({"message": "Login successful!", "access_token": access_token}), 200
            else:
                # Redirect to the index route when user logs in from the form.
                return redirect(url_for('index'))
        else:
            if data:
                return jsonify({"message": "Invalid credentials!"}), 401
            else:
                # Show the error on the HTML login page.
                return render_template('login.html', error="Invalid credentials!")

    return render_template('login.html')


@app.route('/')
def index():
    return '<h1>Phase 4 Project Server</h1>'

@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = data['password']

    # Check if the user already exists
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({"message": "User already exists!"}), 400

    new_user = User(username=username, password=password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully!"}), 201


if __name__ == '__main__':
    app.run(port=5555, debug=True)

