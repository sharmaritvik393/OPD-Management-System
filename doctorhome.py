from tkinter import Tk, Label, Button, Entry
from tkinter.messagebox import showinfo

from connectionfile import *
from doctorappointments import *
from changepassword2 import *

class doctorhome:
    def updatepassword(self):
        obj=changepassword2(self.globalemail)

    def add(self):
            obj=doctorappointments(self.globalemail)

    def __init__(self,email):
        self.root=Tk()
        self.globalemail=""
        self.globalemail=email
        self.root.geometry("400x400")
        conn = connectionfile.connect('')
        cr = conn.cursor()

        self.lb1=Label(self.root,text="welcome "+email)

        self.bt1=Button(self.root,text="change password",command=self.updatepassword)
        self.bt2 = Button(self.root, text="view appointments", command=self.add)
        self.bt2.grid(row=3, column=1)

        self.lb1.grid(row=0,column=0)
        self.bt1.grid(row=0,column=1)
        self.bt2.grid(row=1,column=1)

        self.root.mainloop()


#..............................
