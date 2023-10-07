# The updated script you provided includes additional checks to ensure that the directory path is valid and converts the given directory path to an absolute path before performing the directory traversal and file listing. Here's a breakdown of how it works

from sys import * # the sys module to access command-line arguments,
import os #the os module to work with the file system,
import time  #the time module to measure execution time.

# It defines a function DirectoryTravel(DirName) that takes a directory path (DirName) as an argument and scans and lists the contents of that directory and its subdirectories.

def DirectoryTravel(DirName):
    print("We are going to Scan Directory: ",DirName)
# checks if the provided directory path is absolute using os.path.isabs(),
    flag = os.path.isabs(DirName)   #isabs = is Absolute
# converts it to an absolute path using os.path.abspath() if it's not already absolute.
    if flag == False:
        DirName = os.path.abspath(DirName)  #abspath = Absolute path
# It then checks if the directory exists using os.path.isdir().
    exist = os.path.isdir(DirName)
# If it exists, it calls the DirectoryTravel function with the directory name provided as the second argument and measures the end time.
    if exist:
        for foldername, subfoldername, filename in os.walk(DirName):
            print("Current directory name: ",foldername)
            

            for subname in subfoldername:
                print("Subfolder Name: ",subname)

            for fname in filename:
                print(os.path.abspath(fname))
                # print(os.path.getsize(fname))
                # print(fname, " : ",os.path.getsize(foldername+"/"+fname),"bytes")

    else:
        print("Invalid Path:")           

def main():
    print("------------Automation Script------------")
    
    print("Automation Script name : ",argv[0])

    if (len(argv) != 2):
        print("Invalid Number of Arguments")
        exit()

    if(argv[1] == "-h" or argv[1]=="-H"):  #flag for displaying help
        print("The automation script is used to perform File Automations")
        exit()

    elif(argv[1] == "-u" or argv[1] == "-U"):  #flag for displaying usage of script
        print("Usage : Name_of_script First_Argument")
        print("Example: Demo.py Marvellous")
        exit()

    else:
        startime = time.time()
        #logic
        DirectoryTravel(argv[1])
        endtime = time.time()

        print("The script took time to execute as : ",endtime-startime)
            
if __name__ == "__main__":
    main()