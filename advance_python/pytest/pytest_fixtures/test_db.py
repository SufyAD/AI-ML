"""
Using SQLite for simplicity in our testing framework. 
SQLite is a lightweight, serverless database that is easy to set up and use, making it ideal for testing purposes. 
By utilizing SQLite in our pytest fixtures, we can efficiently create and manage test databases without the overhead of a full database server. 
This allows for quick and reliable testing of database interactions within our application.
"""

import sqlite3
import pytest

@pytest.fixture(scope="module")
def db():
    print("setting up")
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    # inserting dummy data in the dummy for testing
    cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
    cursor.executemany("insert INTO users (name) VALUES (?)", [("Tuba",), ("Sufyan",)])
    conn.commit()
    
    yield conn
    conn.close()
    print("tearing down")    
    
def test_tubas_id(db):
    cursor = db.cursor()
    cursor.execute("SELECT id FROM users WHERE name=?", ("Tuba",))
    result = cursor.fetchone()
    assert result[0] == 1

    
def test_sufyan_exists(db):
    cursor = db.cursor()
    cursor.execute("select name from users WHERE name=?", ("Sufyan",))
    result = cursor.fetchone()
    assert result[0] == "Sufyan"

def test_count(db):
    cursor = db.cursor()    
    cursor.execute("select count(*) from users")
    result = cursor.fetchone()
    assert result[0] == 2