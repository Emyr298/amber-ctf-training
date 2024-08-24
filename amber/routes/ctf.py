from flask import Blueprint, request
from sqlmodel import Session
from database import engine

from repository.flag import pwn_flags
from repository.team import get_team_by_id
from utils.flags import notify_pwns
from dto.ctf import PostFlags

ctf_bp = Blueprint("ctf", __name__)

@ctf_bp.route("/post-flags", methods=["POST"])
def post_flags():
    try:
        body = PostFlags(**request.json)
    except:
        return { "error": "invalid body" }, 400
    
    with Session(engine) as session:
        team = get_team_by_id(session, 1)
        if not team:
            raise Exception("team not found")
        accepted_flags = pwn_flags(session, team, body.flags)
        if len(accepted_flags) > 0:
            notify_pwns(session, team, accepted_flags)
        session.commit()
    
    return { "accepted": accepted_flags }
