from sqlalchemy import create_engine  # to open and use db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://tododb_kqp7_user:1vHQO5vxkhLDzpQfos6BwCBb8MAyNvt6@dpg-cq88rsqj1k6c73cgc790-a.frankfurt-postgres.render.com/tododb_kqp7"


# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:vice@localhost/TodoApplicationDatabase'  # used to create a location for the db in the fastapi app

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()