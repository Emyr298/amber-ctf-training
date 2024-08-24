from sqlmodel import Session, select

from models import Team

def get_teams(session: Session):
    return session.exec(select(Team)).fetchall()

def get_team_by_id(session: Session, id: int):
    return session.exec(select(Team).where(Team.id == id)).first()
