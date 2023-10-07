# from distutils.filelist import FileList
# from genericpath import exists
from sys import *
import os
import hashlib
# from unittest import result

def hashfile(path, blocksize = 1024):
    fd = open(path, 'rb')
    hasher = hashlib.md5()
    buf = fd.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf = fd.read(blocksize)
    fd.close()
    return hasher.hexdigest()
# The FindDuplicate function is defined, which takes a directory path as an argument. It traverses through the directory and its subdirectories using os.walk() and calculates the MD5 checksum for each file it encounters. It maintains a dictionary (dups) where the MD5 hash is the key, and the list of filenames with that hash is the value.
def FindDuplicate(path):
    flag = os.path.isabs(path)

    if flag==False:
        path=os.path.abspath(path)

    exists=os.path.isdir(path)

    dups={}

    if exists:
        for dirName, subdir, FileList in os.walk(path):
            for filen in FileList:
                path = os.path.join(dirName,filen)
                file_hash = hashfile(path)
                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]
        return dups
    else:
        print("Invalid Path")   
# The PrintDuplicate function takes the dictionary of duplicate files (dict1) as an argument, and it filters the dictionary to find duplicate MD5 hashes (more than one filename with the same hash). It then prints the duplicate filenames.
def PrintDuplicate(dict1):

    results = list(filter(lambda x: len(x)>1, dict1.values()))   

    if len(results)>0:
        print("Duplicate found:")   

        print("the following files are identical:")  

        icnt = 0
        for result in results:
            for subresult in result:
                icnt+=1
                if icnt >= 2:
                    print("\t\t%s"%subresult)

        else:
            print("No duplicate files found")           

def main():
   
    print("Application name : " +argv[0])

    if (len(argv) != 2):
        print("Error : Invalid number of arguments")
        exit()
    
    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to traverse specific directory and display checksum of files")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName AbsolutePath_of_Directory Extention")
        exit()

    try:
        arr = {}
        arr = FindDuplicate(argv[1])
        PrintDuplicate(arr)

    except ValueError:
        print("Error : Invalid datatype of input")

if __name__ == "__main__":
    main()
