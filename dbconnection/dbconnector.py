import psycopg2
import os

DB_HOST="127.0.0.1"
DB_NAME="MoneyButlerdb"
DB_USER="postgres"
DB_PASS="1234567890"

class DBConnector():

    @staticmethod
    def connect():
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            database=os.getenv("DB_NAME")
        )

        # conn = psycopg2.connect(
        #     host=DB_HOST,
        #     user=DB_USER,
        #     password=DB_PASS,
        #     database=DB_NAME
        # )
        return conn