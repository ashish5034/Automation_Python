import os
import shutil
from sys import *

def copy_files_with_extension(source_dir, dest_dir, file_extension):
    
    # Check if the source directory exists
    flag = os.path.isabs(source_dir)
    if flag == False:
        source_dir = os.path.abspath(source_dir)
        
    exist = os.path.isdir(source_dir)
    
    if exist:
        
    # Iterate through the files in the source directory
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                if file.endswith(file_extension):
                    source_path = os.path.join(root, file)
                    dest_path = os.path.join(dest_dir, file)
                    shutil.copy2(source_path, dest_path)
                    print(f"Copied: {source_path} -> {dest_path}")

def main():
    print("Automation Script to Copy Files with a Specific Extension")
    
    print("Application name is :",argv[0])
    
    if(argv[1]=="-h" or argv[1]=="-H"):
        print("Automation Script to Rename Files by Extension")
        exit()
        
    if(argv[1]=="-u" or argv[1] == "-U"):
        print("Usage:DirectoryCopyExt.py")
        print("Demo Temp .exe")
        exit()
      
    if(len(argv) != 4):
        print("Invalid number of argument")
        exit()  
    
    try:
        copy_files_with_extension(argv[1],argv[2],argv[3])
        
    except ValueError:
        print("Error:Invalid Input:")
        
    except Exception as E:
        print("Error: Invalid input",E)
    

if __name__ == "__main__":
    main()
