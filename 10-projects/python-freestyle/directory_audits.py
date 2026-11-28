# problem : bulding a directory audit tool
# 
# Functional Req:
# - detect if the input path is a valid dir and not a file
# - count how many files inside the folder and subfolders --> print them
# - check the total size
# - reconize each file extension and files without exention
# - split the files group using extension & print the result
# - recognize empty files --> checkning the size of each file
# - get the relative path of empty file
# - skip the symbilc link
# - 
# Non Functional Reqs:
#  
# - no change to files
# - error mesage for non existant paths
# - error message to path pointing to a file
# - using pathlib
# 
# 
##### How to :
# - detect if the input path is a valid dir  
# - using Path(the path).is_dir()

from pathlib import Path
import os
from webbrowser import get


current_path = os.getenv("test0","")
test_message = os.getenv("TEST_MESSAGE")

def get_user_input() -> str:
  user_input = ""
  while not len(user_input):
     user_input = input("\nPlease provide a valid directory path: ").strip()
     if user_input == "test":
         user_input = current_path
     # print("DEBUG: user_input length:", len(user_input), user_input)
  return user_input

def check_path(path) -> bool: 
    # print("DEBUG: ",path,  Path(path).is_dir()) 
    return Path(path).is_dir()
    

def get_path() -> Path:
    path = "x"
    while not check_path(path):
        path = get_user_input()
    path = Path(path)
    return path

def main():
    print(test_message)
    print("\nWelcome to directory audit tool !!!!")
    path = get_path()
    print("path:", path)
    # 
    
    return









main()