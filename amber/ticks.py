from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from sqlmodel import Session
from database import engine

from repository.team import get_teams
from repository.containers import get_containers
from repository.flag import add_flag
from utils.flags import generate_flag
from config import GLOBAL

def change_flags():
    GLOBAL["CURRENT_TICK"] += 1
    print("RENEWING FLAGS FOR TICK {}".format(GLOBAL["CURRENT_TICK"]))
    
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
                # TODO: change on docker containers
        session.commit() # Commit before connecting to docker containers if possible.. or making connecting to docker container async or in other thread

def setup_ticks():
    change_flags()
    scheduler = BackgroundScheduler()
    scheduler.add_job(change_flags, CronTrigger(minute="*/5"))
    scheduler.start()
