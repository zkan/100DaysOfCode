import sqlalchemy

from models.model_base import ModelBase
from models.checklist import Checklist
from models.item import Item


conn_str = 'sqlite:///db.sqlite'

engine = sqlalchemy.create_engine(conn_str, echo=False)
session = sqlalchemy.orm.sessionmaker(bind=engine)

ModelBase.metadata.create_all(engine)

# create
s = session()
c = Checklist()
c.name = 'Hello'
s.add(c)
s.commit()

c = s.query(Checklist).filter(Checklist.name == 'Hello').first()
i = Item()
i.name = 'Item 1'
i.checklist_id = c.id
s.add(i)
s.commit()

# list
s = session()
checklists = s.query(Checklist).all()
for each in checklists:
    print(each.name)

items = s.query(Item).all()
for each in items:
    print(each.name, each.checklist, each.checklist_id)
