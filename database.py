import psycopg2 as psql
import os 
from dotenv import load_dotenv
load_dotenv()

class Database:
    @staticmethod
    def connect(query, query_type):
        database = psql.connect(
            database = os.getenv("DT_BASE"),
            host = os.getenv("DB_HOST"),
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASSWORD")
        )

        cursor = database.cursor()
        cursor.execute(query)
        if query_type == "insert":
            database.commit()
            return "inserted"
        if query_type == "select":
            return cursor.fetchall()

