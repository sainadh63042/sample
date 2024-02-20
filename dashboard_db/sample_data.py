# # from flask import Flask, request, jsonify
# #
# # app = Flask(__name__)
# #
# # # Mock data for demonstration (replace with your actual data)
# # summary_data = {
# #     'Total Unique Sources': 10,
# #     'Total Unique Messages': 25,
# #     'Total Messages': 50
# # }
# #
# # detailed_report_data = [
# #     {'Sno': 1, 'Source': 'Source A', 'Message': 'Message 1', 'Time': '2023-11-07 10:30:00'},
# #     {'Sno': 2, 'Source': 'Source B', 'Message': 'Message 2', 'Time': '2023-11-07 10:35:00'},
# #     # Add more rows as needed
# # ]
# #
# # # Endpoint to retrieve summary
# # @app.route('/summary', methods=['GET'])
# # def get_summary():
# #     summary_text = "\nSummary\n"
# #     for key, value in summary_data.items():
# #         summary_text += f"{key} : {value}\n"
# #     return summary_text
# #
# # # Endpoint to retrieve detailed report
# # @app.route('/detailed_report', methods=['GET'])
# # def get_detailed_report():
# #     table = "<table border='1'>"
# #     table += "<tr><th>Sno</th><th>Source</th><th>Message</th><th>Time</th></tr>"
# #     for row in detailed_report_data:
# #         table += f"<tr><td>{row['Sno']}</td><td>{row['Source']}</td><td>{row['Message']}</td><td>{row['Time']}</td></tr>"
# #     table += "</table>"
# #     return table
# #
# # if __name__ == '__main__':
# #     app.run(debug=True)
# from flask import Flask, request, jsonify
# import mysql.connector
# from tabulate import tabulate  # Ensure you have the 'tabulate' library installed
#
# app = Flask(__name__)
#
# # Establish MySQL connection
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Sai@Nadh123",
#     database="message_db"
# )
# mycursor = mydb.cursor()
#
# # Ensure that the table 'message_db' exists in your database.
# # If not, create the table with necessary columns.
# # Example: mycursor.execute("CREATE TABLE IF NOT EXISTS message_db (id INT AUTO_INCREMENT PRIMARY KEY, source VARCHAR(255), message TEXT)")
#
# # Endpoint to receive and store messages
# @app.route('/messages', methods=['POST'])
# def store_message():
#     data = request.get_json()
#     source = data.get('source')
#     message = data.get('message')
#
#     # Insert the message into the database
#     sql = "INSERT INTO message_db (source, message) VALUES (%s, %s)"
#     val = (source, message)
#     mycursor.execute(sql, val)
#     mydb.commit()
#
#     return jsonify({'message': 'Message received and stored.'}), 201
#
# # Endpoint to retrieve detailed report of the table
# @app.route('/detailed_report', methods=['GET'])
# def get_detailed_report():
#     # Query to get all rows from the table
#     mycursor.execute("SELECT * FROM message_db")
#     columns = [desc[0] for desc in mycursor.description]
#     data = mycursor.fetchall()
#
#     detailed_report = []
#     for row in data:
#         detailed_report.append(dict(zip(columns, row)))
#
#     return tabulate(detailed_report, headers="keys", tablefmt="pipe")
#
# # Endpoint to retrieve summary
# @app.route('/summary', methods=['GET'])
# def get_summary():
#     # Query for summary information
#     summary_query = "SELECT COUNT(DISTINCT source) AS total_unique_sources, COUNT(DISTINCT message) AS total_unique_messages, COUNT(*) AS total_messages FROM message_db"
#     mycursor.execute(summary_query)
#     summary_result = mycursor.fetchone()
#
#     summary_text = f"Total Unique Sources: {summary_result[0]}\nTotal Unique Messages: {summary_result[1]}\nTotal Messages: {summary_result[2]}"
#     return summary_text
#
# if __name__ == '__main__':
#     app.run(debug=True)
# from flask import Flask, request, jsonify
# import mysql.connector
#
# app = Flask(__name__)
#
# # Establish MySQL connection
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Sai@Nadh123",
#     database="message_db"
# )
# mycursor = mydb.cursor()
#
# @app.route('/messages', methods=['POST'])
# def store_message():
#     data = request.get_json()
#     source = data.get('source')
#     message = data.get('message')
#
#     # Insert the message into the database
#     sql = "INSERT INTO message_db (source, message) VALUES (%s, %s)"
#     val = (source, message)
#     mycursor.execute(sql, val)
#     mydb.commit()
#
#     return jsonify({'message': 'Message received and stored.'}), 201
#
#
# @app.route('/detailed_report', methods=['GET'])
# def get_detailed_report():
#     mycursor.execute("SELECT * FROM message_db")
#     columns = [desc[0] for desc in mycursor.description]
#     data = mycursor.fetchall()
#
#     detailed_report = []
#     for row in data:
#         detailed_report.append(dict(zip(columns, row)))
#
#     return jsonify(detailed_report)
#
#
#
# @app.route('/summary', methods=['GET'])
# def get_summary():
#     # Query for summary information
#     summary_query = "SELECT COUNT(DISTINCT source) AS total_unique_sources, COUNT(DISTINCT message) AS total_unique_messages, COUNT(*) AS total_messages FROM message_db"
#     mycursor.execute(summary_query)
#     summary_result = mycursor.fetchone()
#
#     summary = {
#         'Total Unique Sources': summary_result[0],
#         'Total Unique Messages': summary_result[1],
#         'Total Messages': summary_result[2]
#     }
#     return jsonify(summary)
#
#
# if __name__ == '__main__':
#     app.run(host="117.99.203.27", debug=True)
from flask import Flask, request, jsonify, render_template
import mysql.connector

app = Flask(__name__)

# Establish MySQL connection
mydb = mysql.connector.connect(
    host="localhost",  # Replace with your actual host IP
    user="root",
    password="Sai@Nadh123",
    database="message_db"
)
mycursor = mydb.cursor()


# User Input Page
@app.route('/user', methods=['GET', 'POST'])
def user_input():
    if request.method == 'POST':
        source = request.form.get('source')
        message = request.form.get('message')

        # Insert the message into the database
        sql = "INSERT INTO message_db (source, message) VALUES (%s, %s)"
        val = (source, message)
        mycursor.execute(sql, val)
        mydb.commit()

    return render_template('user_input.html')


# Database Service Page
@app.route('/db_service', methods=['GET'])
def db_service():
    # Query for summary information
    summary_query = ("SELECT COUNT(DISTINCT source) AS total_unique_sources, COUNT(DISTINCT message) AS "
                     "total_unique_messages, COUNT(*) AS total_messages FROM message_db")
    mycursor.execute(summary_query)
    summary_result = mycursor.fetchone()

    # Query to get all rows from the table
    mycursor.execute("SELECT * FROM message_db")
    columns = [desc[0] for desc in mycursor.description]
    data = mycursor.fetchall()

    detailed_report = []
    for row in data:
        detailed_report.append(dict(zip(columns, row)))

    summary = {
        'Total Unique Sources': summary_result[0],
        'Total Unique Messages': summary_result[1],
        'Total Messages': summary_result[2],
        'Detailed Report': detailed_report
    }

    return render_template('db_service.html', summary=summary)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
