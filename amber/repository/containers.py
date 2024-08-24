from sqlmodel import Session, select

from models import Team, Container

def get_containers(session:Session, team: Team):
    return session.exec(
        select(Container).where(Container.team_id == team.id)
    ).fetchall()
