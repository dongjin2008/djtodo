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

i = pickle.load(open("VSF.dat", "rb"))
print(i)
        
if argument == "add":
    task = sys.argv[2]
    due_date = sys.argv[3]
    data[i] = {'task': task, 'due_date': due_date, 'status': False}
    i += 1
    pickle.dump(i, open("VSF.dat", "wb"))
    with open(File.file, "a") as f:
        json.dump(data, f)
        