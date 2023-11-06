from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from decouple import config
import psycopg2

from dotenv import load_dotenv

load_dotenv()

meta = MetaData()

DATABASE_URL = config("DATABASE_URI")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
conn = psycopg2.connect(DATABASE_URL)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()
