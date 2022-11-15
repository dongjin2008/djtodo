import os
from pathlib import Path
import getpass

print("""
1. Create new tasks
2. List tasks
3. Quit
""")

UI = input("Enter the number: ")

username = getpass.getuser()
base = Path("/home/{}/.config/".format(username))
folder = Path("{}djtodo".format(base))
file = Path("{}djtodo/task.txt".format(base))

if not folder.is_dir():
        os.mkdir(folder)
        if not file.is_file(): 
            f = open(file, "w+")
        else:
            f = open(file, "a")

if UI == 1:
    task = input("Task: ")
    date = input("Due Date(yyyy/mm/dd): ")
    did = False
    f.write("{} {} {}".format(task, date, did))
