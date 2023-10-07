import psutil
from sys import *

def ProcessDisplay(processname):
    # listprocess =[]
    for proc in psutil.process_iter(attrs=['pid','name']):
        try:
            if proc.info['name'] == processname:
                pid = proc.info['pid']
                
                proc_info = psutil.proc(pid)
                # pinfo = proc.as_dict(attrs=['pid','name','username'])
                print(f"Process Name: {processname}")
                print(f"PID: {pid}")
                print(f"Status: {'Running' if proc_info.is_running() else 'Not Running'}")
                print(f"CPU Usage: {proc_info.cpu_percent(interval=1)}%")
                print(f"Memory Usage: {proc_info.memory_info().rss / 1024 / 1024:.2f} MB")
                return

                # listprocess.append(pinfo)
        except(psutil.NoSuchProcess, psutil.AccessDenied,psutil.ZombieProcess):
            pass
    print(f"Process {processname} is not curruntly running")
        
    # return listprocess
        
def main():
    print("Application name:",argv[0])
    
    if len(argv)!=2:
        print("Invalid number of Arguments:")
        exit()
        
    if argv[1] == "-h" or argv[1] == "-H":
        print("Application for showing running process ")
        exit()

    if argv[1] == "-u" or argv[1] == "-U":
        print("Usage: processInfo.py Notepad")
        exit()
    print("Process Monitor: ")
    
    listprocess = ProcessDisplay(argv[1])
    
    # icnt=0
    # for process in listprocess:
    #     icnt+=1
    #     print(process)
    # print("Number of process running are: ",icnt)
    
if __name__ == "__main__":
    main()