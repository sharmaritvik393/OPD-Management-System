import tkinter
from tkinter.messagebox import showinfo
from tkinter.ttk import Combobox

from tkcalendar import DateEntry
from connectionfile import *



class bookappointment:

    def insert(self):
        conn = Connect("127.0.0.1", "root", "", "opd")
        cr = conn.cursor()
        s1="select * from appointment where doctorid='"+str(self.cb2.get())+"' and date='"+str(self.textbox3.get_date())+"' and slotid='"+str(self.cb3.get())+"'"
        n=cr.execute(s1)
        tokenno=0
        s2="select maxcap from slots where doctorid='"+str(self.cb2.get())+"'  and slotid='"+str(self.cb3.get())+"'"
        cr.execute(s2)
        rs=cr.fetchone()
        maxcap=(int)(rs[0])
        if n<=maxcap:
            cr.execute(s1)
            result =cr.fetchall()
            for row in result:
                tokenno=(int)(row[8])
            tokenno=tokenno+1
            p = "insert into appointment values(NULL,'" + str(self.cb1.get()) + "','" + str(
                self.cb2.get()) + "','" + str(self.textbox3.get_date()) + "','" + str(self.cb3.get()) + "','" + str(
                self.textbox4.get()) + "','" + str(self.cb4.get()) + "','" + str(self.cb5.get()) + "','"+str(tokenno)+"','pending', '')"

            cr.execute(p)
            conn.commit()
            showinfo("", "data added successfully")
        else:
            showinfo('','slot is full ')




    def go(self):
        s=self.cb1.get()
        if s=="":
            showinfo("","select patient id")
        else:
            d="select * from patientrecord where patientid='"+s+"'"
            conn = connectionfile.connect('')
            cr = conn.cursor()
            n=cr.execute(d)
            row=cr.fetchone()
            self.textbox1.delete(0, tkinter.END)

            if n>0:
                self.textbox1.insert(0,str(row[1]))

    def search(self):
        print()
        if self.cb1.get() == "":
            showinfo('', 'select patientid')
        else:
            s = "select * from patientrecord where patientid='" + self.cb1.get() + "'"
            conn = connectionfile.connect('')
            cr = conn.cursor()
            cr.execute(s)
            row = cr.fetchone()
            self.textbox1.insert(0, str(row[1]))
            self.textbox2.insert(0, str(row[2]))
            self.textbox3.insert(0, str(row[3]))
            self.textbox4.insert(0, str(row[4]))

        if self.cb2.get() == "":
            showinfo('', 'select doctorid')
        else:
            a = "select * from doctor where doctorid='" + self.cb2.get() + "'"
            conn = connectionfile.connect('')
            cr = conn.cursor()
            cr.execute(a)
            row = cr.fetchone()
            self.textbox1.insert(0, str(row[1]))
            self.textbox2.insert(0, str(row[2]))
            self.textbox3.insert(0, str(row[3]))
            self.textbox4.insert(0, str(row[4]))




    def callback(self,event):
        self.cb3.set('')
        self.cb3['values']=''
        self.doctorid=self.cb2.get()
        b="select * from slots where doctorid="+self.cb2.get()
        conn = connectionfile.connect('')
        cr = conn.cursor()
        cr.execute(b)
        result = cr.fetchall()
        z = []
        for row in result:
            z.append(row[0])

        self.cb3['values']=z

    def __init__(self):
        self.root=tkinter.Tk()
        self.root.geometry("400x400")
        conn = connectionfile.connect('')
        s="select *from patientrecord"
        cr=conn.cursor()
        cr.execute(s)
        result=cr.fetchall()
        x=[]
        for row in result:
            x.append(row[0])

        self.lb1=tkinter.Label(self.root, text="patientid")
        self.cb1=Combobox(self.root,values=x,state="readonly")
        self.cb1.grid(row=0,column=1)

        self.lb2=tkinter.Label(self.root, text="name")
        self.textbox1=tkinter.Entry(self.root)
        self.textbox1.grid(row=1,column=1)

        self.lb3=tkinter.Label(self.root, text="patient history")
        self.textbox2=tkinter.Entry(self.root)
        self.textbox2.grid(row=2,column=1)


        a = "select *from doctor"
        cr = conn.cursor()
        cr.execute(a)
        result = cr.fetchall()
        y = []
        for row in result:
            y.append(row[0])

        self.lb4=tkinter.Label(self.root, text="select doctor id")
        self.cb2=Combobox(self.root,values=y,state="readonly")

        self.cb2.grid(row=3,column=1)
        self.cb2.bind("<<ComboboxSelected>>",self.callback)


        self.lb5=tkinter.Label(self.root, text="date")
        self.textbox3=DateEntry(self.root)
        self.textbox3.grid(row=4,column=1)


        b = "select *from slots"
        cr = conn.cursor()
        cr.execute(b)
        result = cr.fetchall()
        z = []
        for row in result:
            z.append(row[0])

        self.lb6=tkinter.Label(self.root, text="slotid")
        self.cb3=Combobox(self.root,values=z,state="readonly")
        self.cb3.grid(row=5,column=1)

        self.lb7=tkinter.Label(self.root, text="amount")
        self.textbox4=tkinter.Entry(self.root)
        self.textbox4.grid(row=6,column=1)

        self.lb8=tkinter.Label(self.root, text="type of booking")
        self.cb4=Combobox(self.root,values=("phone","walkin"))
        self.cb4.grid(row=7,column=1)

        self.lb9=tkinter.Label(self.root, text="payment recieved")
        self.cb5=tkinter.Entry(self.root)
        self.cb5.grid(row=8,column=1)

        self.lb1.grid(row=0,column=0)
        self.lb2.grid(row=1,column=0)
        self.lb3.grid(row=2,column=0)
        self.lb4.grid(row=3,column=0)
        self.lb5.grid(row=4,column=0)
        self.lb6.grid(row=5,column=0)
        self.lb7.grid(row=6,column=0)
        self.lb8.grid(row=7,column=0)
        self.lb9.grid(row=8,column=0)

        self.bt3=tkinter.Button(self.root, text="book", command=self.insert)
        self.bt3.grid(row=9,column=1)

        self.bt4= tkinter.Button(self.root,text="get details",command=self.go )
        self.bt4.grid(row=0,column=3)
        self.root.mainloop()
#.............................
