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
from utils.discord import notify_background

def change_flags():
    GLOBAL["CURRENT_TICK"] += 1
    print("TICK {}".format(GLOBAL["CURRENT_TICK"]))
    
    notify_background("**Tick {} Started**".format(GLOBAL["CURRENT_TICK"]))
    
    with Session(engine) as session:
        for team in get_teams(session):
            for container in get_containers(session, team):
                while True:
                    flag = generate_flag()
                    print(flag)
                    try:
                        add_flag(session, container, flag, GLOBAL["CURRENT_TICK"])
                    except:
                        continue
                    break
                change_flag_async(team.host, team.host_token, container.chall.name, flag)
        session.commit()

def setup_ticks():
    change_flags()
    scheduler = BackgroundScheduler()
    scheduler.add_job(change_flags, CronTrigger(minute="*/5"))
    scheduler.start()
