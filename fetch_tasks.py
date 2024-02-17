import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('ProjectTasks.db')

# Create a cursor object
cursor = conn.cursor()

# Fetch all tasks
cursor.execute("SELECT * FROM Tasks")

# Fetch all rows from the last executed query
tasks = cursor.fetchall()

# Check if tasks are found and print them
if tasks:
    for task in tasks:
        print(f"Task ID: {task[0]}, Task Name: {task[1]}, Status: {task[2]}")
else:
    print("No tasks found.")

# Close the connection
conn.close()
