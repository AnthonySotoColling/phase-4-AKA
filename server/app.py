#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import Flask, request, jsonify
from extensions import db, bcrypt
from flask_jwt_extended import create_access_token, JWTManager
from flask_migrate import Migrate
from flask_cors import CORS



app = Flask(__name__)
app.config.from_object('config')
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000", "methods": ["GET", "POST", "PUT", "DELETE"]}})


db.init_app(app)
bcrypt.init_app(app)
jwt = JWTManager(app)
migrate = Migrate(app, db)



from models import User, Game, Rating, Favorite


@app.route('/api/login', methods=['POST'])
def api_login():
    data = request.get_json()

    if not data:
        return jsonify({"message": "Missing data!"}), 400

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"message": "Missing username or password!"}), 400

    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):
        access_token = create_access_token(identity=username)
        
        
        return jsonify({
            "message": "Login successful!",
            "access_token": access_token,
            "user_id": user.id   
        }), 200
    else:
        return jsonify({"message": "Invalid credentials!"}), 401



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

@app.route('/api/games', methods=['GET'])
def get_games():
    try:
        games = Game.query.all()
        return jsonify([game.to_dict() for game in games])
    except Exception as e:
        print(e)  
        return jsonify({"error": "An error occurred while fetching games"}), 500
    

@app.route('/api/favorites', methods=['POST'])
def add_favorite():
    data = request.get_json()

    user_id = data['user_id']  
    game_id = data['game_id']

    favorite = Favorite.query.filter_by(user_id=user_id, game_id=game_id).first()

    if favorite:  
        db.session.delete(favorite)
        db.session.commit()
        return jsonify({"message": "Removed from favorites!"}), 200
    else:  
        new_favorite = Favorite(user_id=user_id, game_id=game_id)
        db.session.add(new_favorite)
        db.session.commit()
        return jsonify({"message": "Added to favorites!"}), 201
    
@app.route('/api/ratings', methods=['POST'])
def add_rating():
    data = request.get_json()
    if not data:
        return jsonify({"message": "Missing data!"}), 400

    user_id = data.get('user_id')
    game_id = data.get('game_id')
    rating_value = data.get('rating')

    if not all([user_id, game_id, rating_value]):
        return jsonify({"message": "Missing user_id, game_id or rating!"}), 400

    existing_rating = Rating.query.filter_by(user_id=user_id, game_id=game_id).first()

    if existing_rating:
        existing_rating.rating = rating_value
        message = "Rating updated!"
    else:
        new_rating = Rating(user_id=user_id, game_id=game_id, rating=rating_value)
        db.session.add(new_rating)
        message = "Rating added!"
    try:
        db.session.commit()
        return jsonify({"message": message}), 201
    except Exception as e:
        print(e)
        return jsonify({"error": "An error occurred while saving the rating"}), 500
    
@app.route('/api/favorites/<int:user_id>', methods=['GET'])
def get_user_favorites(user_id):
    try:
        user = User.query.get(user_id)
        if not user:
            return jsonify({"error": "User not found"}), 404

        favorite_games = db.session.query(Game).join(Favorite, Game.id == Favorite.game_id).filter(Favorite.user_id == user_id).all()

        serialized_favorite_games = [game.to_dict() for game in favorite_games]

        return jsonify(serialized_favorite_games), 200
    except Exception as e:
        print(e)
        return jsonify({"error": "An error occurred while fetching favorites"}), 500
    
@app.route('/api/favorites/<int:user_id>/<int:game_id>', methods=['DELETE'])
def remove_favorite(user_id, game_id):
    try:
        favorite = Favorite.query.filter_by(user_id=user_id, game_id=game_id).first()

        if not favorite:
            return jsonify({"error": "Favorite not found"}), 404

        db.session.delete(favorite)
        db.session.commit()

        return jsonify({"message": "Favorite removed successfully"}), 200

    except Exception as e:
        print(e)
        return jsonify({"error": "An error occurred while removing the favorite"}), 500




if __name__ == '__main__':
    app.run(port=5555, debug=True)

