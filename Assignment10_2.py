import os
from sys import *

def rename_files_with_extension(directory, old_extension, new_extension):
    
    print("We are going to scan directory: ",directory)
    
    flag = os.path.isabs(directory)
    
    if flag == False:
        directory = os.path.abspath(directory)
        
    exist = os.path.isdir(directory)
    
    # Check if the provided directory exists
    if exist:
        

    # Iterate through the files in the directory
        for foldername, subfoldername, files in os.walk(directory):
            for file in files:
                if file.endswith(old_extension):
                    old_path = os.path.join(foldername, file)
                    new_file = file.replace(old_extension, new_extension)
                    new_path = os.path.join(foldername, new_file)
                    os.rename(old_path, new_path)
                    print(f"Renamed: {old_path} -> {new_path}")

    else:
        print("Error: Directory does not exist.")
        

def main():
    print("Automation Script to Rename Files by Extension")
    print("Application name is :",argv[0])
    
    if(argv[1]=="-h" or argv[1]=="-H"):
        print("Automation Script to Rename Files by Extension")
        exit()
        
    if(argv[1]=="-u" or argv[1] == "-U"):
        print("Usage:DirectoryName.py")
        print("Demo .txt .py")
        exit()
      
    if(len(argv) != 4):
        print("Invalid number of argument")
        exit()  
    
    try:
        rename_files_with_extension(argv[1],argv[2], argv[3])
        
    except ValueError:
        print("Error:Invalid Input:")
        
    except Exception as E:
        print("Error: Invalid input",E)
        
if __name__ == "__main__":
    main()
