from tkinter import Tk, PanedWindow, Entry, Label, Button
from tkinter.ttk import Treeview
from pymysql import *
from connectionfile import *

class viewpatients:
    def search(self):
        s="select *from patientrecord "

        conn=connectionfile.connect('')
        cr=conn.cursor()
        cr.execute(s)
        result=cr.fetchall()
        i=0
        for row in result:
            self.t1.insert("",index=i,values=row)
            i=i+1
    def __init__(self):
        self.root=Tk()
        self.root.geometry("800x800")

        self.p1=PanedWindow(self.root)
        self.p2=PanedWindow(self.root)
        self.p1.pack()
        self.p2.pack()

        self.bt=Button(self.p1,text="show data",command=self.search)


        self.t1=Treeview(self.p2,column=("patientid","patientname","email","mobile","spousename","fathername","dob","age","knownproblems","knownallergies"))

        self.t1.heading("patientid",text="pateintid")
        self.t1.heading("patientname",text="pateint name")
        self.t1.heading("email",text="email")
        self.t1.heading("mobile",text="mobile")
        self.t1.heading("spousename",text="spouse name")
        self.t1.heading("fathername",text="father's name")
        self.t1.heading("dob",text="date of birth")
        self.t1.heading("age",text="age")
        self.t1.heading("knownproblems",text="known problems")
        self.t1.heading("knownallergies",text="known allergies")


        self.t1["show"]="headings"
        self.bt.grid(row=0,column=2)

        self.t1.pack()
        self.root.mainloop()

 #..............................................
