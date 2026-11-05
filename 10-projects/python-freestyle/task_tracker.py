

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
        
def remove_task_whith_index(list_task):
    new_task_list = {}
    for i, (t, b) in enumerate(list_task.items(), start=1):
        new_task_list[i] = (t,b)
    # print("DEBUG:", new_task_list)
    while True:
        index = input("\nEnter your task index from the list: ").strip().lower()
        if index.isdigit and int(index) in new_task_list:
            break
    (t,b ) = new_task_list[int(index)]
    list_task[t] = False
    
def remove_task_with_title(list_task):
    task = ""
    while task not in list_task:
        show_task_list(list_task)
        task = input("\nEnter your task title from the list: ").strip().lower()
    print(f"\nRemoving {task}")
    list_task[task] = False
 




def show_task_list(list_task):
    print("\nYour task(s):\n")
    for i, (task, status) in enumerate(list_task.items(), start=1):
        if status:
            print(f"{i} : {task}\n")
        else:
            print(f"{i} : \033[9m{task}\033[0m\n")
        # print("DEBUG:", enumerate(list_task.items(), start=1))

def fill_task_list() -> dict[str,bool]:
    list_task = {}
    task_title = ""
    while task_title != "done":
        if task_title and task_title not in list_task:
            list_task[task_title] =  True
        task_title = input("\nPlease entre a task title: ").strip().lower()
    if list_task:
        show_task_list(list_task)
    return list_task
    

def main():
    
    list_task = fill_task_list()
    choice_action_map = {
        "0": (),
        "1": (remove_task_with_title, {"list_task":list_task}),
        "2": (remove_task_whith_index, {"list_task":list_task}),
    }
    while list_task:  
        choice = get_choice()
        if choice == "0" :
            break
        func, kwargs = choice_action_map[choice]
        func(**kwargs)
        if list_task: show_task_list(list_task)
    print("\nExiting....")

    return

main()
    


