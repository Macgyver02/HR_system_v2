import sqlite3
import os
file_path = os.path.dirname(os.path.abspath(__file__))
database_path = os.path.join(file_path,'employees_database.db')
def get_or_create_db():
    '''this function creates our db'''
    connection = sqlite3.connect(database_path)
    mycursor = connection.cursor()
    connection.commit()
    connection.close()

def create_table_employees():
    '''creates an employees table'''
    connection = sqlite3.connect(database_path)
    mycursor = connection.cursor()
    mycursor.execute("""CREATE TABLE IF NOT EXISTS employees(
                     EmpId TEXT  PRIMARY KEY,
                     EmpName TEXT,
                     Gender TEXT,
                     Status TEXT,
                     Position TEXT,
                     Salary TEXT,
                     Days_on_leave TEXT
    )""")
    connection.commit()
    connection.close()

def create_table_admins():
    '''creates an admins table'''
    connection = sqlite3.connect(database_path)
    mycursor = connection.cursor()
    mycursor.execute("""CREATE TABLE IF NOT EXISTS admins(
                     staff_number TEXT  PRIMARY KEY,
                     first_name TEXT,
                     second_name TEXT,
                     last_name TEXT,
                     password TEXT
    )""")
    connection.commit()
    connection.close()

def insert_employee(EmpId ,EmpName ,Gender ,Status,Position,Salary ,Days_on_leave = 'NULL'):
    '''Sends input data to db'''
    connection = sqlite3.connect(database_path)
    mycursor = connection.cursor()
    mycursor.execute('''INSERT INTO employees VALUES (?,?,?,?,?,?,?)''',(EmpId ,EmpName ,Gender ,Status,Position,Salary ,Days_on_leave,))
    connection.commit()
    connection.close()

def fetch_employees():
    '''retrieve all employees details'''
    connection = sqlite3.connect(database_path)
    mycursor = connection.cursor()
    mycursor.execute('''SELECT * FROM employees ''')
    employees = mycursor.fetchall()
    connection.close()
    return employees

def get_employee(EmpId):
    '''retrieve employee details'''
    connection = sqlite3.connect(database_path)
    mycursor = connection.cursor()
    mycursor.execute('''SELECT * FROM employees WHERE EmpId = ? ''',(EmpId ,))
    employee = mycursor.fetchone()
    connection.close()
    return employee

def add_admin(staff_number,first_name,second_name,last_name,password):
    '''add admin to the db'''
    connection = sqlite3.connect(database_path)
    mycursor = connection.cursor()
    mycursor.execute('''INSERT INTO admins VALUES (?,?,?,?,?)''',(staff_number,first_name ,second_name , last_name ,password ,))
    connection.commit()
    connection.close()

def get_admin(staff_number):
    '''gets the admin'''
    connection = sqlite3.connect(database_path)
    mycursor = connection.cursor()
    mycursor.execute('''SELECT * FROM admins WHERE staff_number = ? ''',(staff_number,))
    admin = mycursor.fetchone()
    connection.close()
    return admin

def delete_employee(EmpId):
    '''deletes an employee from the db'''
    connection = sqlite3.connect(database_path)
    mycursor = connection.cursor()
    mycursor.execute('''DELETE FROM employees WHERE EmpId = ? ''',(EmpId,))
    connection.commit()
    connection.close()

def update_employee(EmpName ,Gender ,Status,Position,Salary ,Days_on_leave,EmpId):
    '''updates an employee'''
    connection = sqlite3.connect(database_path)
    mycursor = connection.cursor()
    mycursor.execute('''UPDATE employees SET 
                     EmpName = ? ,
                     Gender = ? ,
                     Status = ?,
                     Position = ?, 
                     Salary = ?,
                     Days_on_leave = ?
                     
                      WHERE EmpId = ? ''',(EmpName ,Gender ,Status,Position,Salary ,Days_on_leave ,EmpId,))
    connection.commit()
    connection.close()

def update_employee_leave(leave_days, leave_status, emp_id):
    '''update employee leave'''
    connection = sqlite3.connect(database_path)
    mycursor = connection.cursor()
    mycursor.execute('''UPDATE employees SET  
                     Status = ?,
                     Days_on_leave = ?
                      WHERE EmpId = ? ''',(leave_status,leave_days, emp_id,))
    connection.commit()
    connection.close()

def id_exists(EmpId):
    '''checks whether an employee exists'''
    connection = sqlite3.connect(database_path)
    mycursor = connection.cursor()
    mycursor.execute('''SELECT COUNT(*) FROM employees WHERE EmpId = ? ''',(EmpId,))
    result = mycursor.fetchone()
    connection.close()
    return result[0] > 0

get_or_create_db()
create_table_admins()
create_table_employees()