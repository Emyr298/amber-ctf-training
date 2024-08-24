from sqlmodel import Session, select

from models import Chall

def get_challs(session: Session):
    return session.exec(select(Chall)).fetchall()
