class Task:
    def __init__(self, id, title, description=None, completed=False):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed

    def __str__(self):
        status = "✓" if self.completed else " "
        desc = f" ({self.description})" if self.description else ""
        return f"[{status}] {self.id}: {self.title}{desc}"

class TodoApp:
    def __init__(self):
        self.tasks = []
        self._next_id = 1

    def add_task(self, title, description=None):
        task = Task(self._next_id, title, description)
        self.tasks.append(task)
        self._next_id += 1
        return task

    def get_all_tasks(self):
        return self.tasks

    def mark_task_complete(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.completed = True
                return True
        return False

    def update_task(self, task_id, new_title=None, new_description=None):
        for task in self.tasks:
            if task.id == task_id:
                if new_title is not None:
                    task.title = new_title
                return True
        return False

    def delete_task(self, task_id):
        initial_len = len(self.tasks)
        self.tasks = [task for task in self.tasks if task.id != task_id]
        return len(self.tasks) < initial_len

def display_menu():
    print("\n--- Todo CLI App ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Complete")
    print("4. Update Task")
    print("5. Delete Task")
    print("6. Exit")

def main():
    app = TodoApp()
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description (optional): ")
            app.add_task(title, description if description else None)
            print("Task added successfully!")
        elif choice == '2':
            tasks = app.get_all_tasks()
            if not tasks:
                print("No tasks to display.")
            else:
                for task in tasks:
                    print(task)
        elif choice == '3':
            task_id = int(input("Enter the ID of the task to mark as complete: "))
            if app.mark_task_complete(task_id):
                print(f"Task {task_id} marked as complete.")
            else:
                print(f"Task {task_id} not found.")
        elif choice == '4':
            task_id = int(input("Enter the ID of the task to update: "))
            new_title = input("Enter new title (leave blank to keep current): ")
            new_description = input("Enter new description (leave blank to keep current): ")
            if app.update_task(task_id, new_title if new_title else None, new_description if new_description else None):
                print(f"Task {task_id} updated successfully.")
            else:
                print(f"Task {task_id} not found.")
        elif choice == '5':
            task_id = int(input("Enter the ID of the task to delete: "))
            if app.delete_task(task_id):
                print(f"Task {task_id} deleted successfully.")
            else:
                print(f"Task {task_id} not found.")
        elif choice == '6':
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()

