from flask import g
from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from python-dotenv import load_dotenv
# from python-dotenv import load_dotenv
from dotenv import load_dotenv

# load env variables
load_dotenv()

# connect to database using env variable
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
Session = sessionmaker(bind=engine)
Base = declarative_base()


def init_db():
    Base.metadata.create_all(engine)
    
    
def get_db():
    # return Session()
    if 'db' not in g:
        # store db connection in g object
        g.db = Session()
    return g.db



