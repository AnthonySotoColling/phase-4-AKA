#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, Game, Rating, Favorite

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        
def seed_data():
    # Create sample users
    user1 = User(username="Alice", password="alice123")
    user2 = User(username="Bob", password="bob123")

    # Create sample games
    game1 = Game(name="Super Mario", genre="Platformer", picture="mario.jpg")
    game2 = Game(name="Legend of Zelda", genre="Adventure", picture="zelda.jpg")

    # Ratings
    rating1 = Rating(rating=5, user_id=user1.id, game_id=game1.id)
    rating2 = Rating(rating=4, user_id=user2.id, game_id=game2.id)

    # Favorites
    favorite1 = Favorite(user_id=user1.id, game_id=game2.id)

    # Add data to session
    db.session.add(user1)
    db.session.add(user2)
    db.session.add(game1)
    db.session.add(game2)
    db.session.add(rating1)
    db.session.add(rating2)
    db.session.add(favorite1)

    # Commit data to database
    db.session.commit()


if __name__ == "__main__":
    seed_data()
