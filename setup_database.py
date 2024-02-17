import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('ProjectTasks.db')

# Create a cursor object
cursor = conn.cursor()

# Create the Tasks table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Tasks (
    TaskID INTEGER PRIMARY KEY AUTOINCREMENT,
    TaskName TEXT NOT NULL,
    Status TEXT NOT NULL
)
''')

# Commit changes and close the connection
conn.commit()
conn.close()
