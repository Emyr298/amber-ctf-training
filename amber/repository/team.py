from sqlmodel import Session, select

from models import Team

def get_teams(session: Session):
    return session.exec(select(Team)).fetchall()
