from tkinter import Tk, Label, Entry, Button, Menu
from tkinter.messagebox import showinfo

from pymysql import *


class addstaff:
    def insert(self):
        if str(self.textbox2.get()).count("@")!=1:
            showinfo("","invalid email address")
        elif not str(self.textbox3.get()).isdigit():
            showinfo("","invalid mobile number")
        elif len(self.textbox3.get())!=10:
            showinfo("","invalid mobile number")
        elif str(self.textbox2.get()).count(".com")!=1:
            showinfo("","invalid email")

        else:
            s="insert into staff values(NULL,'"+self.textbox1.get()+"','"+ self.textbox2.get()+"','"+ self.textbox3.get()+"','"+self.textbox4.get()+"','"+self.textbox5.get()+"')"
            conn=Connect("127.0.0.1","root","","opd")
            cr=conn.cursor()
            cr.execute(s)
            conn.commit()
            showinfo("","staff added successfully")

    def __init__(self):

        self.root=Tk()

        self.root.geometry("500x500")



        self.lb1=Label(self.root,text="enter staff name")
        self.textbox1 = Entry(self.root)
        self.lb2=Label(self.root, text="enter email id")
        self.textbox2 = Entry(self.root)
        self.lb3=Label(self.root,text="enter mobile")
        self.textbox3 = Entry(self.root)
        self.lb4=Label(self.root, text="enter password")
        self.textbox4 = Entry(self.root)
        self.lb5=Label(self.root, text="enter designation")
        self.textbox5=Entry(self.root)

        self.lb1.grid(row=0,column=0)
        self.lb2.grid(row=1, column=0)
        self.lb3.grid(row=2, column=0)
        self.lb4.grid(row=3, column=0)
        self.lb5.grid(row=4, column=0)

        self.textbox1.grid(row=0,column=1)
        self.textbox2.grid(row=1,column=1)
        self.textbox3.grid(row=2, column=1)
        self.textbox4.grid(row=3, column=1)
        self.textbox5.grid(row=4, column=1)

        self.bt1=Button(self.root,text="add",command=self.insert)
        self.bt1.grid(row=5,column=1)

        self.root.mainloop()
#............................
