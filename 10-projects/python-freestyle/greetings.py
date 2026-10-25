

name = input("what is your name bro ? ")
age = input(f"what is your age {name} ? ")
while not age.isdigit():
    age = input(f"You must put a valid age {name}:")

lengh_Name = len(name)
print("hey whats up:", name)
print("you have", lengh_Name, "letters in your name", name)
new_age = int(age) + 1
print("next year your age gonna be:", new_age)
