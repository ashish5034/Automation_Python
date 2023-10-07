import psutil #python system and process utilitis-it is across platform library for retriving info on running process and system utilization

def ProcessDisplay():
    listprocess = []
    
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            
            listprocess.append(pinfo);
        
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    
    return listprocess

def main():
    print("Marvellous Infosystems : Python Automation & Machine Learning")

    print("Process Monitor")
    
    listprocess = ProcessDisplay()

    icnt = 0
    for elem in listprocess:
        icnt+=1
        print(elem)
    print("Number of running process: ",icnt)
if __name__=="__main__":
    main()