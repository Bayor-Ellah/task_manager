file = open("tasks.txt", "r")
tasks = file.read().split("\n")
for task in tasks:
    print(f"{tasks.index(task) +1}. {task}")

file = open("tasks.txt", "r")
print(file.read ())