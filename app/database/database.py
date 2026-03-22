import psycopg2
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

env_file = ".env.main"
load_dotenv(dotenv_path=env_file)

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL, echo=True)

print("Engine created successfully!")


