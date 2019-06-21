import sqlalchemy

from models.model_base import ModelBase
from models.checklist import Checklist


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

# list
s = session()
checklists = s.query(Checklist).all()
for each in checklists:
    print(each.name)
