import mysql.connector
from typing import Optional, Dict

def track_order_by_id(order_id: str) -> Optional[Dict]:
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password",
            database="your_db"
        )
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM orders WHERE order_id = %s"
        cursor.execute(query, (order_id,))
        result = cursor.fetchone()
        return result
    except mysql.connector.Error as err:
        print(f"MySQL Error: {err}")
        return None
