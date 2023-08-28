#!/usr/bin/env python3

# Standard library imports
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Remote library imports


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

from models import Game, User, Favorite, Rating

if __name__ == '__main__':
    engine = create_engine("")
    Session = sessionmaker(bind=engine)
    session = Session()

    skyrim = Game(name="skyrim", rating=4.7, genre="rpg, singleplayer",
                  image="https://cdn.cloudflare.steamstatic.com/steam/apps/489830/header.jpg?t=1650909796")
    diblo_4 = Game(name="diblo 4", rating=4, genre="arpg, multiplayer",
                   image="https://image.api.playstation.com/vulcan/ap/rnd/202212/0522/Dzry5RAwU9HsJGXZ3PUSYgCa.jpg")
    overwatch_2 = Game(name="overwatch 2", rating=1, genre="fps, multiplayer",
                       image="https://news.xbox.com/en-us/wp-content/uploads/sites/2/2022/10/OW2-be9287b234afbe7898ac.jpg")
    path_of_exile = Game(name="path of exile", rating=4.8, genre="arpg, multiplayer",
                         image="https://image.api.playstation.com/cdn/UP4781/CUSA11924_00/jFpnaAjStsemwBPwNcmypKIYwupH8y7J.png")
    metro_exodus = Game(name="metro exodus", rating=3.5, genre="fps, singleplayer",
                        image="https://cdn.cloudflare.steamstatic.com/steam/apps/412020/capsule_616x353.jpg?t=1669390585")
    bioshock = Game(name="bioshock", rating=4.5, genre="fps, singleplayer",
                    image="https://upload.wikimedia.org/wikipedia/en/thumb/6/6d/BioShock_cover.jpg/220px-BioShock_cover.jpg")
    arkham_city = Game(name="arkham city", rating=5, genre="action, singleplayer",
                       image="https://upload.wikimedia.org/wikipedia/en/0/00/Batman_Arkham_City_Game_Cover.jpg")
    rainbow_six_siege = Game(name="rainbow six siege", rating=2.3, genre="fps, multiplayer",
                             image="https://cdn.cloudflare.steamstatic.com/steam/apps/359550/capsule_616x353.jpg?t=1692727022")
    grand_theft_auto = Game(name="grand theft auto", rating=4.4, genre="open world, multiplayer",
                            image="https://upload.wikimedia.org/wikipedia/en/a/a5/Grand_Theft_Auto_V.png")
    dead_by_daylight = Game(name="dead by daylight", rating=4, genre="horror, multiplayer",
                            image="https://cdn1.epicgames.com/offer/611482b8586142cda48a0786eb8a127c/EGS_DeadbyDaylight_BehaviourInteractive_S1_2560x1440-a32581cf9948a9a2e24b2ff15c1577c7")
    project_zomboid = Game(name="project zomboid", rating=4.5, genre="survival, multiplayer",
                           image="https://cdn.cloudflare.steamstatic.com/steam/apps/108600/capsule_616x353.jpg?t=1691508011")
    need_for_hot_pursuit_2 = Game(name="need for hot pursuit 2", rating=5, genre="racing, singleplayer",
                                  image="https://upload.wikimedia.org/wikipedia/en/9/95/NFSHP2_PC.jpg")
    maplestory = Game(name="maplestory", rating=2.5, genre="mmorpg",
                      image="https://images.ctfassets.net/5p1u9t4r48s4/58ZM0MS9HOY2DaAN63IlA0/3c9d7c3dc39150dfb0c1e346fe069409/Dirt_Cover_Photo.png")
    elden_ring = Game(name="elden ring", rating=5, genre="rpg, singleplayer",
                      image="https://image.api.playstation.com/vulcan/ap/rnd/202110/2000/aGhopp3MHppi7kooGE2Dtt8C.png")
    metal_gear_solid_3 = Game(name="metal gear solid 3", rating=5, genre="action, singleplayer",
                              image="https://cdn.akamai.steamstatic.com/steam/apps/2131650/capsule_616x353.jpg?t=1688633867")
    lost_ark = Game(name="lost ark", rating=3, genre="arpg, mmorpg",
                    image="https://images.ctfassets.net/umhrp0op95v1/VvjFjkl41oG52Nf71hZbr/e39168a3549882dd41f8b23187aa576c/LA_Y2_KA_Share_1200x630.jpg")

    db.session.add_all(Game)
    db.session.commit()

    tony = User(username="tonythetiger", password="theyregreat")
    admin = User(username="admin", password="Banned123")

    db.session.add_all(User)
    db.session.commit()

