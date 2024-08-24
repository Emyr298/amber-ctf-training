from sqlmodel import SQLModel, Session, create_engine
from models import Team

engine = create_engine("sqlite:///database.db")

def init_database():
    SQLModel.metadata.create_all(engine)
    try:
        with Session(engine) as session:
            session.add(Team(id=1, name="CyberPewPew"))
            session.add(Team(id=2, name="Bot"))
            session.commit()
    except:
        pass
