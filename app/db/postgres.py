from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

from dynaconf import settings

Base = declarative_base()
engine = create_engine(settings.POSTGRE_URL)

Session = sessionmaker(engine)


@contextmanager
def transaction_scope(session, close_at_exit=False):
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise
    finally:
        if close_at_exit:
            session.close()
