import os

#OS name/info
os_info = os.uname()
os_name = os.uname().sysname
print(f'OS Info: {os_info}')
print(f'OS Name: {os_name}')

#Current Working Directory
cwd = os.getcwd()
print("Current working dir: ", cwd)

#List Files/Directories
print(os.listdir('.'))
print("list of files/folders in cwd:", os.listdir(cwd))

# Check if File exist or not?
try:
    filename = 'abc.txt'
    f = open(filename, 'r')
    text = f.read()
    f.close()
except IOError as e:
    print(f"Not accessed or problem in reading:" + filename +"\n", {e})

