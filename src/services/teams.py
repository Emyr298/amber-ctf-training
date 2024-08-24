from sqlmodel import Session, select

from database import engine
from models.team import Team

def get_teams():
    with Session(engine) as session:
        statement = select(Team)
        teams = session.exec(statement).fetchall()
        print(teams)
