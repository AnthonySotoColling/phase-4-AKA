from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

# Models go here!


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    _password = db.Column(db.String)

    def __repr__(self):
        return f"<Username:{self.username}, Password:{self._password}"


class Game(db.Model):
    __tablename__ = "games"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    genre = db.Column(db.String)
    image = db.Column(db.String)

    def __repr__(self):
        return f"<Game Name:{self.name}, Genre:{self.genre}, Image:{self.image}"


class Rating(db.Model):
    __tablename__ = "ratings"

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    game_id = db.Column(db.Integer, db.ForeignKey("games.id"))

    def __repr__(self):
        return f"Rating:{self.rating}"


class Favorite(db.Model):
    __tablename__ = "favorites"
    id = db.Column(db.Interger, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    game_id = db.Column(db.Integer, db.ForeignKey("games.id"))
