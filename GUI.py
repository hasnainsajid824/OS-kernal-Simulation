
import ttkbootstrap as btk
from tkinter import *
from tkinter import ttk
from ttkbootstrap.widgets import Combobox
from OSProject import *


TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 11"
FONT_BOLD = "Helvetica 13 bold"

class OS:
    def __init__(self):
        self.root = btk.Window(themename="superhero")
        self.root.title("Operating System")
        self.s = ttk.Style()
        self.s.theme_use('default')
        self.s.configure('Treeview', background="green3",foreground='black')
        self.root.resizable(width=False, height=False)
        self.root.configure(width=470, height=500)
        self.main_window()
        self.root.mainloop()
    def close(self):
        self.root.destroy()

    def popup(self):
            win = Toplevel()
            win.wm_title("Error")

            l = Label(win, text="No Process was created", fg=TEXT_COLOR)
            l.grid(row=0, column=0)

            b = Button(win, text="Okay", fg=TEXT_COLOR, command=win.destroy)
            b.grid(row=1, column=0)
    def block_popup(self):
        win = Toplevel()
        win.wm_title("Error")

        l = Label(win, text="No Such Process Exist", fg=TEXT_COLOR)
        l.grid(row=0, column=0)
        b = Button(win, text="Okay", fg=TEXT_COLOR, command=win.destroy)
        b.grid(row=1, column=0)
    def noblock_popup(self):
        self.win = Toplevel(self.root)
        self.win.wm_title("Error")

        l = Label(self.win, text="No Process were Blocked", fg=TEXT_COLOR)
        l.grid(row=0, column=0)
        b = Button(self.win, text="Okay", fg=TEXT_COLOR, command=self.process_management)
        b.grid(row=1, column=0)

    def get_quantum(self):
        win = Toplevel()
        win.wm_title("Time Quantum")
        win.configure(width=300, height= 200)
        l1 = Label(win, text="Enter Time Quantum: ",font="Helvetica 14 bold" ,fg=TEXT_COLOR)
        l1.place(relx=0.1,rely=0.2, relwidth=0.8)
        self.time_quantum = Entry(win, font=FONT)
        self.time_quantum.place(relx=0.12,rely=0.51, relwidth=0.7)
        b = Button(win, text="Submit", fg=TEXT_COLOR, command=self.rr)
        b.place(relx=0.38,rely=0.75,relwidth=0.15, relheight= 0.2)

    def main_window(self):
        for i in self.root.winfo_children():
            i.destroy()
        # head label
        head_label = Label(self.root,  fg=TEXT_COLOR,
                           text="Welcome to Operating System", font="Helvetica 14 bold", pady=10)
        head_label.place(relwidth=1)
        
        # tiny divider
        line = Label(self.root, width=450)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        # buttons

        process_btn = Button(self.root,text="Process Managemet", font="Helvetica 15 bold", width=20, command=self.process_management)
        process_btn.place(relx= 0.24, rely=0.23)

        Memory_btn = Button(self.root,text="Memory Managemet", font="Helvetica 15 bold", width=20, command=self.memory_management)
        Memory_btn.place(relx= 0.24, rely=0.37)

        schedule_btn = Button(self.root,text="Process Scheduling", font="Helvetica 15 bold", width=20, command=self.process_scheduling)
        schedule_btn.place(relx= 0.24, rely=0.53)

        PCB_btn = Button(self.root,text="Process Control Block", font="Helvetica 15 bold", width=20, command=self.process_control_block)
        PCB_btn.place(relx= 0.24, rely=0.68)

        exit_btn = Button(self.root,text="Exit", font="Helvetica 15 bold", width=20, command=self.close)
        exit_btn.place(relx= 0.24, rely=0.85)


#----------------Process Management-------------------------



    def process_management(self):
        for i in self.root.winfo_children():
            i.destroy()
        # head label
        head_label = Label(self.root,  fg=TEXT_COLOR,
                           text="Process Management", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)
        
        # tiny divider
        line = Label(self.root, width=450)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        # buttons
        create_btn = Button(self.root,text="Create a Process", font=FONT_BOLD, width=20, command=self.create_process)
        create_btn.place(relx= 0.27, rely=0.18)

        destroy_btn = Button(self.root,text="Terminate a Process", font=FONT_BOLD, width=20, command=self.terminate_process)
        destroy_btn.place(relx= 0.27, rely=0.27)

        run_btn = Button(self.root,text="Execute a Process", font=FONT_BOLD, width=20, command=self.run_process)
        run_btn.place(relx= 0.27, rely=0.36)

        block_btn = Button(self.root,text="Block a Process", font=FONT_BOLD, width=20, command=self.block_process)
        block_btn.place(relx= 0.27, rely=0.45)

        resume_btn = Button(self.root,text="Resume a Process", font=FONT_BOLD, width=20, command=self.resume_process)
        resume_btn.place(relx= 0.27, rely=0.54)

        priority_btn = Button(self.root,text="Change the Priority", font=FONT_BOLD, width=20,command=self.priority_change)
        priority_btn.place(relx= 0.27, rely=0.63)

        dispatch_btn = Button(self.root,text="Dispatch a Process", font=FONT_BOLD, width=20)
        dispatch_btn.place(relx= 0.27, rely=0.72)
        
        back_btn = Button(self.root,text="Back", font=FONT_BOLD, width=10, command=self.main_window)
        back_btn.place(relx= 0.27, rely=0.81)

    # Create a Process
    def create_process(self):
        for i in self.root.winfo_children():
            i.destroy()
        # head label
        head_label = Label(self.root,  fg=TEXT_COLOR,
                           text="Create A Process", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)

        # tiny divider
        line = Label(self.root, width=450)
        line.place(relwidth=1, rely=0.07, relheight=0.002)
        
        # Create a frame for inputting process ID
        
        pid_label = Label(self.root, text="Enter Process ID: ",  fg=TEXT_COLOR,font=FONT_BOLD, pady=10)
        self.pid_entry = Entry(self.root, font=FONT)
        self.pid_entry.focus()
        pid_label.place(relx=0.1, rely=0.21)
        self.pid_entry.place(relx=0.43, rely=0.24,relwidth=0.15, relheight= 0.03)
        # Create a frame for selecting priority
        priority_label = Label(self.root, text="Select Process Priority: ",  fg=TEXT_COLOR,font=FONT_BOLD, pady=10)
        
        self.priority_dropdown = Combobox(self.root, values=["High","Medium","Low"], state="readonly")
        self.priority_dropdown.current(0)
        priority_label.place(relx=0.1, rely=0.33)
        self.priority_dropdown.place(relx=0.52, rely= 0.34, relheight= 0.05)
        # Create a frame for inputting burst time and arrival time
        
        burst_label = Label(self.root , text="Enter Process Burst Time: ",  fg=TEXT_COLOR,font=FONT_BOLD, pady=10)
        self.burst_entry = Entry(self.root, font=FONT)
        arrival_label = Label(self.root, text="Enter Process Arrival Time: ",  fg=TEXT_COLOR,font=FONT_BOLD, pady=10)
        self.arrival_entry = Entry(self.root, font=FONT)
        
        burst_label.place(relx=0.1, rely=0.44)
        self.burst_entry.place(relx=0.6, rely=0.47,relwidth=0.15, relheight= 0.03)
        arrival_label.place(relx=0.1, rely=0.54)
        self.arrival_entry.place(relx=0.6, rely=0.57 ,relwidth=0.15, relheight= 0.03)

        # Create a submit button
        submit_button = Button(self.root, text="Submit",font=FONT_BOLD, width=10, command=self.process_submit)
        submit_button.place(relx= 0.34, rely=0.74)
       

    def process_submit(self):
        p = PCB()
        pid = self.pid_entry.get()
        prio = self.priority_dropdown.get()
        burst_time = self.burst_entry.get()
        arrival_time = self.arrival_entry.get()
        p.getData(pid, prio, int(burst_time), int(arrival_time))
        processes.append(p)
        self.process_management()

    def terminate_process(self):
        if len(processes) != 0:
            for i in self.root.winfo_children():
                i.destroy()
            # head label
            head_label = Label(self.root,  fg=TEXT_COLOR,
                                text="Terminate Process", font=FONT_BOLD, pady=10)
            head_label.place(relwidth=1)
            
            frame = Frame(self.root)
            frame.place(relwidth=1, rely=0.1, relheight=0.650)

            # Create a scrollbar for the frame
            vscrollbar = Scrollbar(frame, orient=VERTICAL)
            vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
            # Create the treeview
            tree = ttk.Treeview(frame, columns=("PID", "State", "Priority", "Pointer"), show="headings", yscrollcommand=vscrollbar.set)
            tree.heading("PID", text="PID")
            tree.heading("State", text="State")
            tree.heading("Priority", text="Prority")
            tree.heading("Pointer", text="Pointer")
            tree.column("PID", width=50, anchor='center')
            tree.column("State", width=50, anchor='center')
            tree.column("Priority", width=50, anchor='center')
            tree.column("Pointer", width=50, anchor='center')

            # Add the processes to the treeview
            for i in range(len(processes)):
                tree.insert("", END, values=(processes[i].pid, processes[i].pstate, processes[i].priority, processes[i].point))

            # Add the treeview to the frame
            tree.pack(fill=BOTH, expand=YES)

            # Configure the scrollbar
            vscrollbar.config(command=tree.yview)

            pid_label = Label(self.root, text="Enter Process ID: ",  fg=TEXT_COLOR,font=FONT_BOLD, pady=10)
            self.pid_terminate = Entry(self.root, font=FONT)
            self.pid_terminate.focus()
            pid_label.place(relx=0.1, rely=0.81)
            self.pid_terminate.place(relx=0.43, rely=0.84,relwidth=0.15, relheight= 0.03)

            sub_btn = Button(self.root,text="Terminate", font=FONT_BOLD, width=10, command=self.terminate_submit)
            sub_btn.place(relx= 0.27, rely=0.90)
        else:
            self.popup()

    def terminate_submit(self):
        p_id = self.pid_terminate.get()
        for i in processes:
            if i.pid == p_id:
                processes.remove(i)
                break
        else:
            self.block_popup()
        self.main_window()
    
    def block_process(self):
        if len(processes) != 0:
            for i in self.root.winfo_children():
                i.destroy()
            # head label
            head_label = Label(self.root,  fg=TEXT_COLOR,
                                text="Block Process", font=FONT_BOLD, pady=10)
            head_label.place(relwidth=1)
            
            frame = Frame(self.root)
            frame.place(relwidth=1, rely=0.1, relheight=0.650)

            # Create a scrollbar for the frame
            vscrollbar = Scrollbar(frame, orient=VERTICAL)
            vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
            # Create the treeview
            tree = ttk.Treeview(frame, columns=("PID", "State", "Priority", "Pointer"), show="headings", yscrollcommand=vscrollbar.set)
            tree.heading("PID", text="PID")
            tree.heading("State", text="State")
            tree.heading("Priority", text="Prority")
            tree.heading("Pointer", text="Pointer")
            tree.column("PID", width=50, anchor='center')
            tree.column("State", width=50, anchor='center')
            tree.column("Priority", width=50, anchor='center')
            tree.column("Pointer", width=50, anchor='center')

            # Add the processes to the treeview
            for i in range(len(processes)):
                tree.insert("", END, values=(processes[i].pid, processes[i].pstate, processes[i].priority, processes[i].point))

            # Add the treeview to the frame
            tree.pack(fill=BOTH, expand=YES)

            # Configure the scrollbar
            vscrollbar.config(command=tree.yview)

            pid_label = Label(self.root, text="Enter Process ID: ",  fg=TEXT_COLOR,font=FONT_BOLD, pady=10)
            self.pid_block = Entry(self.root, font=FONT)
            self.pid_block.focus()
            pid_label.place(relx=0.1, rely=0.81)
            self.pid_block.place(relx=0.43, rely=0.84,relwidth=0.15, relheight= 0.03)

            sub_btn = Button(self.root,text="Block", font=FONT_BOLD, width=10, command=self.block_submit)
            sub_btn.place(relx= 0.27, rely=0.90)
        else:
            self.popup()

    def block_submit(self):
        p_id = self.pid_block.get()
        for i in processes:
            if i.pid == p_id:
                i.change_state('Block')
                break
        else:
            self.block_popup()
        self.main_window()

    def run_process(self):
        if len(processes) != 0:
            for i in self.root.winfo_children():
                i.destroy()
            # head label
            head_label = Label(self.root,  fg=TEXT_COLOR,
                                text="Execute Process", font=FONT_BOLD, pady=10)
            head_label.place(relwidth=1)
            
            frame = Frame(self.root)
            frame.place(relwidth=1, rely=0.1, relheight=0.650)

            # Create a scrollbar for the frame
            vscrollbar = Scrollbar(frame, orient=VERTICAL)
            vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
            # Create the treeview
            tree = ttk.Treeview(frame, columns=("PID", "State", "Priority", "Pointer"), show="headings", yscrollcommand=vscrollbar.set)
            tree.heading("PID", text="PID")
            tree.heading("State", text="State")
            tree.heading("Priority", text="Prority")
            tree.heading("Pointer", text="Pointer")
            tree.column("PID", width=50, anchor='center')
            tree.column("State", width=50, anchor='center')
            tree.column("Priority", width=50, anchor='center')
            tree.column("Pointer", width=50, anchor='center')

            # Add the processes to the treeview
            for i in range(len(processes)):
                tree.insert("", END, values=(processes[i].pid, processes[i].pstate, processes[i].priority, processes[i].point))

            # Add the treeview to the frame
            tree.pack(fill=BOTH, expand=YES)

            # Configure the scrollbar
            vscrollbar.config(command=tree.yview)

            pid_label = Label(self.root, text="Enter Process ID: ",  fg=TEXT_COLOR,font=FONT_BOLD, pady=10)
            self.pid_run = Entry(self.root, font=FONT)
            self.pid_run.focus()
            pid_label.place(relx=0.1, rely=0.81)
            self.pid_run.place(relx=0.43, rely=0.84,relwidth=0.15, relheight= 0.03)

            sub_btn = Button(self.root,text="Execute", font=FONT_BOLD, width=10, command=self.run_submit)
            sub_btn.place(relx= 0.27, rely=0.90)
        else:
            self.popup()

    def run_submit(self):
        p_id = self.pid_run.get()
        for i in processes:
            if i.pid == p_id:
                i.change_state('Running')
                break
        else:
            self.block_popup()
        self.main_window()
    
    
    def resume_process(self):
        if len(processes) != 0:
            for i in self.root.winfo_children():
                i.destroy()
            # head label
            head_label = Label(self.root,  fg=TEXT_COLOR,
                                text="Resume Process", font=FONT_BOLD, pady=10)
            head_label.place(relwidth=1)
            
            frame = Frame(self.root)
            frame.place(relwidth=1, rely=0.1, relheight=0.650)

            # Create a scrollbar for the frame
            vscrollbar = Scrollbar(frame, orient=VERTICAL)
            vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
            # Create the treeview
            tree = ttk.Treeview(frame, columns=("PID", "State", "Priority", "Pointer"), show="headings", yscrollcommand=vscrollbar.set)
            tree.heading("PID", text="PID")
            tree.heading("State", text="State")
            tree.heading("Priority", text="Prority")
            tree.heading("Pointer", text="Pointer")
            tree.column("PID", width=50, anchor='center')
            tree.column("State", width=50, anchor='center')
            tree.column("Priority", width=50, anchor='center')
            tree.column("Pointer", width=50, anchor='center')
            block = False
            # Add the processes to the treeview
            for i in range(len(processes)):
                if processes[i].pstate == 'Block':
                    block = True
                    tree.insert("", END, values=(processes[i].pid, processes[i].pstate, processes[i].priority, processes[i].point))
            if block == False:
                self.noblock_popup()
            # Add the treeview to the frame
            tree.pack(fill=BOTH, expand=YES)

            # Configure the scrollbar
            vscrollbar.config(command=tree.yview)

            pid_label = Label(self.root, text="Enter Process ID: ",  fg=TEXT_COLOR,font=FONT_BOLD, pady=10)
            self.pid_resume = Entry(self.root, font=FONT)
            self.pid_resume.focus()
            pid_label.place(relx=0.1, rely=0.81)
            self.pid_resume.place(relx=0.43, rely=0.84,relwidth=0.15, relheight= 0.03)

            sub_btn = Button(self.root,text="Resume", font=FONT_BOLD, width=10, command=self.resume_submit)
            sub_btn.place(relx= 0.37, rely=0.90)
        else:
            self.popup()
    
    def resume_submit(self):
        p_id = self.pid_resume.get()
        for i in processes:
            if i.pid == p_id:
                i.change_state('Ready')
                break
        else:
            self.block_popup()
        self.main_window()


    def priority_change(self):
        if len(processes) != 0:
            for i in self.root.winfo_children():
                i.destroy()
            # head label
            head_label = Label(self.root,  fg=TEXT_COLOR,
                                text="Change Process Priority", font=FONT_BOLD, pady=10)
            head_label.place(relwidth=1)
            
            frame = Frame(self.root)
            frame.place(relwidth=1, rely=0.1, relheight=0.650)

            # Create a scrollbar for the frame
            vscrollbar = Scrollbar(frame, orient=VERTICAL)
            vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
            # Create the treeview
            tree = ttk.Treeview(frame, columns=("PID", "State", "Priority", "Pointer"), show="headings", yscrollcommand=vscrollbar.set)
            tree.heading("PID", text="PID")
            tree.heading("State", text="State")
            tree.heading("Priority", text="Prority")
            tree.heading("Pointer", text="Pointer")
            tree.column("PID", width=50, anchor='center')
            tree.column("State", width=50, anchor='center')
            tree.column("Priority", width=50, anchor='center')
            tree.column("Pointer", width=50, anchor='center')

            # Add the processes to the treeview
            for i in range(len(processes)):
                    tree.insert("", END, values=(processes[i].pid, processes[i].pstate, processes[i].priority, processes[i].point))
            # Add the treeview to the frame
            tree.pack(fill=BOTH, expand=YES)

            # Configure the scrollbar
            vscrollbar.config(command=tree.yview)

            pid_label = Label(self.root, text="Enter Process ID: ",  fg=TEXT_COLOR,font=FONT_BOLD, pady=10)
            self.pid_priority = Entry(self.root, font=FONT)
            self.pid_priority.focus()
            pid_label.place(relx=0.1, rely=0.75)
            self.pid_priority.place(relx=0.43, rely=0.78,relwidth=0.15, relheight= 0.03)

            priority_label = Label(self.root, text="Select Process Priority: ",  fg=TEXT_COLOR,font=FONT_BOLD, pady=10)
            self.change_priority = Combobox(self.root, values=["High","Medium","Low"], state="readonly")
            self.change_priority.current(0)
            priority_label.place(relx=0.1, rely=0.83)
            self.change_priority.place(relx=0.52, rely= 0.86, relheight= 0.05)

            sub_btn = Button(self.root,text="Change", font=FONT_BOLD, width=10, command=self.priority_submit)
            sub_btn.place(relx= 0.37, rely=0.92)
        else:
            self.popup()
    

    def priority_submit(self):
        p_id = self.pid_priority.get()
        priority = self.change_priority.get()
        change = False
        for i in processes:
            if i.pid == p_id:
                change = True
                i.change_priority(priority)
                break
        if change == False:
            self.block_popup()
        self.main_window()
        



#----------------------------MEMORY MANAGEMENT---------------------------------


    def memory_management(self):
        for i in self.root.winfo_children():
            i.destroy()
        # head label
        head_label = Label(self.root,  fg=TEXT_COLOR,
                            text="Memory Management", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)
        
        # tiny divider
        line = Label(self.root, width=450)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        # buttons
        paging_btn = Button(self.root,text="Paging", font=FONT_BOLD, width=20)
        paging_btn.place(relx= 0.27, rely=0.28)

        lru_btn = Button(self.root,text="LRU Page Replacement", font=FONT_BOLD, width=20, command=self.lru_GUI)
        lru_btn.place(relx= 0.27, rely=0.40)

        fifo_btn = Button(self.root,text="FIFO Page Replacement", font=FONT_BOLD, width=20,command=self.fifo_GUI)
        fifo_btn.place(relx= 0.27, rely=0.52)

        back_btn = Button(self.root,text="Back", font=FONT_BOLD, width=10, command=self.main_window)
        back_btn.place(relx= 0.37, rely=0.64)

    def MM_POPUP(self, faults, hit):
        win = Toplevel()
        win.wm_title("Memory Management")
        win.configure(width=300, height= 250)
        l1 = Label(win, text="Number of Page Faults: "+ str(faults),font="Helvetica 14 bold" ,fg=TEXT_COLOR)
        l1.place(relx=0.1,rely=0.2, relwidth=0.8)
        l2 = Label(win, text="Number of Page Hit: "+ str(hit),font="Helvetica 14 bold" ,fg=TEXT_COLOR)
        l2.place(relx=0.1,rely=0.5, relwidth=0.7)
        b = Button(win, text="Okay", fg=TEXT_COLOR, command=self.main_window)
        b.place(relx=0.3,rely=0.8,relwidth=0.2)


    def lru_GUI(self):
        for i in self.root.winfo_children():
            i.destroy()
        head_label = Label(self.root,  fg=TEXT_COLOR,
                            text="LRU Page Replacement", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)

        pages_label = Label(self.root, text="Enter Your Reference String: ",  fg=TEXT_COLOR,font=FONT_BOLD, pady=10)
        self.pages_entry = Entry(self.root, font=FONT)
        self.pages_entry.focus()
        pages_label.place(relx=0.1, rely=0.31)
        self.pages_entry.place(relx=0.63, rely=0.32,relwidth=0.25, relheight= 0.06)
        framesize_label = Label(self.root, text="Enter Your Frame Size: ",  fg=TEXT_COLOR,font=FONT_BOLD, pady=10)
        self.framesize_entry = Entry(self.root, font=FONT)
        framesize_label.place(relx=0.1, rely=0.51)
        self.framesize_entry.place(relx=0.53, rely=0.53,relwidth=0.25, relheight= 0.06)

        submit_btn = Button(self.root,text="Submit", font=FONT_BOLD, width=10, command=self.lru_submit)
        submit_btn.place(relx= 0.37, rely=0.68)

    def lru_submit(self):
        pages = self.pages_entry.get()
        frame_size = self.framesize_entry.get()
        pages = list(pages)
        PageFaults, PageHit = LRU_replacement(pages,frame_size)
        self.MM_POPUP(PageFaults,PageHit)


    def fifo_GUI(self):
        for i in self.root.winfo_children():
            i.destroy()
        head_label = Label(self.root,  fg=TEXT_COLOR,
                            text="LRU Page Replacement", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)

        pages_label = Label(self.root, text="Enter Your Reference String: ",  fg=TEXT_COLOR,font=FONT_BOLD, pady=10)
        self.pages_entry = Entry(self.root, font=FONT)
        self.pages_entry.focus()
        pages_label.place(relx=0.1, rely=0.31)
        self.pages_entry.place(relx=0.63, rely=0.32,relwidth=0.25, relheight= 0.06)
        framesize_label = Label(self.root, text="Enter Your Frame Size: ",  fg=TEXT_COLOR,font=FONT_BOLD, pady=10)
        self.framesize_entry = Entry(self.root, font=FONT)
        self.framesize_entry.focus()
        framesize_label.place(relx=0.1, rely=0.51)
        self.framesize_entry.place(relx=0.53, rely=0.52,relwidth=0.25, relheight= 0.06)

        submit_btn = Button(self.root,text="Submit", font=FONT_BOLD, width=10, command=self.fifo_submit)
        submit_btn.place(relx= 0.37, rely=0.68)

    def fifo_submit(self):
        pages = self.pages_entry.get()
        frame_size = self.framesize_entry.get()
        pages = list(pages)
        PageFaults, PageHit = FIFO_replacement(pages,int(frame_size))
        self.MM_POPUP(PageFaults,PageHit)




#----------------------------SCHEDULING-------------------------------



    def process_scheduling(self):
        for i in self.root.winfo_children():
            i.destroy()
        # head label
        head_label = Label(self.root,  fg=TEXT_COLOR,
                            text="Process Scheduling", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)
        

        # buttons
        rr_btn = Button(self.root,text="Round Robin Scheduling", font=FONT_BOLD, width=20, command=self.get_quantum)
        rr_btn.place(relx= 0.27, rely=0.40)

        fifo_btn = Button(self.root,text="FIFO Scheduling", font=FONT_BOLD, width=20, command=self.FCFS)
        fifo_btn.place(relx= 0.27, rely=0.52)

        back_btn = Button(self.root,text="Back", font=FONT_BOLD, width=10, command=self.main_window)
        back_btn.place(relx= 0.27, rely=0.64)


# ROUND ROBIN GUI
    def rr(self):
        if len(processes) != 0:
            rr_list = processes.copy()
            quantum = self.time_quantum.get()
            process = RoundRobin(rr_list,quantum)
            for i in self.root.winfo_children():
                i.destroy()
            # head label
            head_label = Label(self.root,  fg=TEXT_COLOR,
                                text="Round Robin Scheduling", font=FONT_BOLD, pady=10)
            head_label.place(relwidth=1)
            
            # Create a frame to hold the treeview
            frame = Frame(self.root)
            frame.place(relwidth=1, rely=0.1, relheight=0.80)

            # Create a scrollbar for the frame
            vscrollbar = Scrollbar(frame, orient=VERTICAL)
            vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)

            # Create the treeview
            tree = ttk.Treeview(frame, columns=("PID", "CT", "AT", "BT", "TT", "WT"), show="headings", yscrollcommand=vscrollbar.set)
            tree.heading("PID", text="PID")
            tree.heading("CT", text="CT")
            tree.heading("AT", text="AT")
            tree.heading("BT", text="BT")
            tree.heading("TT", text="TT")
            tree.heading("WT", text="WT")
            tree.column("PID", width=50, anchor='center')
            tree.column("CT", width=50, anchor='center')
            tree.column("AT", width=50, anchor='center')
            tree.column("BT", width=50, anchor='center')
            tree.column("TT", width=50, anchor='center')
            tree.column("WT", width=50, anchor='center')

            # Add the processes to the treeview
            for i in range(len(process)):
                tree.insert("", END, values=(process[i].pid, process[i].completion_time, process[i].arrival_time, process[i].burst_time, process[i].turnaround_time, process[i].waiting_time))

            # Add the treeview to the frame
            tree.pack(fill=BOTH, expand=YES)

            # Configure the scrollbar
            vscrollbar.config(command=tree.yview)

            back_btn = Button(self.root,text="Back", font=FONT_BOLD, width=10, command=self.main_window)
            back_btn.place(relx= 0.27, rely=0.94)
        else:
            self.popup()
# FCFS GUI
    def FCFS(self):
        if len(processes) != 0:
            for i in self.root.winfo_children():
                i.destroy()
            # head label
            head_label = Label(self.root,  fg=TEXT_COLOR,
                                text="First Come First Serve", font=FONT_BOLD, pady=10)
            head_label.place(relwidth=1)
            
            fcfs_list = processes.copy()
            process = fcfs(fcfs_list)

            frame = Frame(self.root)
            frame.place(relwidth=1, rely=0.1, relheight=0.80)

            # Create a scrollbar for the frame
            vscrollbar = Scrollbar(frame, orient=VERTICAL)
            vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
            # Create the treeview
            tree = ttk.Treeview(frame, columns=("PID", "CT", "AT", "BT", "TT", "WT"), show="headings", yscrollcommand=vscrollbar.set)
            tree.heading("PID", text="PID")
            tree.heading("CT", text="CT")
            tree.heading("AT", text="AT")
            tree.heading("BT", text="BT")
            tree.heading("TT", text="TT")
            tree.heading("WT", text="WT")
            tree.column("PID", width=50, anchor='center')
            tree.column("CT", width=50, anchor='center')
            tree.column("AT", width=50, anchor='center')
            tree.column("BT", width=50, anchor='center')
            tree.column("TT", width=50, anchor='center')
            tree.column("WT", width=50, anchor='center')

            # Add the processes to the treeview
            for i in range(len(process)):
                tree.insert("", END, values=(process[i].pid, process[i].completion_time, process[i].arrival_time, process[i].burst_time, process[i].turnaround_time, process[i].waiting_time))

            # Add the treeview to the frame
            tree.pack(fill=BOTH, expand=YES)

            # Configure the scrollbar
            vscrollbar.config(command=tree.yview)

            back_btn = Button(self.root,text="Back", font=FONT_BOLD, width=10, command=self.main_window)
            back_btn.place(relx= 0.27, rely=0.94)
        else:
            self.popup()



#___________________PCB___________________


    def process_control_block(self):
        if len(processes) != 0:
            for i in self.root.winfo_children():
                i.destroy()
            # head label
            head_label = Label(self.root,  fg=TEXT_COLOR,
                                text="Process Control Block", font=FONT_BOLD, pady=10)
            head_label.place(relwidth=1)
            
            frame = Frame(self.root)
            frame.place(relwidth=1, rely=0.1, relheight=0.80)

            # Create a scrollbar for the frame
            vscrollbar = Scrollbar(frame, orient=VERTICAL)
            vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
            # Create the treeview
            tree = ttk.Treeview(frame, columns=("PID", "State", "Priority", "Pointer"), show="headings", yscrollcommand=vscrollbar.set)
            tree.heading("PID", text="PID")
            tree.heading("State", text="State")
            tree.heading("Priority", text="Priority")
            tree.heading("Pointer", text="Pointer")
            tree.column("PID", width=60, anchor='center')
            tree.column("State", width=60, anchor='center')
            tree.column("Priority", width=60, anchor='center')
            tree.column("Pointer", width=60, anchor='center')

            # Add the processes to the treeview
            for i in range(len(processes)):
                tree.insert("", END, values=(processes[i].pid, processes[i].pstate, processes[i].priority, processes[i].point))

            # Add the treeview to the frame
            tree.pack(fill=BOTH, expand=YES)

            # Configure the scrollbar
            vscrollbar.config(command=tree.yview)

            back_btn = Button(self.root,text="Back", font=FONT_BOLD, width=10, command=self.main_window)
            back_btn.place(relx= 0.27, rely=0.94)
        else:
            self.popup()
        
        

if __name__ == "__main__":
    app = OS()