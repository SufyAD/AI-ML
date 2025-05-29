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
        # new_order = -1, if inser_order_item is failed
        new_order_id = insert_order_item(gym_item, quantity) # order_id is auto-incremental
    cursor.close()
    return new_order_id


def get_total_order_price(order_id: int):
    try:
        with cnx.cursor() as cursor:
            cursor.execute("SELECT get_total_order_price(%s)", (order_id,))
            cnx.commit() # debug fix
            order_id = cursor.fetchone()
            return order_id
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return -1
    
def insert_order_item(gym_item: str, quantity: int):
    try:
        with cnx.cursor() as cursor:
            cursor.execute("SET @p_order_id = 0")
            cursor.execute("CALL pandeyji_eatery.insert_order_item(%s, %s, @p_order_id)", (gym_item, quantity))
            cursor.execute("SELECT @p_order_id")
            
            order_id = cursor.fetchone()[0] # get order_id from the callproc            
            insert_order_tracking(order_id, "in-progress") # add tracking by-default
            cnx.commit()
            
            return order_id
        
    except mysql.connector.Error as err:
        print(f"MySQL Error: {err}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    
    cnx.rollback()
    return -1


# Function to insert a record into the order_tracking table
def insert_order_tracking(order_id: int, status: str):
    cursor = cnx.cursor()

    insert_query = "INSERT INTO order_tracking (order_id, status) VALUES (%s, %s)"
    cursor.execute(insert_query, (order_id, status))
    cnx.commit()
    cursor.close()

def get_total_order_price(order_id):
    cursor = cnx.cursor()

    # Executing the SQL query to get the total order price
    query = f"SELECT get_total_order_price({order_id})"
    cursor.execute(query)

    price = cursor.fetchone()[0]
    cursor.close()

    return price

# Function to fetch the order status from the order_tracking table
def get_order_status(order_id: int):
    try:
        with cnx.cursor() as cursor:
            query = "SELECT status FROM order_tracking WHERE order_id = %s"
            cursor.execute(query, (order_id,))
            result = cursor.fetchone()
            return result[0] if result else None
    except mysql.connector.Error as err:
        print(f"MySQL Error: {err}")
        return None



if __name__ == "__main__":
    # print(get_total_order_price(3475))
    # print(get_total_order_price(3474))
    # print(get_total_order_price(311))
    # print(get_total_order_price(3472))
    # print(get_total_order_price(1234))
    # insert_order_item('Pav Bhaji', 1, 99)
    #  print(get_next_order_id())insert_order_tracking(99, "in progress")
    print(get_order_status(123124))
    #
    pass