import json
import os
import sys

DATA_FILE = "tasks.json"

def load_tasks() -> list[dict]:
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return []

def save_tasks(tasks: list[dict]):
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(tasks, f, indent=4)
    except OSError as e:
        print(f"Error saving data: {e}")

def display_tasks(tasks: list[dict]):
    if not tasks:
        print("\nNo tasks found.")
        return

    priority_map = {1: "🔴 High", 2: "🟡 Medium", 3: "🟢 Low"}
    sorted_tasks = sorted(tasks, key=lambda x: (x["completed"], x["priority"]))

    print("\n--- YOUR TASK LIST ---")
    for idx, task in enumerate(sorted_tasks, start=1):
        status = "✅ Completed" if task["completed"] else "❌ Pending"
        p_label = priority_map.get(task["priority"], "Unknown")
        print(f"{idx}. [{status}] [{p_label}] {task['title']}")
    print("-" * 30)

def get_valid_int(prompt: str, min_val: int, max_val: int) -> int:
    while True:
        user_input = input(prompt).strip()
        if user_input.lower() == "exit":
            print("Goodbye!")
            sys.exit()
        try:
            val = int(user_input)
            if min_val <= val <= max_val:
                return val
            print(f"Enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Enter a whole number.")

def add_task(tasks: list[dict]):
    title = input("Enter task title: ").strip()
    if not title:
        print("Task title cannot be empty.")
        return

    print("Select Priority:")
    print("1. High | 2. Medium | 3. Low")
    priority = get_valid_int("Priority (1-3): ", 1, 3)

    tasks.append({"title": title, "priority": priority, "completed": False})
    save_tasks(tasks)
    print(f"Task '{title}' added.")

def mark_completed(tasks: list[dict]):
    pending = [t for t in tasks if not t["completed"]]
    if not pending:
        print("No pending tasks to complete.")
        return

    display_tasks(tasks)
    sorted_tasks = sorted(tasks, key=lambda x: (x["completed"], x["priority"]))
    choice = get_valid_int("Enter task number to mark complete: ", 1, len(sorted_tasks))
    
    target_task = sorted_tasks[choice - 1]
    target_task["completed"] = True
    save_tasks(tasks)
    print(f"Marked '{target_task['title']}' as completed.")

def delete_task(tasks: list[dict]):
    if not tasks:
        print("No tasks to delete.")
        return

    display_tasks(tasks)
    sorted_tasks = sorted(tasks, key=lambda x: (x["completed"], x["priority"]))
    choice = get_valid_int("Enter task number to delete: ", 1, len(sorted_tasks))

    target_task = sorted_tasks[choice - 1]
    tasks.remove(target_task)
    save_tasks(tasks)
    print(f"Deleted task: '{target_task['title']}'")

def main():
    tasks = load_tasks()
    print("=== Personal Task Tracker ===")
    print("Type 'exit' at any prompt to quit.\n")

    while True:
        print("\nMenu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("\nChoose option (1-5): ").strip().lower()

        if choice in ["5", "exit"]:
            print("Goodbye!")
            sys.exit()
        elif choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        else:
            print("Invalid choice. Select from 1 to 5.")

if __name__ == "__main__":
    main()
