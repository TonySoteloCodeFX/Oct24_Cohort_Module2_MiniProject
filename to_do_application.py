from art import welcome, goodbye
import os

incomplete_tasks = []
completed_tasks = []

def clr():
    '''This clears the terminal.'''
    os.system('cls' if os.name == 'nt' else 'clear')

def add_task():
    '''Adds task to incomplete list & returns confirmation.'''
    clr()
    try:
        print("-" * 50)
        new_task = input("Enter task name: ")
        if len(new_task) < 4:
            print("-" * 50)
            print("Task names must be at least 4 characters long. Try again.")
            print("-" * 50)
        else:
            print("-" * 50)
            incomplete_tasks.append(new_task)
            print(f"{new_task} - has been added to your TO-DO List.")  
            print("-" * 50)         
    except ValueError:
        print("-" * 50)
        print("Sorry, try again.\n")
        print("-" * 50)

def view_tasks():
    '''Prints out all tasks with their status.'''
    clr()
    all_tasks = incomplete_tasks + completed_tasks
    for index, task in enumerate(all_tasks):
        print("-" * 50)
        if task in incomplete_tasks:
            print(f"Task #{index + 1}: {task}: Incomplete")
            print("-" * 50)
        else:
            print(f"Task #{index + 1}: {task}: Completed")
            print("-" * 50)

def mark_complete():
    '''Marks given task as complete and returns confirmation.'''
    clr()
    print("-" * 50)
    try:
        print("Marking the following task complete.")
        task_to_mark_complete = input("Enter task name: ")
        if task_to_mark_complete in completed_tasks:
            print(f"{task_to_mark_complete}: is already completed\n")
        elif task_to_mark_complete not in completed_tasks and task_to_mark_complete in incomplete_tasks:
            completed_tasks.append(task_to_mark_complete)
            incomplete_tasks.remove(task_to_mark_complete)
            print("-" * 50)
            print(f"{task_to_mark_complete}: Completed\n") 
            print("-" * 50)
    except ValueError:
        print("Sorry. Try again.")

def delete_task():
    '''Deletes task given and returns confirmation.'''
    clr()
    print("-" * 50)
    try:
        print("Removing the following task.")
        task_to_delete = input("Enter task name: ")
        if task_to_delete in completed_tasks:
            completed_tasks.remove(task_to_delete)
            print("-" * 50)
            print(f"{task_to_delete} has been deleted.")
            print("-" * 50)
        else:
            incomplete_tasks.remove(task_to_delete)
            print("-" * 50)
            print(f"{task_to_delete} has been deleted.")
            print("-" * 50)
    except ValueError:
        print("Sorry. Try again.")


keep_running = True
clr()
print(welcome)
while keep_running:
    print("Menu:")
    print("1. Add a task\n2. View tasks\n3. Mark a task as complete\n4. Delete a task\n5. Quit")
    print("-" * 50)
    
    try:
        operation = int(input("Enter Option: "))
        if operation == 1:
            add_task()
        elif operation == 2:
            view_tasks()
        elif operation == 3:
            mark_complete()
        elif operation == 4:
            delete_task()
        elif operation == 5:
            clr()
            print(goodbye)
            keep_running = False
        else:
            clr()
            print("-" * 50)
            print("That is not an option. Try again.\n")
    except ValueError:
        print("You must type a number. Try again.")
        print("-" * 50)
    finally:
        print("Thank you for using the TO-DO Application\n")
        print("-" * 50)