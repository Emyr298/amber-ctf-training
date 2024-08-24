from typing import TYPE_CHECKING, Optional
from sqlmodel import SQLModel, Field, Relationship

class TeamFlagLink(SQLModel, table=True):
    team_id: int | None = Field(default=None, foreign_key="team.id", primary_key=True)
    flag_id: str = Field(foreign_key="flag.flag", primary_key=True)

class Chall(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    
    containers: list["Container"] = Relationship(back_populates="chall")

class Team(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    
    flags: list["Flag"] = Relationship(back_populates="teams", link_model=TeamFlagLink)
    containers: list["Container"] = Relationship(back_populates="team")

class Container(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    host: str
    port: int
    
    chall_id: int | None = Field(default=None, foreign_key="chall.id")
    chall: Chall = Relationship(back_populates="containers")
    team_id: int | None = Field(default=None, foreign_key="team.id")
    team: Team = Relationship(back_populates="containers")
    flags: list["Flag"] = Relationship(back_populates="container")

class Flag(SQLModel, table=True):
    flag: str = Field(primary_key=True)
    tick: int
    
    container_id: int | None = Field(default=None, foreign_key="container.id")
    container: Container = Relationship(back_populates="flags")
    teams: list["Team"] = Relationship(back_populates="flags", link_model=TeamFlagLink)
