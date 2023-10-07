from sys import *
import os
import time

def DirectoryTravel(DirName):
    print("We are going to Scan Directory: ",DirName)

    for foldername, subfoldername, filename in os.walk(DirName):
        print("Current directory name: ",foldername)
        
# It iterates through the subdirectories in the specified directory and prints their names.
        for subname in subfoldername:
            print("Subfoldername: ",subname)
            
# It iterates through the files in the specified directory, prints their names, and uses os.path.getsize() to display the file size in bytes.
        for fname in filename:
            print("File Name Is: ",fname)
            # print(os.path.getsize(fname))
            print(fname, " : ",os.path.getsize(foldername+"/"+fname),"bytes")
            

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