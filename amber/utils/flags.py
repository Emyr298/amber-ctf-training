import os, requests, threading
from sqlmodel import Session

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

def change_flag_in_hosts(host: str, token: str, challenge: str, new_flag: str):
    requests.post(
        f"http://{host}/flag",
        json={
            "challenge": challenge,
            "flag": new_flag,
        },
        headers={
            "Authorization": token,
        }
    )

def change_flag_async(host: str, token: str, challenge: str, new_flag: str):
    thread = threading.Thread(target=change_flag_in_hosts, args=(host, token, challenge, new_flag))
    thread.start()
