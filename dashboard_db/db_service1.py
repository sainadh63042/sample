from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# MySQL connection configuration (change these values accordingly)
mysql_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Sai@Nadh123',
    'database': 'dashboard_db'
}

# Connect to MySQL database
conn = mysql.connector.connect(**mysql_config)
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS dashboard_table (
                    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
                    source VARCHAR(255) NOT NULL,
                    message TEXT NOT NULL,
                    timestamp DATETIME
                )''')
conn.commit()


@app.route('/dashboard', methods=['GET'])
def dashboard():
    # Fetch summary details
    cursor.execute('''SELECT COUNT(DISTINCT source) AS unique_sources,
                      COUNT(DISTINCT message) AS unique_messages,
                      COUNT(*) AS total_messages
                      FROM dashboard_table''')
    summary = cursor.fetchone()

    # Fetch all rows from the messages table
    cursor.execute('''SELECT * FROM dashboard_table''')
    rows = cursor.fetchall()

    summary_data = {
        'total_unique_sources': summary[0],
        'total_unique_messages': summary[1],
        'total_messages': summary[2]
    }

    detailed_report = []
    for row in rows:
        detailed_report.append({
            'Sno': row[0],
            'Source': row[1],
            'Message': row[2],
            'Time': row[3].strftime("%Y-%m-%d %H:%M:%S")
        })

    return render_template('dashboard.html', summary=summary_data, detailed_report=detailed_report)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
