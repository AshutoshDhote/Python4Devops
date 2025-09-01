import os
def curr_path():
    cwd = os.getcwd()
    print("Current working dir: ", cwd)

curr_path()
os.chdir("/home")
curr_path()

os_name = os.uname().sysname
print(os_name)
print(os.name)