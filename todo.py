# ============================================
# CodSoft Python Internship
# Task 1: To-Do List Application
# ============================================

tasks = []

def show_menu():
    print("\n" + "=" * 40)
    print("        TO-DO LIST APPLICATION")
    print("=" * 40)
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Mark Task as Completed")
    print("5. Exit")
    print("=" * 40)


def view_tasks():
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            status = "✔" if task["completed"] else "✘"
            print(f"{index}. [{status}] {task['title']}")


def add_task():
    title = input("\nEnter the task: ").strip()

    if title == "":
        print("Task cannot be empty!")
        return

    tasks.append({
        "title": title,
        "completed": False
    })

    print("Task added successfully!")


def remove_task():
    view_tasks()

    if not tasks:
        return

    try:
        task_no = int(input("\nEnter task number to remove: "))

        if 1 <= task_no <= len(tasks):
            removed = tasks.pop(task_no - 1)
            print(f"'{removed['title']}' removed successfully.")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def mark_completed():
    view_tasks()

    if not tasks:
        return

    try:
        task_no = int(input("\nEnter task number to mark as completed: "))

        if 1 <= task_no <= len(tasks):
            tasks[task_no - 1]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


while True:
    show_menu()

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        view_tasks()

    elif choice == "2":
        add_task()

    elif choice == "3":
        remove_task()

    elif choice == "4":
        mark_completed()

    elif choice == "5":
        print("\nThank you for using the To-Do List Application!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
