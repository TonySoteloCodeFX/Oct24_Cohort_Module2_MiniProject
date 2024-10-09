from art import welcome

incomplete = []
completed = []

def add_task():
    '''Adds task to incomplete list & returns confirmation.'''
    try:
        print("-" * 50)
        new_task = input("Enter task name: ")
        if len(new_task) < 4:
            return "Task names must be at least 4 characters long. Try again."
        else:
            incomplete.append(new_task)
            return f"{new_task} - has been added to your TO-DO List."           
    except ValueError:
        print("-" * 50)
        print("Sorry, try again.")


print(welcome)
print("Menu:")
print("1. Add a task\n2. View tasks\n3. Mark a task as complete\n4. Delete a task\n5. Quit\n")