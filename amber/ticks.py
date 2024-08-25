from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from sqlmodel import Session
from database import engine

from repository.team import get_teams
from repository.containers import get_containers
from repository.flag import add_flag
from utils.flags import generate_flag
from config import GLOBAL

from utils.flags import change_flag_async
from utils.discord import notify, notify_background

def notify_challs():
    msg = "**🚩🚩🚩 CTF has started 🚩🚩🚩**\n\n"
    with Session(engine) as session:
        for team in get_teams(session):
            msg_team = f"**{team.name}**\n"
            cnt_container = 0
            for container in get_containers(session, team):
                cnt_container += 1
                msg_team += f"- {container.chall.name}: {container.team.host} {container.chall.port}\n"
            if cnt_container == 0:
                msg_team += "No Challs"
            msg_team += "\n\n"
            msg += msg_team
    notify(msg)

def change_flags():
    GLOBAL["CURRENT_TICK"] += 1
    notify_background("**⏰⏰ Tick {} ⏰⏰**".format(GLOBAL["CURRENT_TICK"]))
    with Session(engine) as session:
        for team in get_teams(session):
            for container in get_containers(session, team):
                while True:
                    flag = generate_flag()
                    try:
                        add_flag(session, container, flag, GLOBAL["CURRENT_TICK"])
                    except:
                        continue
                    break
                change_flag_async(team.host, team.host_token, container.chall.name, flag)
        session.commit()

def setup_ticks():
    notify_challs()
    change_flags()
    scheduler = BackgroundScheduler()
    scheduler.add_job(change_flags, CronTrigger(minute="*/5"))
    scheduler.start()
