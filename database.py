from sqlalchemy import create_engine  # to open and use db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://u_4771ebc8_433a_4d58_96f9_c0e210c43d80:2n6647V6bki5Cv63lVXjVEJQu5TsxDVjaP9R664X61kZ6A8g1q5U@pg.rapidapp.io:5433/db_4771ebc8_433a_4d58_96f9_c0e210c43d80?ssl=true&application_name=rapidapp_nodejs"


# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:vice@localhost/TodoApplicationDatabase'  # used to create a location for the db in the fastapi app

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()