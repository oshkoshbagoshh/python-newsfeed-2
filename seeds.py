from app.models import User
from app.db import Session, Base, engine



# drop and rebuild all tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

