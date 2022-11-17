import sys
import File
import json
from File import file
import pickle

File.create_file()
argument = ""
try:
    argument = sys.argv[1]
except IndexError:
    pass
test= {}
data = {}
task_removed = []
new_data = []


i = pickle.load(open("VSF.dat", "rb"))


def add(i):
    try:
        task = sys.argv[2]
    except IndexError:
        print("djtodo: empy argument")
        sys.exit()

    
    data = {'name': i,'task': task, 'status': False}
    
    i += 1
    pickle.dump(i, open("VSF.dat", "wb"))
    with open(File.file, "+r") as f:
        dt = json.load(f)
        dt.append(data)
        f.seek(0)
        json.dump(dt, f, indent=4)
if argument == "add":
    add(i)
    


def ls():
    with open(File.file, "r", encoding='utf-8') as f:
        dt = json.load(f)
        for items in dt:
            if items["status"] == 0:
                flag = "x"
                print("{} {} {}".format(flag, items["name"], items["task"]))
            else:
                flag = "o"
                print("{} {} {}".format(flag, items["name"], items["task"]))

if argument == "list":
    ls()

if argument == "remove":
    try:
        name = sys.argv[2]
    except IndexError:
        print("djtodo: empy argument")
        sys.exit()
    
    with open(File.file, "r") as f:
        dt = json.load(f)

    for items in dt:
        if items["name"] != int(name):
            new_data.append(items)
            index = new_data.index(items)
            new_data[index]["name"] = index + 1 
            i = index+2
            pickle.dump(i, open("VSF.dat", "wb"))
    
    with open(File.file, "w") as f:
        json.dump(new_data, f, indent= 4)

        

        


if argument == "toggle":
    pass