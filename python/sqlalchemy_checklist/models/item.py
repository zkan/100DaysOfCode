import sqlalchemy
from sqlalchemy import orm

from .model_base import ModelBase


class Item(ModelBase):
    __tablename__ = 'items'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True,
                           autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String,
                             nullable=False)
    checklist_id = sqlalchemy.Column(sqlalchemy.Integer,
                                     sqlalchemy.ForeignKey('checklists.id'),
                                     nullable=False)
    checklist = orm.relation('Checklist')
