import mysql.connector
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

def get_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

def get_all_employees():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM employees")

    employees = cursor.fetchall()

    cursor.close()
    conn.close()

    return employees

def add_employee(id, name, department):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    INSERT INTO employees(id, name, department)
    VALUES(%s, %s, %s)
    """

    cursor.execute(sql, (id, name, department))

    conn.commit()

    cursor.close()
    conn.close()
    
def get_employee_by_id(emp_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM employees WHERE id=%s",
        (emp_id,)
    )

    employee = cursor.fetchone()

    cursor.close()
    conn.close()

    return employee


def update_employee(emp_id, name, department):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    UPDATE employees
    SET name=%s,
        department=%s
    WHERE id=%s
    """

    cursor.execute(sql, (name, department, emp_id))

    conn.commit()

    cursor.close()
    conn.close()
    
def delete_employee(emp_id):
    conn = get_connection()
    cursor = conn.cursor()

    sql = "DELETE FROM employees WHERE id=%s"

    cursor.execute(sql, (emp_id,))

    conn.commit()

    cursor.close()
    conn.close()