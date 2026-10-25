
# ask tje user which task they completed
def get_choice():
    choices = ["0","1","2"]
    while True:
        print("\nChoose how you would search and check a task:")
        print("0- Exit the program")
        print("1- for Task Title")
        print("2- for Task Index")
        choice = input("\nEnter your choice: ").strip()
        if choice in choices:
            return choice
        print("\n Please provide a valid choice :) ")
        
def remove_task_title(list_task):
    task_title = ""
    while not task_title or task_title not in list_task:
        task_title = input("\nEntre a title from your task list: ").strip()
    print(f"\nRemoving {task_title}")
    list_task.remove(task_title)

def remove_task_index(list_task):
    task_index = ""
    while not task_index.isdigit() or int(task_index) not in range(1,len(list_task)+1):
        task_index = input("\nEnter your task index from the list: ")
    task_index_rem = int(task_index) - 1
    print(f"\nRemoving {list_task[task_index_rem]}")
    list_task.remove(list_task[task_index_rem])


def exit_programm():
    print("\nExiting....")
    exit()
    

def show_task_list(list_task):
    print("\nYour task(s):\n")
    n = 1
    for i in list_task:
        print(f"{n} : {i}\n")
        n += 1
    

list_task = []
task_title = ""
while task_title.lower() != "done":
    if task_title and task_title not in list_task:
        list_task.append(task_title)
    task_title = input("\nPlease entre a task title: ").strip()
if not list_task:
    print(" no tasks ! program exit ..")
    exit()

show_task_list(list_task)
    
task_title = ""
task_number = "-1"
# get choices
choice_action_map = {
    "0": (exit_programm, {}),
    "1": (remove_task_title, {"list_task":list_task}),
    "2": (remove_task_index, {"list_task":list_task}),
}

choice = get_choice()
func, kwargs = choice_action_map[choice]
# print(**kwargs)
func(**kwargs)

show_task_list(list_task)


