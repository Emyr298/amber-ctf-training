from sqlmodel import Session, select, col

from models import Container, Flag, Team, TeamFlagLink
from config import GLOBAL

def add_flag(session: Session, container: Container, flag_content: str, tick: int):
    flag = Flag(flag=flag_content, container=container, tick=tick)
    session.add(flag)

def pwn_flags(session: Session, team: Team, posted_flags: list[str]):
    print(GLOBAL["CURRENT_TICK"])
    statement = select(Flag).join(
            Container, Flag.container_id == Container.id, isouter=True
        ).join(
            Team, Container.team_id == Team.id, isouter=True
        ).where(
            col(Flag.flag).in_(posted_flags)
        ).where(
            Flag.tick == GLOBAL["CURRENT_TICK"]
        ).where(
            Team.id != team.id
        ).where(
            col(Flag.flag).notin_(
                select(TeamFlagLink.flag_id).where(
                    TeamFlagLink.team_id == team.id
                )
            )
        )
    flags = session.exec(statement).fetchall()
    
    accepted = []
    for flag in flags:
        accepted.append(flag.flag)
        session.add(TeamFlagLink(team_id=team.id, flag_id=flag.flag))
    return accepted
