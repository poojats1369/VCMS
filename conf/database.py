from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os 
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

db_uri=os.environ.get('SQLALCHEMY_DATABASE_URI')

# SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:Valtech123@localhost/Users" 

engine = create_engine(db_uri)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()
