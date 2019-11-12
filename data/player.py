import datetime

import sqlalchemy as sa

from data.modelbase import SqlAlchemyBase


class Player(SqlAlchemyBase):
    __tablename__ = 'players'

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    created_date: datetime.datetime = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)
    room_code: str = sa.Column(sa.String, sa.ForeignKey('rooms.code'))
    card: str = sa.Column(sa.String)
