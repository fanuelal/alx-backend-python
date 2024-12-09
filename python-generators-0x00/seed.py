#!/usr/bin/python3
import mysql.connector as db
import uuid

def connect_db():
    try:
        db.connect(
            host="localhost",
            user="yourusername",
            password="yourpassword",
        )
        print("Connected to MySQL database successfully")
    except db.connector.Error as e:
        print("error has been occured: ${e}")
        raise

def connect_db():
    try:
        cnx = db.connect(user='root', password='', host='localhost', database='ALX_prodev')
        cursor = cnx.cursor()
        return cnx, cursor
    except db.Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None, None
    
def create_database(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        print("Database ALX_prodev ensured to exist.")
    except db.Error as e:
        print(f"Error creating database: {e}")
        raise
def connect_to_prodev():
    try:
        connection = db.connect(user='root', password='', host='localhost', database="ALX_prodev")
    except db.Error as e:
        print(f"Error connecting to database: {e}")
        return None
            
def create_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS user_data (
            user_id CHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL(3, 1) NOT NULL,
            INDEX (user_id)
        )''')
        print("Table users created successfully.")
    except db.Error as e:
        print(f"Error creating table: {e}")
        raise
def insert_data(connection, data):
    try:
        cursor = connection.cursor()
        insert_query = """
        INSERT INTO user_data (user_id, name, email, age)
        VALUES (%s, %s, %s, %s)
        """
        cursor.executemany(insert_query, data)
        connection.commit()
        print(f"Inserted {cursor.rowcount} rows into user_data.")
    except Error as e:
        print(f"Error inserting data: {e}")
        raise