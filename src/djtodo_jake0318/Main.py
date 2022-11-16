import os
from pathlib import Path
import getpass

username = getpass.getuser()
base = Path("/home/{}/.config/".format(username))
folder = Path("{}/djtodo".format(base))
file = Path("{}/djtodo/task.txt".format(base))

if not folder.is_dir():
        os.mkdir(folder)
if not file.is_file(): 
        f = open(file, "w+")


print("""
1. Create new tasks
2. List tasks
3. Quit
""")

# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa   2022/03/18  [x]                 


UI = input("Enter the number: ")


if UI == "1":
    f = open(file, "a")
    while True:
        task = input("Task: ")
        date = input("Due Date(yyyy/mm/dd): ")
        did = False
        f.write("{} {} {}\n".format(task, date, did))
        cnt = input("Create more? [y/N]")
        if cnt.lower() == "y":
            continue
        if cnt.lower() == "n" or cnt == "":
            break

if UI == "2":
    f = open(file, "r")
    x = [line[:-1] for line in f]
    c = []
    for d in x:
        l = d.split(" ")
        if l[2] == "False":
            l[2] = "x"
        else:
            l[2] = "o"
        
        c.append("{}\t{}".format(l[0], l[1]))
        


    
    
        