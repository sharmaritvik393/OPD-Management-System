from tkinter import *
from changepassword1 import *

class staffhome:
    def updatepassword(self):
        obj=changepassword1(self.globalemail)

    def __init__(self,email):
        self.root=Tk()
        self.globalemail=""
        self.globalemail=email
        self.root.geometry("400x400")

        self.lb1=Label(self.root,text="welcome "+email)

        self.bt1=Button(self.root,text="change password",command=self.updatepassword)
        self.bt2=Button(self.root,text="add patient")


        self.lb1.grid(row=0,column=0)
        self.bt1.grid(row=1,column=1)
        self.bt2.grid(row=1,column=2)

        self.root.mainloop()
#....................................
