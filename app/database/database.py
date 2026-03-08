import psycopg2
from dotenv import dotenv_values
from sqlalchemy import create_engine

config = dict(dotenv_values(".env"))
DB_USER = config['DB_USER']
DB_PASSWORD = config['DB_PASS']
DB_HOST = config['DB_HOST']
DB_PORT = config['DB_PORT']
DB_NAME = config['DB_NAME']

database_url = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(database_url, echo=True)

print("Engine created successfully!")
