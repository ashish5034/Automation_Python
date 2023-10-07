import os
import time
from sys import *
from tkinter.ttk import Separator
import psutil

def processDisplay(log_dir = "Marvellous"):
    listprocess = []

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    Separator = "-" * 80
    log_path = os.path.join(log_dir,"MarvellousLog%s.log"%(time.time))
    f=open(log_path,'w')
    f.write(Separator+ "\n")
    f.write("Marvellous Infosystem Process Logger: "+time.time() + "\n")
    f.write(Separator + "\n")

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            pinfo['vms'] = proc.memory_info().vms/(1024*1024)
            pinfo['vms']= vms    #virtual machiene system
            listprocess.append(pinfo)

        except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    for element in listprocess:
        f.write("%s\n"%element)

def main():
    print("Python Automation and Machine Learning")
    print("Application Name: "+argv[0])

    if(len(argv)!=2):
        print("Error: Invalid Number of argument")
        exit()

    if(argv[1]=="-h")or(argv[1]=="-H"):
        print("This script is used log record of running processes")
        exit()

    if(argv[1]=="-u")or(argv[1]=="-U"):
        print("Usage: ApplicationName AbsolutePath_of_Directory")
        exit()

    try:
        processDisplay(argv[1])

    except ValueError:
        print("Error: Invalid datatype of input")

    except Exception:
        print("Error: Invalid Input")

if __name__=="__main__":
    main()