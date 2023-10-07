from sys import *
import os

def DirectoryTravel(DirName):
    print("We are going to Scan Directory: ",DirName)

    for foldername, subfoldername, filename in os.walk(DirName):
        print("Current directory name: ",foldername)

        for subname in subfoldername:
            print("Subfoldername: ",subname)
            
        for fname in filename:
            print("File name is :",fname)

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
        
        DirectoryTravel(argv[1])
            
if __name__ == "__main__":
    main()