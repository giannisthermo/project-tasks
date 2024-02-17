import sqlite3


def add_task(task_name, status):
    """
    Inserts a new task into the Tasks table.
    """
    conn = sqlite3.connect('ProjectTasks.db')
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Tasks (TaskName, Status) VALUES (?, ?)", (task_name, status))
        conn.commit()
        print("Task added successfully.")
    except sqlite3.Error as e:
        print("Error occurred:", e)
    finally:
        conn.close()


if __name__ == "__main__":
    # Prompt the user to enter the task name and status
    task_name = input("Enter the task name: ")
    status = input("Enter the task status (Pending, In Progress, Completed): ")

    # Validate status input
    if status in ['Pending', 'In Progress', 'Completed']:
        add_task(task_name, status)
    else:
        print("Invalid status. Please enter 'Pending', 'In Progress', or 'Completed'.")
