from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


SQLBase = declarative_base()
engine = create_engine('sqlite:///database.db', connect_args={'check_same_thread': False}, echo=True)
Session = sessionmaker(bind=engine)


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
