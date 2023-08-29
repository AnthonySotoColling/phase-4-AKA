#!/usr/bin/env python3

# Standard library imports
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Game, Rating, Favorite, db
from app import app
from extensions import db, bcrypt


def seed_users():
    users = [
        {"username": "Alice", "password": "alice123"},
        {"username": "Bob", "password": "bob123"},
        {"username": "tonythetiger", "password": "theyregreat"},
        {"username": "admin", "password": "Banned123"}
    ]

    added_users = []

    for user_data in users:
        user = User.query.filter_by(username=user_data["username"]).first()
        if not user:
            user = User(username=user_data["username"])
            user.password = user_data["password"]
            db.session.add(user)
        added_users.append(user)

    db.session.commit()
    return tuple(added_users)

def seed_data():
    with app.app_context():
        db.create_all()
        user1, user2, tony, admin = seed_users() 

        games = [
            Game(name="Super Mario", genre="Platformer", image="mario.jpg"),
            Game(name="Legend of Zelda", genre="Adventure", image="zelda.jpg"),
            Game(name="skyrim", genre="rpg, singleplayer", image="https://cdn.cloudflare.steamstatic.com/steam/apps/489830/header.jpg?t=1650909796"),
            Game(name="diblo 4", genre="arpg, multiplayer", image="https://image.api.playstation.com/vulcan/ap/rnd/202212/0522/Dzry5RAwU9HsJGXZ3PUSYgCa.jpg"),
            Game(name="overwatch 2", genre="fps, multiplayer", image="https://news.xbox.com/en-us/wp-content/uploads/sites/2/2022/10/OW2-be9287b234afbe7898ac.jpg"),
            Game(name="path of exile", genre="arpg, multiplayer", image="https://image.api.playstation.com/cdn/UP4781/CUSA11924_00/jFpnaAjStsemwBPwNcmypKIYwupH8y7J.png"),
            Game(name="metro exodus", genre="fps, singleplayer", image="https://cdn.cloudflare.steamstatic.com/steam/apps/412020/capsule_616x353.jpg?t=1669390585"),
            Game(name="bioshock", genre="fps, singleplayer", image="https://upload.wikimedia.org/wikipedia/en/thumb/6/6d/BioShock_cover.jpg/220px-BioShock_cover.jpg"),
            Game(name="arkham city", genre="action, singleplayer", image="https://upload.wikimedia.org/wikipedia/en/0/00/Batman_Arkham_City_Game_Cover.jpg"),
            Game(name="rainbow six siege", genre="fps, multiplayer", image="https://cdn.cloudflare.steamstatic.com/steam/apps/359550/capsule_616x353.jpg?t=1692727022"),
            Game(name="grand theft auto", genre="open world, multiplayer", image="https://upload.wikimedia.org/wikipedia/en/a/a5/Grand_Theft_Auto_V.png"),
            Game(name="dead by daylight", genre="horror, multiplayer", image="https://cdn1.epicgames.com/offer/611482b8586142cda48a0786eb8a127c/EGS_DeadbyDaylight_BehaviourInteractive_S1_2560x1440-a32581cf9948a9a2e24b2ff15c1577c7"),
            Game(name="project zomboid", genre="survival, multiplayer", image="https://cdn.cloudflare.steamstatic.com/steam/apps/108600/capsule_616x353.jpg?t=1691508011"),
            Game(name="need for hot pursuit 2", genre="racing, singleplayer", image="https://upload.wikimedia.org/wikipedia/en/9/95/NFSHP2_PC.jpg"),
            Game(name="maplestory", genre="mmorpg", image="https://images.ctfassets.net/5p1u9t4r48s4/58ZM0MS9HOY2DaAN63IlA0/3c9d7c3dc39150dfb0c1e346fe069409/Dirt_Cover_Photo.png"),
            Game(name="elden ring", genre="rpg, singleplayer", image="https://image.api.playstation.com/vulcan/ap/rnd/202110/2000/aGhopp3MHppi7kooGE2Dtt8C.png"),
            Game(name="metal gear solid 3", genre="action, singleplayer", image="https://cdn.akamai.steamstatic.com/steam/apps/2131650/capsule_616x353.jpg?t=1688633867"),
            Game(name="lost ark", genre="arpg, mmorpg", image="https://images.ctfassets.net/umhrp0op95v1/VvjFjkl41oG52Nf71hZbr/e39168a3549882dd41f8b23187aa576c/LA_Y2_KA_Share_1200x630.jpg"),
        ]

        db.session.add_all(games)
        db.session.commit()
        

        ratings = [
            Rating(rating=5, user_id=user1.id, game_id=games[0].id),
            Rating(rating=4, user_id=user2.id, game_id=games[1].id),
            Rating(rating=5, user_id=tony.id, game_id=games[2].id),
            Rating(rating=3, user_id=admin.id, game_id=games[3].id)
        ]

        db.session.add_all(ratings)
        db.session.commit()

if __name__ == "__main__":
    print("Starting seed...")
    seed_data()
    print("Seeding completed!")

