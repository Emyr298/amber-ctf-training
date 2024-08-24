from sqlmodel import SQLModel, Session, create_engine
from models.team import Team

engine = create_engine("sqlite:///database.db")

def init_database():
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        session.add(Team(name="CyberPewPew"))
        session.add(Team(name="Bot"))
        session.commit()
