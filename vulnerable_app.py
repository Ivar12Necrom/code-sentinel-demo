import sqlite3
import os

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

def get_user_data(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # High/Critical Severity: SQL Injection Vulnerability
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
    
    return cursor.fetchall()

def execute_math_expression(expression):
    # Critical Severity: Remote Code Execution (RCE)
    return eval(expression)