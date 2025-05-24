import pytest
import mysql.connector
from db_conn import get_db_cursor, get_db_conn


@pytest.fixture(scope="function")
def db_connection():
    """
    Establishes a fresh database connection for each test function
    and cleans up any test data.
    """
    conn = get_db_conn()
    cursor = conn.cursor()

    yield conn, cursor

    cursor.close()
    conn.close()

# Fixture to provide a clean database connection for each test
def test_insert_order(db_connection):
    """
    Tests inserting a new order into the database.
    """
    conn, cursor = db_connection
    # order_id = 1203 # default increment
    order_id = 12312
    item_id  = 123
    quantity = 3
    total_price = 4000.00

    insert_query = """
    INSERT INTO orders (order_id, item_id, quantity, total_price)
    VALUES (%d, %d, %d, %f);
    """
    try:
        cursor.execute(insert_query, (item_id, quantity, total_price))
        conn.commit()
        
        cursor.execute("SELECT * FROM orders WHERE order_id = %d;", (order_id,))
        result = cursor.fetchone()

        assert result is not None
        assert result[0] == order_id
        assert result[1] == item_id
        assert result[2] == quantity
        assert abs(float(result[3]) - total_price) < 0.001 # total_price is the fourth column, careful with float comparison

    except mysql.connector.Error as err:
        pytest.fail(f"Database error during insert test: {err}")
        

