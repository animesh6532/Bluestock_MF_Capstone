import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

PROJECT_ROOT = os.path.dirname(BASE_DIR)

DATABASE_DIR = os.path.join(PROJECT_ROOT, "database")

os.makedirs(DATABASE_DIR, exist_ok=True)

DB_PATH = os.path.join(DATABASE_DIR, "mutual_fund.db")

SCHEMA_PATH = os.path.join(DATABASE_DIR, "schema.sql")

conn = sqlite3.connect(DB_PATH)

with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
    conn.executescript(f.read())

conn.commit()
conn.close()

print("Database created successfully!")
print("Database location:", DB_PATH)