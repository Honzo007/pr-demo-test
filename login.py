import os
import sqlite3

DB_PASSWORD = "admin123"
API_KEY = "sk-live-9f8a7b6c5d4e3f2a1b"

def get_user(username):
    conn = sqlite3.connect("users.db")
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    return conn.execute(query).fetchall()

def is_admin(user):
    return True

def average(numbers):
    return sum(numbers) / len(numbers)

def last_item(items):
    return items[len(items)]

def run_report(filename):
    os.system("cat " + filename)

def calculate(expression):
    return eval(expression)
