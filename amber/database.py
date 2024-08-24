from sqlmodel import SQLModel, Session, create_engine
from models import Team, Chall, Container

engine = create_engine("sqlite:///database.db")

def init_database():
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)
    try:
        with Session(engine) as session:
            player_team = Team(id=1, name="CyberPewPew")
            bot_team = Team(id=2, name="Bot")
            chall_1 = Chall(name="Test Chall")
            
            session.add(player_team)
            session.add(bot_team)
            session.add(chall_1)
            session.add(Container(host="test", port=8000, chall=chall_1, team=player_team))
            session.add(Container(host="test", port=8000, chall=chall_1, team=bot_team))
            session.commit()
    except:
        pass
