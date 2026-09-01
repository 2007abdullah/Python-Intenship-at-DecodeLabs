tasks = []


def add_task():
    task = input("Enter your task: ").strip()

    if task:
        tasks.append(task)
        print("✅ Task added successfully!")
    else:
        print("❌ Task cannot be empty.")
        



def view_tasks():
    if not tasks:
        print("\n📋 No tasks available.")
        return

    print("\n📋 Your Tasks:")

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")




def main():
    while True:
        print("\n" + "=" * 50)
        print("                 TO-DO LIST")
        print("=" * 50)
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")
        print("=" * 50)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            print("\nThank you for using the To-Do List! 👋")
            break

        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()