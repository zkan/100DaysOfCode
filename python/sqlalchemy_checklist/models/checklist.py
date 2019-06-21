import sqlalchemy

from .model_base import ModelBase


class Checklist(ModelBase):
    __tablename__ = 'checklists'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True,
                           autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String,
                             nullable=False)
