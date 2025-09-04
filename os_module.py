import os

def osname_listdir():

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

#osname_listdir()

# Sort the files in current working directory

def soft_files():
    files_n_dirs = os.listdir('.')
    print (files_n_dirs)

    #VALID FILES CHECK
    files = [item for item in files_n_dirs if os.path.isfile(os.path.join(os.getcwd(),item))]
    print(f'Files: {files}')
    sorted_files = sorted(files)

    #Print one by one
    if sorted_files:
        for f in sorted_files:
            print(f'- {f}')


soft_files()