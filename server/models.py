# models.py
from sqlalchemy_serializer import SerializerMixin
from extensions import db, bcrypt
from sqlalchemy.orm import validates

# Models go here!


class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    _password = db.Column(db.String)

    def set_password(self, password):
        """Hash the provided password and store it."""
        self._password = bcrypt.generate_password_hash(
            password).decode('utf-8')

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

    # makes sure username is unique
    @validates('username')
    def validate_username(self, key, username):
        existing_user = User.query.filter(User.username == username).first()
        if existing_user is not None:
            raise ValueError("Username has been taken")
        return username

    def __repr__(self):
        return f"<Username:{self.username}, Password:{self._password}"


class Game(db.Model, SerializerMixin):
    __tablename__ = "games"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    genre = db.Column(db.String)
    image = db.Column(db.String)

    @property
    def average_rating(self):
        ratings = Rating.query.filter_by(game_id=self.id).all()
        if ratings:
            total_rating = sum([r.rating for r in ratings])
            return total_rating / len(ratings)
        return None

    serialize_only = ('id', 'name', 'genre', 'image', 'average_rating')

    def __repr__(self):
        return f"<Game Name:{self.name}, Genre:{self.genre}, Image:{self.image}"


class Rating(db.Model, SerializerMixin):
    __tablename__ = "ratings"

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    game_id = db.Column(db.Integer, db.ForeignKey("games.id"))

    serialize_only = ('id', 'rating', 'user_id', 'game_id')

    @validates
    def validates_rating(self, key, rating):
        if not (0 <= rating <= 5):
            raise ValueError("rating must be between 1-5")
        return rating

    @staticmethod
    def average_rating_for_game(game_id):
        ratings = Rating.query.filter_by(game_id=game_id).all()
        if ratings:
            total_rating = sum([r.rating for r in ratings])
            return total_rating / len(ratings)
        return None

    def __repr__(self):
        return f"Rating:{self.rating}"


class Favorite(db.Model):
    __tablename__ = "favorites"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    game_id = db.Column(db.Integer, db.ForeignKey("games.id"))
