import os
from tkinter import *
class PCB:
    def __init__(self):
        self.pid = 0
        self.pstate = 'Ready'
        self.priority = 'High'
        self.point = hex(id(self))
        self.burst_time = 0
        self.arrival_time = 0
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0
        self.start_time = 0

    def getData(self, p_id,prio, bt, at):
        self.pid = p_id
        self.priority = prio
        self.burst_time = bt
        self.arrival_time = at

    def display(self):
        print("--------------------------------------------")
        print(f"The Process ID: {self.pid}")
        print(f"Process State: {self.pstate}")
        print(f"Process Priority: {self.priority}")
        print(f"Process Pointer: {self.point}")
        print("--------------------------------------------")
    def displayAll(self):
        print(f"{self.pid:>5}{self.pstate:>22}{self.priority:>15}{self.point:>24}")

    def change_state(self, state):
        self.pstate = state
    
    def change_priority(self, prior):
            self.priority =  prior
        


def display_table(processes):
    str1 = 'Process ID'
    str2 = 'Process State'
    str3 = 'Process Priority'
    str4 = 'Memory Location'
    if len(processes) > 0:
        print(f"\n{str1}{str2:>20}{str3:>20}{str4:>18}")
        print("----------------------------------------------------------------------------------------------")
        for i in processes:
            i.displayAll()
        
        print("----------------------------------------------------------------------------------------------")
    else:
        print('No processes Found !!!')
        return False
    
def fcfs(process):
    sum_TAT = 0
    sum_WT = 0
    process.sort(key = lambda x : x.arrival_time)
    for i in range(len(process)):
        process[i].start_time = max(process[i].arrival_time, process[i-1].completion_time)
        process[i].completion_time = process[i].start_time + process[i].burst_time
        process[i].turnaround_time = process[i].completion_time - process[i].arrival_time
        process[i].waiting_time = process[i].burst_time - process[i].arrival_time
        if process[i].waiting_time <= 0:
            process[i].waiting_time = 0
        if process[i].turnaround_time <= 0 :
            process[i].turnaround_time = 0
        sum_TAT += process[i].turnaround_time
        sum_WT += process[i].waiting_time

    length_cycle = process[-1].completion_time - process[0].start_time
    avg_turnaround = sum_TAT / len(process)
    avg_waiting = sum_WT / len(process)

    print("__________________________________________________")
    print("P-No.\tPid \tAT\tBT\tCT\tTAT\tWT")
    print("__________________________________________________")
    for i in range(len(process)):
        print(f"{i+1}\t{process[i].pid}\t{process[i].arrival_time}\t{process[i].burst_time}\t{process[i].completion_time}\t{process[i].turnaround_time}\t{process[i].waiting_time}")

    print("\nAverage Waiting Time: ", avg_waiting)
    print("Average Turnaround Time: ", avg_turnaround)
    print("Total Cycle Time: ", length_cycle)
    return process
        
def RoundRobin(processes,quantum):
    n = len(processes)
    process = processes.copy()
    sum_TAT = 0
    sum_WT = 0
    # quantum = 3 
    quantum = int(quantum)
    completion_time = 0
    
    completed = []
    process.sort(key = lambda x : x.arrival_time)
    while len(completed) < n:
        arrived_processes = [p for p in process if p.arrival_time <= completion_time]
        
        if len(arrived_processes) == 0:
            completion_time += quantum
            continue

        current_process = arrived_processes[0]
        
        if current_process.burst_time <= quantum:
            completion_time += current_process.burst_time
            completed.append((current_process, completion_time))
            process.remove(current_process)
        else:
            current_process.burst_time -= quantum
            process.append(current_process)
            process.remove(current_process)
            completion_time += quantum
    
    for i in range(n):
        processes[i].turnaround_time  = completed[i][1] - processes[i].arrival_time
        if processes[i].turnaround_time < 1:
            processes[i].turnaround_time = 0
        processes[i].waiting_time = processes[i].turnaround_time - processes[i].burst_time
        if processes[i].waiting_time < 0:
            processes[i].waiting_time = 0
        processes[i].completion_time = completed[i][1]
        sum_TAT += processes[i].turnaround_time
        sum_WT += processes[i].waiting_time

    avg_turnaround = sum_TAT / n
    avg_waiting = sum_WT / n

    print("__________________________________________________")
    print("P-No.\tPid \tAT\tBT\tCT\tTAT\tWT")
    print("__________________________________________________")
    for i in range(n):
        print(f"{i+1}\t{processes[i].pid}\t{processes[i].arrival_time}\t{processes[i].burst_time}\t{processes[i].completion_time}\t{processes[i].turnaround_time}\t{processes[i].waiting_time}")

    print("\nAverage Waiting Time: ", avg_waiting)
    print("Average Turnaround Time: ", avg_turnaround)
    print("Total Cycle Time: ", completion_time)
    return processes

def LRU_replacement(pages, framesize):
    
    pageFaults = 0
    pageHits = 0
    s = []
    for i in pages:
        if i not in s:
            if(len(s) == framesize):
                s.remove(s[0])
                s.append(i)
    
            else:
                s.append(i)
            pageFaults +=1
        else:
            s.remove(i)
            s.append(i)
            pageHits += 1
    return pageFaults,pageHits

def FIFO_replacement(pages, framesize):
    frames = [0] * framesize
    
    index = 0
    pageHits = 0
    page_faults = 0
    
    for i in range(len(pages)):
        if pages[i] not in frames:
            frames[index] = pages[i]
            index = (index + 1) % framesize
            page_faults += 1
        else:
            pageHits += 1
    return page_faults,pageHits

#   MAIN
processes = []



""""
while run == True: 
    os.system('cls')
    run2 = True
    print(" ______________________________________________________")
    print('|                                                      |')
    print("|                     OS Project                       |")
    print("|______________________________________________________|")
    print('|                                                      |')
    print('|                                                      |')
    print("|          >> Press 1 for Process Management           |")
    print("|          >> Press 2 for Memory Management            |")
    print("|          >> Press 3 for I/O Management               |")
    print("|          >> Press 4 for Other Operations             |")
    print("|          >> Press 5 to Exit.                         |")
    print("|------------------------------------------------------|")

    ch = int(input('  Enter your choice: '))

    if ch == 1:
        while run2 == True:
            os.system('cls')
            print("--------------------------------------------")
            print("        Welcome to Process Management      ")
            print("--------------------------------------------\n")
            print(">> Press 1 to Create a Process.")
            print(">> Press 2 to Terminate a Process.")
            print(">> Press 3 to Execute a Process.")
            print(">> Press 4 to Block a Process.")
            print(">> Press 5 to Resume a Process.")
            print(">> Press 6 to Change the Priority of Process.")
            print(">> Press 7 to Show PCB Table.")
            print("--------------------------------------------")
            print(">> Press 11 for FCFS Process Scheduling")
            print(">> Press 12 for Round Robin Process Scheduling")
            print("--------------------------------------------")
            print(">> Press 0 go back to Main Menu.")
            print("--------------------------------------------\n")
            op = int(input('>> Enter your choice: '))
            os.system('cls')

            # Process Creation
            if op == 1:
                n = int(input('> Enter the number of process you want to create: '))
                for i in range(n):
                    processes.append(PCB())
                    processes[i].getData(pid,"HIGH", 3,5)
                    pid += 1
                os.system('Pause')

            # Process Termination
            elif op == 2:
                if display_table(processes) != False:
                    p_id = int(input("> Enter process id you want to terminate: "))
                    for i in processes:
                        if i.pid == p_id:
                            processes.remove(i)
                            print("> Process Terminated !!!")
                            break
                    else:
                        print('> Process Not Found !!')
                else:
                    pass

                os.system('pause')
            
            #Executing Process
            elif op == 3:
                if display_table(processes) != False:
                    p_id = int(input("> Enter process id you want to Execute: "))
                    for i in processes:
                        if i.pid == p_id:
                            i.change_state('Running')
                            print(f"> Process {i.pid} Now Executing !!!")
                            break
                    else:
                        print('> Process Not Found !!')
                else:
                    pass
                os.system('pause')
            # Block Process
            elif op == 4:
                if display_table(processes) != False:
                    p_id = int(input("> Enter process id you want to Block: "))
                    for i in processes:
                        if i.pid == p_id:
                            i.change_state('Block')
                            print(f"> Process {i.pid} is Now Blocked !!!")
                            break
                    else:
                        print('> Process Not Found !!')
                else:
                    pass
                os.system('pause')
            # Resume Process
            elif op == 5:
                if display_table(processes) != False:
                    p_id = int(input("> Enter process id you want to Resume: "))
                    for i in processes:
                        if i.pid == p_id:
                            i.change_state('Ready')
                            print(f"> Process {i.pid} is now in Ready State !!!")
                            break
                    else:
                        print('> Process Not Found !!')
                else:
                    pass
                os.system('pause')
            # Change Process Priority
            elif op == 6:
                if display_table(processes) != False:
                    p_id = int(input("> Enter process id you want to Change Priority: "))
                    for i in processes:
                        if i.pid == p_id:
                            i.change_priority()
                            break
                    else:
                        print('> Process Not Found !!')
                else:
                    pass
                os.system('pause')
            # Show PCB
            elif op == 7:
                for i in processes:
                    i.display()
                os.system('Pause')

            # First Come First Scheduling
            elif op == 11:
                if len(processes) == 0:
                    print('> No Processes were created !!!\n')
                else:
                    fcfs_list = processes.copy()
                    fcfs(fcfs_list)
                os.system('Pause')

            # Round Robin Scheduling
            elif op == 12:
                if len(processes) == 0:
                    print('> No Processes were created !!!\n')
                else:
                    #rr_list = processes.copy()
                    # completed = RoundRobin(rr_list)
                    pass
                    
                os.system('Pause')

            # GO BACK
            elif op == 0:
                run2 = False


    elif ch == 2:
        pass
    elif ch == 3:
        pass
    elif ch == 4:
        pass
    elif ch == 5:
        run = False
    else:
        print('Invalid Input !!!!')
        """

