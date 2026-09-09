import sqlite3

# High Severity: Hardcoded credentials
DB_USER = "admin"
DB_PASS = "supersecretpassword123"

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