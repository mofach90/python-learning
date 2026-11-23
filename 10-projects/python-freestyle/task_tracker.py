# i deided to transform the task-list directly inside fill_task_list() to a map like that: 
# {
# "uncomplete" : [list of uncompeted tasks], 
# "complete"  ; [list of completed tasks]
# }
# then just send the uncomplete tasks to the remove functions, and inside the funtion move the uncomplete to the complete


import json
from logging import DEBUG
from pathlib import Path
from textwrap import indent

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
    # print("DEBUG:", list_task)
    index = ''
    while list_task["uncomplete"]:
        show_task_list(list_task)
        index = input("\nEnter your task index from the list: ").strip().lower()
        if index.isdigit() and int(index) in range(1,len(list_task["uncomplete"])+1):
            break
    list_task["complete"].append(list_task["uncomplete"][int(index)-1])
    list_task["uncomplete"].pop(int(index)-1)
    
def remove_task_with_title(list_task):
    task = ""
    while task not in list_task["uncomplete"]:
        show_task_list(list_task)
        task = input("\nEnter your task title from the list: ").strip().lower()
    print(f"\nRemoving {task}")
    list_task["complete"].append(task)
    list_task["uncomplete"].remove(task)
 




def show_task_list(list_task):
    print("\nYour task(s):")
    uncomplete_tasks = list_task["uncomplete"]
    complete_tasks = list_task["complete"]
    # print("DEBUG:", list_task)
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
            

def fill_task_list() -> dict[str,list]:
    list_task = {"uncomplete":[] , "complete":[]}
    uncomplete = []
    task_title = ""
    while task_title != "done":
        if task_title and task_title not in uncomplete:
            uncomplete.append(task_title)
        task_title = input("\nPlease entre a task title: ").strip().lower()
    if uncomplete:
        list_task = { "uncomplete" : uncomplete, "complete" : []}
        show_task_list(list_task)
    return list_task

# def get_new_task_list(list_task) -> dict[str,tuple]:
#     new_task_list = {}
#     n = 1
#     for (t, b) in list_task.items():
#         if b:
#             complete[n] = (t,b)
#             n += 1
#     return new_task_list
def save_data(data, target_file_name):
    tarjet_folder = Path.cwd() / "Tasks"
    tarjet_folder.mkdir(exist_ok=True)
    target = tarjet_folder / target_file_name
    try:
        with open( target, "w", encoding="utf-8") as file:
            json.dump(data,file, indent=2)
    except Exception as error:
        print("Data is not saved and the error is :", error)
    finally:
        print("save data function runs...")

def restore_local_data() -> dict[str,list]:
    data = {}
    file_path = input("If you have a List of tasks , privide the file path or leave empty: ").lower().strip()
    try:
        with open(file_path,"r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("no local data found, start with empty list")
        return {}
    except Exception:
        print("Error: ", Exception)
    return data

def main():
    data = restore_local_data()
    if data["uncomplete"]:
        list_task = data
    else:
        list_task = fill_task_list()
    print("Data:", list_task)
    choice_action_map = {
        "0": (),
        "1": (remove_task_with_title, {"list_task":list_task}),
        "2": (remove_task_whith_index, {"list_task":list_task}),
    }
    while list_task["uncomplete"]:  
        choice = get_choice()
        if choice == "0" :
            break
        if list_task:
            func, kwargs = choice_action_map[choice]
            func(**kwargs)
        if list_task: 
            show_task_list(list_task)
    save_data(list_task, "test1.json")
    print("\nExiting....")

    return

main()
# import json
# import os
# from pathlib import Path
# 
# 
# 
# current_dir = Path.cwd()
# print("current path:", current_dir, type(current_dir))
# 
# test_folder = current_dir / "Tests"
# test_folder.mkdir(exist_ok=True)
# test_file = test_folder / "test1.json"
# 
# data = {"1":{"a":"ddd", "b":12}, "22":2, 32:1}
# 
# 
# with open(test_file, "w", encoding="utf-8") as file:
#     json.dump(data,file)
# 
# with open(test_file, "r", encoding="utf-8") as file:
#     # data1 = json.load(file)
#     # data1 = file.read()
#     # print("data1:", data1)
#     # print(type(data1))
#     data2 = json.loads(file.read())
#     print("data2:", data2)

