import sqlite3
from sqlalchemy import create_engine


database_url = f"sqlite:///dev.db"

engine = create_engine(database_url, echo=True)

print("Engine created successfully!")
