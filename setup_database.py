import sqlite3
import random

conn = sqlite3.connect("database.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS employees")
cur.execute("""
CREATE TABLE employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    department TEXT,
    salary INTEGER,
    city TEXT
)
""")

departments = ["HR", "Tech", "Finance", "Marketing"]
cities = ["Mumbai", "Delhi", "Bengaluru", "Chennai"]

for i in range(5000):
    cur.execute("INSERT INTO employees (name, department, salary, city) VALUES (?, ?, ?, ?)",
                (f"Emp{i}", random.choice(departments), random.randint(30000, 150000), random.choice(cities)))

conn.commit()
conn.close()
print("Database created with sample data!")
