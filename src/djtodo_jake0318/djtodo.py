import sys
import File
from File import file
import pickle
import module

File.create_file()
argument = ""
try:
    argument = sys.argv[1]
except IndexError:
    pass
i = pickle.load(open("VSF.dat", "rb"))


if argument == "add":
    module.add(i)

if argument == "list":
    module.ls()

if argument == "remove":
    module.remove(i)

if argument == "done":
    pass