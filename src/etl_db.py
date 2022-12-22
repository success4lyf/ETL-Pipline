import psycopg2
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Load environment variables from .env file
load_dotenv()
HOST = os.environ.get("postgres_host")
USER = os.environ.get("postgres_user")
PASSWORD = os.environ.get("postgres_pass")
DATABASE = os.environ.get("postgres_db")

DATABASE_TYPE = 'postgresql'
DBAPI = 'psycopg2'
PORT = 5433

conn = psycopg2.connect(
    host=HOST,
    user=USER,
    password=PASSWORD,
    database=DATABASE,
    port=PORT)

cursor = conn.cursor()

# DB_DATA = 'postgresql+psycopg2://' + USER + ':' + PASSWORD + '@' + HOST + ':5433/' + DATABASE + '?charset=utf8mb4'
engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")
engine.connect()
print('connected')