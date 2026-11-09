# i deided to transform the task-list directly inside fill_task_list() to a map like that: 
# {
# "uncomplete" : [list of uncompeted tasks], 
# "complete"  ; [list of completed tasks]
# }
# then just send the uncomplete tasks to the remove functions, and inside the funtion move the uncomplete to the complete

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

    print("DEBUG:", list_task)
    while True:
        show_task_list(list_task)
        index = input("\nEnter your task index from the list: ").strip().lower()
        if index.isdigit() and int(index) in list_task:
            break
    (t,b ) = list_task[int(index)]
    list_task[t] = False
    
def remove_task_with_title(list_task):
    task = ""
    while task not in list_task:
        show_task_list(list_task)
        task = input("\nEnter your task title from the list: ").strip().lower()
    print(f"\nRemoving {task}")
    list_task[task] = False
 




def show_task_list(list_task):
    print("\nYour task(s):")
    uncomplete_tasks = []
    complete_tasks = []
    for i in list_task:
        if list_task[i][1]:
            uncomplete_tasks.append(list_task[i][0])
        else:
            complete_tasks.append(list_task[i][0])
    # print("DEBUG:", uncomplete_tasks)
    if uncomplete_tasks:
        print("\nUmcompleted Tasks:")
        for i in range(len(uncomplete_tasks)):
            print(f"{i+1} : {uncomplete_tasks[i]}")
    else:
        print("\nAll tasks are DONE !!")
    if complete_tasks:
        print("\nCompleted Tasks:")
        # print("DEBUG:", complete_tasks)
        for i in range(len(complete_tasks)):
            print(f"{i+1} : \033[9m{complete_tasks[i]}\033[0m")
            

def fill_task_list() -> dict[str,tuple]:
    list_task = {}
    task_title = ""
    while task_title != "done":
        if task_title and task_title not in list_task:
            list_task[task_title] =  True
        task_title = input("\nPlease entre a task title: ").strip().lower()
    if list_task:
        list_task = get_new_task_list(list_task)
        show_task_list(list_task)
    return list_task

def get_new_task_list(list_task) -> dict[str,tuple]:
    new_task_list = {}
    n = 1
    for (t, b) in list_task.items():
        if b:
            new_task_list[n] = (t,b)
            n += 1
    return new_task_list

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
        if list_task:
            func, kwargs = choice_action_map[choice]
            func(**kwargs)
        if list_task: 
            show_task_list(list_task)
    print("\nExiting....")

    return

main()
    


