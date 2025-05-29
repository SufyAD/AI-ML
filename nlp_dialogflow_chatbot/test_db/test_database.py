import pytest
import mysql.connector
from db_conn import get_db_conn

# app.py

def insert_order_item(conn, gym_item, quantity) -> int:
    try:
        order_id = 0 # output
        cursor = conn.cursor()
        cursor.callproc('insert_order_item', (gym_item, quantity, order_id))
        conn.commit()
        cursor.close()
        
        return order_id 

    except Exception as e:
        print(f"Insert error: {e}")
        conn.rollback()
        return -1


def get_total_order_price(conn, order_id):
    try:
        cursor = conn.cursor()
        query = f"SELECT get_total_order_price({order_id})"
        cursor.execute(query)
        result = cursor.fetchone()[0]
        cursor.close()
        print("****************")
        return result
    except Exception as e:
        print(f"Total price error: {e}")
        return -1
 
    
        
@pytest.fixture
def db_connection():
    conn = get_db_conn()
    yield conn
    conn.close()

# def test_insert_order_item(db_connection):
#     conn = db_connection
#     gym_item = "bands"
#     quantity = 2
#     order_id = insert_order_item(conn, gym_item, quantity)
#     print(f"Order id is {order_id}")
#     assert order_id != -1
#     assert isinstance(order_id, int)

def test_get_total_order_price(db_connection):
    conn = db_connection
    test_items = [
        ("bands", 2),
        ("yoga mat", 3),
        ("shirt", 3),
        ("dumbell", 3),
        ("gym belt", 10),
        ("resistance bands", 100)]
    
    for item, qty in test_items:
        order_id  = insert_order_item(conn, item, qty)
        print(order_id)
        total_price = get_total_order_price(conn, order_id)
        
        assert order_id != -1
        assert isinstance(order_id, int)
        assert total_price > 0
