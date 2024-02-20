from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# SQLite database setup
conn = sqlite3.connect('employee.db')
cursor = conn.cursor()

# Create an employee table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        position TEXT NOT NULL,
        salary REAL NOT NULL
    )
''')
conn.commit()
conn.close()


# Helper function to serialize employee data
def serialize_employee(employee):
    return {
        'id': employee[0],
        'name': employee[1],
        'position': employee[2],
        'salary': employee[3]
    }


# POST API to create an employee
@app.route('/employees', methods=['POST'])
def create_employee():
    data = request.get_json()
    if 'name' in data and 'position' in data and 'salary' in data:
        conn = sqlite3.connect('employee.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO employees (name, position, salary)
            VALUES (?, ?, ?)
        ''', (data['name'], data['position'], data['salary']))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Employee created successfully'}), 201
    else:
        return jsonify({'error': 'Incomplete data'}), 400


# GET API to retrieve all employees
@app.route('/employees', methods=['GET'])
def get_all_employees():
    conn = sqlite3.connect('employee.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employees')
    employees = cursor.fetchall()
    conn.close()
    serialized_employees = [serialize_employee(employee) for employee in employees]
    return jsonify(serialized_employees)


# GET API to retrieve a specific employee by ID
@app.route('/employees/<int:id>', methods=['GET'])
def get_employee(id):
    conn = sqlite3.connect('employee.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employees WHERE id = ?', (id,))
    employee = cursor.fetchone()
    conn.close()
    if employee:
        return jsonify(serialize_employee(employee))
    else:
        return jsonify({'error': 'Employee not found'}), 404


# PUT API to update an employee by ID
@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    data = request.get_json()
    if 'name' in data and 'position' in data and 'salary' in data:
        conn = sqlite3.connect('employee.db')
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE employees
            SET name = ?, position = ?, salary = ?
            WHERE id = ?
        ''', (data['name'], data['position'], data['salary'], id))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Employee updated successfully'})
    else:
        return jsonify({'error': 'Incomplete data'}), 400


# DELETE API to delete an employee by ID
@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    conn = sqlite3.connect('employee.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM employees WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Employee deleted successfully'})


if __name__ == '__main__':
    app.run(debug=True)
