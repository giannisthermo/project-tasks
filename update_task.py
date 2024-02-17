import sqlite3


def update_task(task_id, new_task_name=None, new_status=None):
    """
    Updates the task name and/or status for a given task ID.
    """
    conn = sqlite3.connect('ProjectTasks.db')
    cursor = conn.cursor()

    # Update task name if new_task_name is provided
    if new_task_name:
        cursor.execute("UPDATE Tasks SET TaskName = ? WHERE TaskID = ?", (new_task_name, task_id))

    # Update status if new_status is provided
    if new_status:
        cursor.execute("UPDATE Tasks SET Status = ? WHERE TaskID = ?", (new_status, task_id))

    conn.commit()
    print("Task updated successfully.")
    conn.close()


if __name__ == "__main__":
    # Prompt user for task ID and new values
    task_id = input("Enter the Task ID of the task you want to update: ")
    new_task_name = input("Enter the new task name (or press Enter to skip): ")
    new_status = input("Enter the new task status (Pending, In Progress, Completed) or press Enter to skip: ")

    # Call the update function with user inputs
    update_task(task_id, new_task_name if new_task_name.strip() != "" else None,
                new_status if new_status.strip() != "" else None)
