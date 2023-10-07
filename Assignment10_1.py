import os
from sys import *

def list_files_with_extension(directory, file_extension):
    print("We are going to scan directory",directory)
    # Check if the provided directory exists
    flag = os.path.isabs(directory)
    
    if flag == False:
        directory = os.path.abspath(directory)
        
    exist = os.path.isdir(directory)
    
    if exist:
        # Iterate through the files in the directory
        for foldername, subfoldername, filename in os.walk(directory):
            for filen in filename:
                if filen.endswith(file_extension):
                    file_path = os.path.join(foldername, filen)
                    print(file_path)
                
    else:
        print("Error: Directory does not exist.")
        

def main():
    print("Automation Script to List Files with a Specific Extension")
    
    print("Automation script Name is : ",argv[0])
    
    if(argv[1]=="-h" or argv[1]=="-H"):
        print("This Automation Script is used to List Files with a Specific Extension : ")
        exit()
        
    if(argv[1]=="-u" or argv[1]=="-U"):
        print("Usage = DirectoryFileSearch.py")
        print("Example : Demo .txt")
        exit()
        
    if(len(argv)!=3):
        print("invalid Number of Arguments:")
        exit()
        
    try:

    # Call the function to list files with the specified extension
        list_files_with_extension(argv[1], argv[2])
    
    except ValueError:
        print("Error: Invalid datatype of input")
        
    except Exception as E:
        print("Error: Invalid input",E)
        
if __name__ == "__main__":
    main()
