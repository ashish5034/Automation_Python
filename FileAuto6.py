from sys import *
import os
import time

def DirectoryTravel(DirName1, DirName2):
    print("We are going to Scan the Directory : ",DirName1)

    flag = os.path.isabs(DirName1)

    if flag == False:
        DirName1 = os.path.abspath(DirName1)

    exist = os.path.isdir(DirName1)

    if (exist == True):
        for foldername, subfoldername, filename in os.walk(DirName1):
            for fname in filename:
                print(fname, " : ", os.path.getsize(os.path.join(foldername,fname)), " bytes")
                if(fname == DirName2):
                    print("File is Present in the directory with name: ",fname)
                    return
    else:
        print("Invalid path")

def main():
    print("-------------- Automation Script --------------")

    print("Automation Script Name : ",argv[0])

    if(argv[1] == "-h" or argv[1] == "-H"):    # Flag for displaying help
        print("This automation script is used to perform File Automations")
        exit()
    
    elif(argv[1] == "-u" or argv[1] == "-U"):    # Flag for displaying the usage of script
        print("Usage : Name_Of_Script First_Argument Second_Argument")
        print("Example : Demo.py Marvellous Demo.txt")
        exit()

    if(len(argv) != 3):
        print("Invalid number of arguments")
        exit()

    
    else:
        starttime = time.time()
        DirectoryTravel(argv[1], argv[2])
        endtime = time.time()

        print("The script took time to execute as : ",endtime-starttime)

if __name__ == "__main__":
    main()

# python FileAutomation.py Directory_Name And FileNAme