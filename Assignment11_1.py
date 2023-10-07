import os
import hashlib
from sys import *

def hashfile(path, blocksize = 1024):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()

def DisplayCheckSum(path):
    print("we are goinng to display checksum of file :")
    
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)
        
    exists = os.path.isdir(path)
    
    if exists:
        for dirName, subDir, fileList in os.walk(path):
            print("Current folder is : ",dirName)
            
            icount=1
            
            for filen in fileList:
                
                path = os.path.join(dirName,filen)
                file_hash = hashfile(path)
                print(path)
                print(file_hash)
                print(' ')
                icount+=1
            print(icount)   
    else:
        print("Invalid Path")

def main():
    
    print("Automation script name is : ",argv[0])
    
    if(argv[1]=="-h" or argv[1] == "-H"):
        print("This script is used to traverse specific directory and display checksum of files")
        exit()
        
    if(argv[1]=="-u" or argv[1]=="-U"):
        print("Usage: DirectoryChecksum.py")
        print("Demo")
        exit()
        
    if(len(argv) != 2):
        print("Error: Invalid Number of Argument")
        exit()
    
    try:
        DisplayCheckSum(argv[1])
        
    except ValueError:
        print("Error: Invalid datatype of input")
        
    except Exception as e:
        print("Error: Invalid Path")
        
if __name__ == "__main__":
    main()
