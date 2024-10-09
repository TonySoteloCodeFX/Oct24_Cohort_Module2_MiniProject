from art import welcome

incomplete_tasks = []
completed_tasks = []

def add_task():
    '''Adds task to incomplete list & returns confirmation.'''
    try:
        print("-" * 50)
        new_task = input("Enter task name: ")
        if len(new_task) < 4:
            print("-" * 50)
            return "Task names must be at least 4 characters long. Try again.\n"
        else:
            print("-" * 50)
            incomplete_tasks.append(new_task)
            return f"{new_task} - has been added to your TO-DO List.\n"           
    except ValueError:
        print("-" * 50)
        print("Sorry, try again.\n")

def view_tasks():
    '''Prints out all tasks with their status.'''
    all_tasks = incomplete_tasks + completed_tasks
    for task in all_tasks:
        print("-" * 50)
        print(f"{enumerate(task)}: {'Incomplete' if task in incomplete_tasks else 'Completed'}")

def mark_complete():
    print("-" * 50)
    try:
        print("Marking the following task complete:")
        task_to_mark_complete = input("Enter task name: ")
    except ValueError:
        pass


print(welcome)
print("Menu:")
print("1. Add a task\n2. View tasks\n3. Mark a task as complete\n4. Delete a task\n5. Quit\n")