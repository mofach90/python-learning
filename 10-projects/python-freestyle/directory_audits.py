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
# - 
# Non Functional Reqs:
# - skip the symbilc link 
# - no change to files
# - error mesage for non existant paths
# - error message to path pointing to a file
# - using pathlib
# 
# 
##### How to :
# - detect if the input path is a valid dir and bot a file 
# - using Path(the path).is_dir()




def get_user_input() -> str:
  user_input = ""
  while not len(user_input):
     user_input = input("\nPlease provide a valid directory path: ").strip()
     print("DEBUG: user_input length:", len(user_input), user_input)
  return user_input
    



def main():
    print("\nWelcome to directory audit tool !!!!")
    get_user_input()


    
    return









main()