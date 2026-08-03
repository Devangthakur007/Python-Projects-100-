import sys

def display_tasks(tasks: list[dict]):
    """Print the current list of tasks with their status."""
    if not tasks:
        print("\nYour to-do list is empty!")
        return

    print("\n--- Your to-do list ---")
    for idx, task in enumerate(tasks, start=1):
        # Fixed: using task['completed'] instead of tasks['completed']
        status = "Done" if task["completed"] else "Pending"
        print(f"{idx}. [{status}] {task['title']}")
    print("-" * 30)


def get_valid_index(prompt: str, max_limit: int) -> int:
    """Helper to safely get a valid task number from the user."""
    while True:
        user_input = input(prompt).strip()
        
        if user_input.lower() == 'exit':
            print("Goodbye!")
            sys.exit()
            
        try:
            val = int(user_input)
            if 1 <= val <= max_limit:
                return val - 1  # Convert to 0-based index
            print(f"Please enter a number between 1 and {max_limit}.\n")
        except ValueError:
            print("Invalid input! Please enter a valid number.\n")


def todo_app():
    tasks = []
    print("=== Python CLI To-Do List ===")
    print("Type 'exit' at any prompt to quit.\n")

    while True:
        print("\nMain Menu:")
        print("1. View Tasks")
        print("2. Add Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("\nEnter choice (1-5): ").strip().lower()

        if choice in ['5', 'exit']:
            print("Goodbye! Keep being productive!")
            sys.exit()

        elif choice == '1':
            display_tasks(tasks)

        elif choice == '2':
            title = input("Enter the task title: ").strip()
            if not title:
                print("Task title cannot be empty!")
                continue
            tasks.append({"title": title, "completed": False})
            print(f"Task '{title}' added successfully!")

        elif choice == '3':
            if not tasks:
                print("No tasks available to mark complete.")
                continue
            display_tasks(tasks)
            task_idx = get_valid_index("Enter task number to mark complete: ", len(tasks))
            tasks[task_idx]["completed"] = True
            print(f"Marked '{tasks[task_idx]['title']}' as complete!")

        elif choice == '4':
            if not tasks:
                print("No tasks available to delete.")
                continue
            display_tasks(tasks)
            task_idx = get_valid_index("Enter task number to delete: ", len(tasks))
            removed_task = tasks.pop(task_idx)
            print(f"Deleted task: '{removed_task['title']}'")

        else:
            print("Invalid option! Please enter a number between 1 and 5.")


if __name__ == "__main__":
    todo_app()