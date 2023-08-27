from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

# Models go here!


class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)


class Game(db.Model):
    __tablename__ = "games"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    genre = db.Column(db.String)
    pictrue = db.Column(db.String)


class Rating(db.Model):
    __tablename__ = "ratings"

    id = db.Column(db.Interger, primary_key=True)
    rating = db.Column(db.Interger)
    user_id = db.Column(db.Interger, db.ForeignKey("users.id"))
    game_id = db.Column(db.Interger, db.ForeignKey("games.id"))


class Favorite(db.Model):
    __tablename__ = "favorites"
    id = db.Column(db.Interger, primary_key=True)
    user_id = db.Column(db.Interger, db.ForeignKey("users.id"))
    game_id = db.Column(db.Interger, db.ForeignKey("games.id"))
