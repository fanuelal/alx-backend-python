#!/usr/bin/python3
import mysql.connector
from mysql.connector import Error

def connect_to_prodev():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ALX_prodev"
        )
        if connection.is_connected():
            print("Connected to database")
        return connection
    except Error as e:
        print(f"Error connecting to database : {e}")
        raise
    
    
def stream_users():
    connection = None
    try:
        connection = connect_to_prodev()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM user_data")
        
        for row in cursor:
            yield row

    except Error as e:
        print(f"Error while streaming users: {e}")
    finally:
        if connection and connection.is_connected():
            connection.close()
            print("Connection closed.")