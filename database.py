from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from config import connection_string
from models import Base
engine = create_engine(connection_string, echo=True)

db_session =scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base.query = db_session.query_property()

def init_db():
    import models
    Base.metadata.create_all(bind=engine)