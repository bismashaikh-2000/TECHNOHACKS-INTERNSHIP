# task 1
# To-do list

print(' -----------------------------------')
print('        TO-DO LIST APPLICATION      ')
print(' -----------------------------------')

to_do_list = []
def add_task():
    print("Let's add a new task.")
    add_task = input('Enter a task:')
    to_do_list.append(add_task)
    print("You did it! Your task added successfully.")

def update_task():
    if not to_do_list:
        print("Oops! You can't update a list because your task list is empty.")
    else:
        task_update = input('Enter an updated task: ')
        task_index = int(input('Enter index to replace the task in any field: ')) - 1
        if 0 <= task_index < len(to_do_list):
            to_do_list[task_index] = task_update
            print('Your task has been updated successfully!')
        else:
            print('Please add the task first.')
            print('Invalid input. Task not updated.')
# Remove the task at the specified index
def delete_task():
    if not to_do_list:
        print("No tasks in the to-do list. Please add your task first")

    else:
        task_index = int(input('Enter index for which you want to remove the task:')) - 1
        if 0 <= task_index < len(to_do_list):
            del to_do_list[task_index]
            print('Task successfully deleted.')
        else:
            print('Select the right index!')
# main loop
try:
    while True:
        print()
        print('MENU:')
        print("1. Add New Task")
        print("2. Update Task")
        print("3. Delete Tasks")
        print("4. View Your Task List")
        print("5. close")

        choice = int(input('Enter the number of your chosen option:'))
        if choice == 1:
            add_task()

        elif choice == 2:
            update_task()

        elif choice == 3:
            delete_task()

        elif choice == 4:
            # View the list of tasks
            print("Let's review existing tasks list!")

            if not to_do_list:
                print("OPPS, Their is No tasks in the to-do list.")

            else:
                print("=" * 30)
                print("{:<10} {:<30}".format("S.NO", "TASK'S"))
                print("=" * 30)
                for index, task in enumerate(to_do_list, start=1):
                    print("{:<10} {:<30}".format(index, task))

        elif choice == 5:
            # Exit the application
            print("Exit the To-Do List Application. Have a good day!")
            break

        else:
            print("Oops! It's not valid option!! Please select a valid option number")

# exception handling
except ValueError:
    print('Invalid Input!! PLease enter a number.')