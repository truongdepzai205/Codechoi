from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

db_url = "sqlite:///database.db"

connect_args = {"check_same_thread": False}
engine = create_engine(db_url, connect_args=connect_args)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)
