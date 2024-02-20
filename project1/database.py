import mysql.connector
import json


def load_config():
    with open('config.json', 'r') as config_file:
        config_data = json.load(config_file)
    return config_data


def adding_password(new_password):
    connection = get_database_connection()
    cursor = connection.cursor()
    alter_query = "ALTER USER 'root'@'localhost' IDENTIFIED WITH 'mysql_native_password' BY %s;"
    cursor.execute(alter_query, (new_password,))
    connection.commit()
    cursor.close()
    connection.close()


def get_database_connection():
    config = load_config()
    return mysql.connector.connect(**config['DATABASE_CONFIG'])


def create_database():
    connection = get_database_connection()
    cursor = connection.cursor()
    cursor.execute('CREATE DATABASE IF NOT EXISTS employees_info;')
    cursor.execute('USE employees_info;')
    connection.commit()
    cursor.close()
    connection.close()


def create_table():
    connection = get_database_connection()
    cursor = connection.cursor()
    # cursor.execute('CREATE DATABASE IF NOT EXISTS employees_info;')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Employees (
        id INT AUTO_INCREMENT PRIMARY KEY,
        Employee_Name VARCHAR(255) NOT NULL,
        Employee_DateOfJoining DATE NOT NULL,
        Employee_Location VARCHAR(255),
        Employee_Project VARCHAR(255)
    );''')
    connection.commit()
    cursor.close()
    connection.close()


def get_employees():
    connection = get_database_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM Employees')
    employees = cursor.fetchall()
    cursor.close()
    connection.close()
    return employees


def add_employee(Employee_Name, Employee_DateOfJoining, Employee_Location, Employee_Project):
    connection = get_database_connection()
    cursor = connection.cursor()
    cursor.execute(
        'INSERT INTO Employees (Employee_Name, Employee_DateOfJoining,Employee_Location,Employee_Project) VALUES (%s, %s,%s,%s)',
        (Employee_Name, Employee_DateOfJoining, Employee_Location, Employee_Project))
    connection.commit()
    cursor.close()
    connection.close()


def get_employee(Employee_ID):
    connection = get_database_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM Employees WHERE Employee_ID=%s', (Employee_ID,))
    employee = cursor.fetchone()
    cursor.close()
    connection.close()
    return employee


def update_employee(Employee_ID, Employee_Name, Employee_DateOfJoining, Employee_Location, Employee_Project):
    connection = get_database_connection()
    cursor = connection.cursor()
    cursor.execute(
        'UPDATE Employees SET  Employee_Name=%s, Employee_DateOfJoining=%s,Employee_Location=%s,Employee_Project=%s WHERE Employee_ID=%s',
        (Employee_Name, Employee_DateOfJoining, Employee_Location, Employee_Project, Employee_ID))
    connection.commit()
    cursor.close()
    connection.close()


def delete_employee(Employee_ID):
    connection = get_database_connection()
    cursor = connection.cursor()
    cursor.execute('DELETE FROM Employees WHERE Employee_ID=%s', (Employee_ID,))
    connection.commit()
    cursor.close()
    connection.close()


def main():
    config = load_config()
    config_data = config["DATABASE_CONFIG"]
    newpassword = config_data["password"]
    adding_password(newpassword)
    create_database()
    create_table()


if __name__ == "__main__":
    main()
