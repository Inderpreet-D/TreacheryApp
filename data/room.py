import datetime

import sqlalchemy as sa

from data.modelbase import SqlAlchemyBase


class Room(SqlAlchemyBase):
    __tablename__ = 'rooms'

    code: str = sa.Column(sa.String, primary_key=True, unique=True)
    created_date: datetime.datetime = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)
    size: int = sa.Column(sa.Integer)
    cards: str = sa.Column(sa.String)
