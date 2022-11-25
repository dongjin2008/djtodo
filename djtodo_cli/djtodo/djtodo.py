
import module

module.File.create_file()

def command(argument):
    if argument == "add":
        module.Add()

    if argument == "list" or argument == "ls":
        module.List_All()

    if argument == "remove":
        module.Remove()

    if argument == "done":
        module.Done()
    
    if argument == "search":
        module.Search()
    
    if argument == "tag":
        module.Tag()

def cli(args=None):
    
    if not args:
        argument = ""
        try:
            argument = module.sys.argv[1]
            command(argument)
        except IndexError:
            print("No argument")
            module.sys.exit()
