from fastapi import Depends
import mysql.connector
from typing import Optional, Dict
from contextlib import contextmanager

global cnx
# Connecting with MySQL db
cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="sufyad26062002",
        database="pandeyji_eatery"
)

def save_order_to_db(order_items: dict) -> int:
    cursor = cnx.cursor()
    
    for gym_item, quantity in order_items.items():
        new_order_id = insert_order_item(gym_item, quantity) # order_id is auto-incremental
       
    insert_order_tracking(new_order_id, "in-progress") # add order tracking on backend
    
    cursor.close()
    
    return new_order_id


def get_total_order_price(order_id: int):
    cursor = cnx.cursor()
    # Executing the SQL query to get the total order price
    query = f"SELECT get_total_order_price({order_id})"
    cursor.execute(query)
    result = cursor.fetchone()[0]
    cursor.close()
    return result
    
# Function to call the MySQL stored procedure and insert an order item
def insert_order_item(gym_item, quantity):
    try:
        order_id = 0
        cursor = cnx.cursor()
        result_args = cursor.callproc('insert_order_item', (gym_item, quantity, order_id))
        cnx.commit()
        cursor.close()
        
        order_id = result_args[2] # result_args[2] contains the order id
        print(f"Order item inserted successfully! with order_id {order_id}")
        return order_id

    except mysql.connector.Error as err:
        print(f"Error inserting order item: {err}")
        cnx.rollback()
        return -1

    except Exception as e:
        print(f"An error occurred: {e}")
        # Rollback changes if necessary
        cnx.rollback()
        return -1

# Function to insert a record into the order_tracking table
def insert_order_tracking(order_id: int, status: str):
    cursor = cnx.cursor()

    # Inserting the record into the order_tracking table
    insert_query = "INSERT INTO order_tracking (order_id, status) VALUES (%s, %s)"
    cursor.execute(insert_query, (order_id, status))
    # Committing the changes
    cnx.commit()
    # Closing the cursor
    cursor.close()

def get_total_order_price(order_id):
    cursor = cnx.cursor()

    # Executing the SQL query to get the total order price
    query = f"SELECT get_total_order_price({order_id})"
    cursor.execute(query)

    # Fetching the result
    result = cursor.fetchone()[0]

    # Closing the cursor
    cursor.close()

    return result

# Function to fetch the order status from the order_tracking table
def get_order_status(order_id):
    cursor = cnx.cursor()
    query = f"SELECT status FROM order_tracking WHERE order_id = {order_id}"
    cursor.execute(query)
    result = cursor.fetchone()

    cursor.close()
    # Returning the order status
    if result:
        return result[0]
    else:
        return None


if __name__ == "__main__":
    # print(get_total_order_price(56))
    # insert_order_item('Samosa', 3, 99)
    # insert_order_item('Pav Bhaji', 1, 99)
    # insert_order_tracking(99, "in progress")
    print(get_next_order_id())
