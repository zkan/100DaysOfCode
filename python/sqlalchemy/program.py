import sqlalchemy

import db.db_folder
from models.model_base import ModelBase
from models.member import Member


full_file = db.db_folder.get_db_file('data.bin')
conn_str = 'sqlite:///' + full_file

engine = sqlalchemy.create_engine(conn_str, echo=False)
ModelBase.metadata.create_all(engine)

session_factory = sqlalchemy.orm.sessionmaker(bind=engine)
