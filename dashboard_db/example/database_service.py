from flask import Flask, jsonify, request, render_template
import mysql.connector
from mysql.connector import Error
from datetime import datetime

app = Flask(__name__)


def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Sai@Nadh123',
            database='message_db'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None


@app.route('/dashboard')
def dashboard():
    try:
        connection = create_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT COUNT(DISTINCT source), COUNT(DISTINCT message), COUNT(*) FROM message_db")
        summary_result = cursor.fetchone()

        cursor.execute("SELECT * FROM message_db")
        messages = cursor.fetchall()

        summary = {
            'Total Unique Sources': summary_result[0],
            'Total Unique Messages': summary_result[1],
            'Total Messages': summary_result[2]
        }

        detailed_report = [{
            'Sno': message[0],
            'Source': message[1],
            'Message': message[2],
            'Time': message[3].strftime('%Y-%m-%d %H:%M:%S')
        } for message in messages]

        return render_template('dashboard.html', summary=summary, detailed_report=detailed_report)

    except Error as e:
        print(f"Error: {e}")
        return jsonify({'error': 'Failed to fetch dashboard data'})

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


if __name__ == '__main__':
    app.run(host= "0.0.0.0",port= 5000, debug=True)
