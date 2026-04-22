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

def main():
    add_task("Buy groceries")
    add_task("Learn Git")
    list_tasks()

if __name__ == "__main__":
    main()
