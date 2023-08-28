# models.py
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from config import db, bcrypt

# Models go here!
class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    _password = db.Column(db.String)

    def set_password(self, password):
        """Hash the provided password and store it."""
        self._password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        """Check if the provided password matches the stored hashed password."""
        return bcrypt.check_password_hash(self._password, password)

    @property
    def password(self):
        """Prevent password from being accessed."""
        raise AttributeError("Password is not a readable attribute.")

    @password.setter
    def password(self, password):
        """Hash the provided password and store it."""
        self.set_password(password)


    def __repr__(self):
        return f"<Username:{self.username}, Password:{self._password}"


class Game(db.Model):
    __tablename__ = "games"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    genre = db.Column(db.String)
    picture = db.Column(db.String)
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

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    game_id = db.Column(db.Integer, db.ForeignKey("games.id"))
