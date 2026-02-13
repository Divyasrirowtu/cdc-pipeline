import json
import mysql.connector

DB_CONFIG = {
    'host': 'mysql',
    'user': 'root',
    'password': 'root',
    'database': 'cdc_db'
}

def process_record(record):
    connection = mysql.connector.connect(**DB_CONFIG)
    cursor = connection.cursor()
    
    sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
    cursor.execute(sql, (record['name'], record['email']))
    
    connection.commit()
    cursor.close()
    connection.close()
    print(f"Inserted record: {record}")
