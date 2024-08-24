import os
from sqlmodel import Session
from database import engine

from models import Team
from repository.flag import get_flags_from_strings
from utils.discord import notify_background

def generate_flag():
    inner = os.urandom(32).hex()
    return "FLAG{" + inner + "}"

def notify_pwns(session: Session, team: Team, accepted_flags: list[str]):
    pwned = []
    flags = get_flags_from_strings(session, accepted_flags)
    for flag in flags:
        chall_name=flag.container.chall.name
        team_name=flag.container.team.name
        pwned.append(chall_name + " - " + team_name)
    notify_background("**{}** has pwned **{}**".format(team.name, ", ".join(pwned)))
