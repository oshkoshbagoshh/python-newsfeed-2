from flask import g
from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# import declarative_base from sqlalchemy.ext.declarative
from dotenv import load_dotenv

# from python_dotenv import load_dotenv
# from sqlalchemy.engine.url import URL
from sqlalchemy.engine.url import URL


load_dotenv()

# connect to database using env variable
db_url = getenv("DB_URL")
if db_url is None:
    raise ValueError("DB_URL environment variable is not set")
engine = create_engine(URL.create(db_url), echo=True, pool_size=20, max_overflow=0)
db_url = getenv("DB_URL")
if db_url is None:
    raise ValueError("DB_URL environment variable is not set")
engine = create_engine(URL.create(db_url), echo=True, pool_size=20, max_overflow=0)
# engine = create_engine(getenv("DB_URL"), echo=True, pool_size=20, max_overflow=0)
engine = create_engine(getenv(DB_URL), echo=True, pool_size=20, max_overflow=0)
Session = sessionmaker(bind=engine)
Base = sqlalchemy.orm.declarative_base()


def init_db():
    Base.metadata.create_all(engine)


def get_db():
    # return Session()
    if "db" not in g:
        # store db connection in g object
        g.db = Session()
    return g.db
