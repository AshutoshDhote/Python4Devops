import os

#OS name/info
os_info = os.uname()
os_name = os.uname().sysname
print(os_info)
print(os_name)

#Current Working Directory
cwd = os.getcwd()
print("Current working dir: ", cwd)


