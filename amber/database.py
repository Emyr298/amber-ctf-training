import os
from sqlmodel import SQLModel, Session, create_engine
from models import Team, Chall, Container

engine = create_engine("sqlite:///database.db")

def init_database():
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)
    try:
        with Session(engine) as session:
            player_team = Team(id=1, name="CyberPewPew", host="", host_token="")
            bot_team = Team(id=2, name="Bot", host=os.getenv("TEAM_BOT_HOST"), host_token=os.getenv("TEAM_BOT_AUTHORIZATION"))
            
            chall_xl = Chall(name="xl", port=11000)
            chall_art = Chall(name="art", port=10000)
            chall_hirnfick = Chall(name="hirnfick", port=15000)
            
            session.add(player_team)
            session.add(bot_team)
            session.add(chall_xl)
            session.add(chall_art)
            session.add(chall_hirnfick)
            session.add(Container(chall=chall_xl, team=bot_team))
            session.add(Container(chall=chall_art, team=bot_team))
            session.add(Container(chall=chall_hirnfick, team=bot_team))
            session.commit()
    except:
        pass
