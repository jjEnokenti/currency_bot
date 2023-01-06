from sqlalchemy import create_engine
from config import Config
from sqlalchemy.ext.declarative import declarative_base

db = create_engine(f"postgresql+psycopg2://{Config.USER}:{Config.PASSWORD}@{Config.HOST}:5432/{Config.DB_NAME}")
base = declarative_base()
