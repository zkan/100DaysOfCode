import datetime

import sqlalchemy

from .model_base import ModelBase


class Member(ModelBase):
    __tablename__ = 'members'

    id = sqlalchemy.Column(
        sqlalchemy.Integer,
        primary_key=True,
        autoincrement=-True
    )
    created = sqlalchemy.Column(
        sqlalchemy.DateTime,
        default=datetime.datetime.now
    )
    name = sqlalchemy.Column(
        sqlalchemy.String,
        nullable=False
    )
