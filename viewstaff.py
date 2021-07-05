from tkinter import Tk, PanedWindow, Entry, Label, Button, END
from tkinter.ttk import Treeview
from pymysql import *
from connectionfile import *

class viewstaff:


    def __init__(self):
        self.root=Tk()
        self.root.geometry("800x800")

        self.p1=PanedWindow(self.root)
        self.p2=PanedWindow(self.root)
        self.p1.pack()
        self.p2.pack()



        self.t1=Treeview(self.p2,column=("staffid","name","email","mobile","password","designation"))

        self.t1.heading("staffid",text="staffid")
        self.t1.heading("name",text="staff name")
        self.t1.heading("email",text="email")
        self.t1.heading("mobile",text="mobile")
        self.t1.heading("password",text="password")
        self.t1.heading("password",text="designation")
        s = "select *from staff "

        conn = connectionfile.connect('')
        cr = conn.cursor()
        cr.execute(s)
        result = cr.fetchall()

        i = 0
        for row in result:
            self.t1.insert("", index=i, values=row)
            i = i + 1


        self.t1["show"]="headings"

        self.t1.pack()
        self.root.mainloop()

 #..............................................
