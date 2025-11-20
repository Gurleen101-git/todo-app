import os

TODO_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        tasks = [line.strip() for line in file.readlines()]
    return tasks

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet!\n")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    print()

def add_task(tasks):
    task = input("Enter task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!\n")

def complete_task(tasks):
    show_tasks(tasks)
    num = int(input("Enter task number to mark as completed: "))
    if 1 <= num <= len(tasks):
        tasks[num - 1] += " (Completed)"
        save_tasks(tasks)
        print("Task marked as completed!\n")
    else:
        print("Invalid task number!\n")

def delete_task(tasks):
    show_tasks(tasks)
    num = int(input("Enter task number to delete: "))
    if 1 <= num <= len(tasks):
        tasks.pop(num - 1)
        save_tasks(tasks)
        print("Task deleted successfully!\n")
    else:
        print("Invalid task number!\n")

def menu():
    tasks = load_tasks()
    while True:
        print("------ TO-DO LIST MANAGER ------")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Try again.\n")

menu()
