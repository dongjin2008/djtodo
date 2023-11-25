###############imports###############
import json
import sys
import File

###############Variables###############
test= {}
data = {}
task_removed = []
new_data = []
reloaded_data = []
done_data = []
###############Functions###############

def Get_First_Argument():
    try:
        argument = sys.argv[2]
    except IndexError:
        print("djtodo: empy argument")
        sys.exit()
    else:
        return argument

def Get_Second_Argument():
    try:
        argument = sys.argv[3]
    except IndexError:
        argument = ""
    else:
        return argument

def Json_Read(file):
    with open(file, "r") as f:
        return json.load(f)
        
def Json_Write(file, new_data):
    with open(file, "w") as f:
        json.dump(new_data, f, indent=4)

def List(items):
    print(f'{items["status"]} {items["name"]} {items["task"]} {items["tag"]}')

def Reload_Name():
    dt = Json_Read(File.file)

    for items in dt:
        index = dt.index(items)
        items["name"] = index + 1
        reloaded_data.append(items)
    
    Json_Write(File.file, dt)

def Add():

    task = Get_First_Argument()
    tag = Get_Second_Argument()

    data = {'name': 0,'task': task, 'status': "x", 'tag': tag}
    
    dt = Json_Read(File.file)
    dt.append(data)
        
    Json_Write(File.file, dt)
    Reload_Name()

def List_All():
    dt = Json_Read(File.file)
    for items in dt:
        List(items)

def Remove():
    name = Get_First_Argument()

    dt = Json_Read(File.file)

    for items in dt:
        if items["name"] != int(name):
            new_data.append(items)

    if new_data == dt:
        print("No such task exist!")
    else:
        print(f"task {name} erased")

    Json_Write(File.file, new_data)
    Reload_Name()

def Done():
    status = Get_First_Argument()

    dt = Json_Read(File.file)

    for items in dt:
        if items["name"] == int(status):
            items["status"] = "o"
        done_data.append(items)
    Json_Write(File.file, done_data)

def Search():

    keyword = Get_First_Argument()

    dt = Json_Read(File.file)

    for items in dt:
        if keyword in items["task"]:
            List(items)

def Tag():
    tag = Get_First_Argument()

    dt = Json_Read(File.file)

    for items in dt:
        try:
            if tag in items["tag"]:
                List(items)
        except TypeError:
            pass

