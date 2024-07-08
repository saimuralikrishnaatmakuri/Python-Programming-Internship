# Initialize an empty list to store tasks
tasks = []

def show_tasks():
  """Prints all tasks and their completion status"""
  if not tasks:
    print("Your list is empty.")
  else:
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks):
      done = "Completed" if task[1] else "Pending"
      print(f"{i+1}. {task[0]} ({done})")

def add_task():
  """Prompts user for new task and adds it to the list"""
  new_task = input("Enter the new task: ")
  tasks.append([new_task, False])  # Store task and completion status (False = not completed)
  print("Task added!")

def mark_done():
  """Marks a task as completed based on user input"""
  show_tasks()
  if not tasks:
    return
  while True:
    try:
      task_number = int(input("Enter the number of the task to mark as done: "))
      if 1 <= task_number <= len(tasks):
        tasks[task_number - 1][1] = True  # Set completion status to True
        print("Task marked as done!")
        break
      else:
        print("Invalid task number.")
    except ValueError:
      print("Please enter a valid number.")

def remove_task():
  """Removes a task from the list based on user input"""
  show_tasks()
  if not tasks:
    return
  while True:
    try:
      task_number = int(input("Enter the number of the task to remove: "))
      if 1 <= task_number <= len(tasks):
        del tasks[task_number - 1]
        print("Task removed!")
        break
      else:
        print("Invalid task number.")
    except ValueError:
      print("Please enter a valid number.")
#new comment
def main():
  """Main loop for user interaction"""
  while True:
    print("\nTo-Do List Options:")
    print("1. Display To-Do List")
    print("2. Add a Task")
    print("3. Mark a Task as Done")
    print("4. Remove a Task")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
      show_tasks()
    elif choice == '2':
      add_task()
    elif choice == '3':
      mark_done()
    elif choice == '4':
      remove_task()
    elif choice == '5':
      print("Exiting To-Do List...")
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()
