from sqlmodel import Session

from models import Container, Flag

def add_flag(session: Session, container: Container, flag_content: str):
    flag = Flag(content=flag_content, container=container)
    session.add(flag)
