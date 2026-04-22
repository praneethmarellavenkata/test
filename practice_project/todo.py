tasks = []

def add_task(title):
    tasks.append({"title": title, "done": False})
    print(f"Added: {title}")

def list_tasks():
    if not tasks:
        print("No tasks yet!")
        return
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["done"] else "○"
        print(f"{i}. [{status}] {task['title']}")

def complete_tasks(index):
    tasks[index - 1]["done"] = True
    print(f"Completed: {tasks[index - 1]['title']}")

def main():
    print("=== My Todo App ===")
    add_task("Buy groceries")
    add_task("Learn Git")
    complete_tasks(2)
    list_tasks()

if __name__ == "__main__":
    main()
