from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

from dynaconf import settings

Base = declarative_base()
engine = create_engine(settings.POSTGRE_URL)

Session = sessionmaker(engine)


@contextmanager
def transaction_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()
