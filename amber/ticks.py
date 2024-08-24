from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from sqlmodel import Session

from database import engine

from repository.team import get_teams
from repository.containers import get_containers
from repository.flag import add_flag
from utils.flags import generate_flag

current_tick = 0

def change_flags():
    global current_tick
    
    current_tick += 1
    print("RENEWING FLAGS FOR TICK {}".format(current_tick))
    
    with Session(engine) as session:
        for team in get_teams(session):
            for container in get_containers(session, team):
                while True:
                    try:
                        add_flag(session, container, generate_flag())
                    except:
                        continue
                    break
                # TODO: change on docker containers

def setup_ticks():
    change_flags()
    scheduler = BackgroundScheduler()
    scheduler.add_job(change_flags, CronTrigger(minute="*/5"))
    scheduler.start()
