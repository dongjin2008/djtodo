import os
from pathlib import Path
import getpass
import shutil

username = getpass.getuser()
base = Path(f"/home/{username}/.config/")
folder = Path(f"{base}/djtodo")
file = Path(f"{base}/djtodo/task.json")

def create_file():
    if not folder.is_dir():
            os.mkdir(folder)
    if not file.is_file(): 
            shutil.copy('task.json', file)
    


