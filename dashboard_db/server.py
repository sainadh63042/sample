from flask import Flask, request, jsonify, render_template
import mysql.connector

app = Flask(__name__)

# Establish MySQL connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sai@Nadh123",
    database="message_db"
)
mycursor = mydb.cursor()


@app.route('/', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        source = request.form.get('source')
        message = request.form.get('message')

        sql = "INSERT INTO message_db (source, message) VALUES (%s, %s)"
        val = (source, message)
        mycursor.execute(sql, val)
        mydb.commit()

    summary_query = ("SELECT COUNT(DISTINCT source) AS total_unique_sources, COUNT(DISTINCT message) AS "
                     "total_unique_messages, COUNT(*) AS total_messages FROM message_db")
    mycursor.execute(summary_query)
    summary_result = mycursor.fetchone()

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

    return render_template('dashboard.html', summary=summary)


if __name__ == '__main__':
    app.run(debug=True)
