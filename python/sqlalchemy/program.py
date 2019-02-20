import sqlalchemy

import db.db_folder
from models.model_base import ModelBase
from models.member import Member


full_file = db.db_folder.get_db_file('data.bin')
conn_str = 'sqlite:///' + full_file

engine = sqlalchemy.create_engine(conn_str, echo=False)
ModelBase.metadata.create_all(engine)

session_factory = sqlalchemy.orm.sessionmaker(bind=engine)


def create(name='Kan'):
    m = Member(name=name)
    s = session_factory()
    s.add(m)
    s.commit()
    s.close()


def get(id=None):
    s = session_factory()
    m = s.query(Member).get(id)
    s.close()
    return m


def delete(id=None):
    s = session_factory()
    m = get(id)
    s.delete(m)
    s.commit()
    s.close()


if __name__ == '__main__':
    # create(name='mils')
    # m = get(2)
    # print(m.id, m.created, m.name)
    delete(2)
