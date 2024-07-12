from sqlalchemy import create_engine  # to open and use db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./todosapp.db"


# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:vice@localhost/TodoApplicationDatabase'  # used to create a location for the db in the fastapi app

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()