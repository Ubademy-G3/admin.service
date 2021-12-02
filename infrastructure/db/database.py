import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv


load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")


if DATABASE_URL is not None:
    engine = create_engine(DATABASE_URL)

    Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
else:
    engine = []
    Session = sessionmaker(autocommit=False, autoflush=False)

session = Session()

# Base class for models
Base = declarative_base()


def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
