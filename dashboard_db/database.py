import mysql.connector
import json


def load_config():
    with open('config.json', 'r') as config_file:
        config_data = json.load(config_file)
    return config_data


def get_database_connection():
    config = load_config()
    return mysql.connector.connect(**config['DATABASE_CONFIG'])


def user_input(source, message):
    connection = get_database_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('INSERT INTO dashboard_table (source, message) VALUES (%s, %s)')