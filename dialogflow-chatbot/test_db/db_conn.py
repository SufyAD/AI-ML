from fastapi import FastAPI
import mysql.connector
from contextlib import contextmanager



app = FastAPI(
    title="Testing API",
    description="This is a simple API"
)

def get_db_conn():
    # Connecting with MySQL db
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sufyad26062002",
            database="pandeyji_eatery"
        )
        print("Successful")
        return conn
    
    except mysql.connector.Error as err:
        print(f"Error connecting to database: {err}")
        return None

@contextmanager
def get_db_cursor():
    conn = None
    cursor = None
    try:
        conn = get_db_conn()
        cursor = conn.cursor()
        yield conn, cursor
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
            
            

        