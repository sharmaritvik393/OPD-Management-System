from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import *
from connectionfile import *
from pymysql import *


class changepassword2:

    def change(self):
        if self.textbox1.get() == "" or self.textbox2.get() == "" or self.textbox3.get() == "":
            showinfo("", "Fields Marked * are Mandatory")
        elif self.textbox2.get() != self.textbox3.get():
            showinfo("", "New Password doesn't match")
        else:
            s = "update doctor set password='" + self.textbox2.get() + "' where email='" + self.globalemail + "'"
            conn = connectionfile.connect('')

            cr = conn.cursor()
            cr.execute(s)
            conn.commit()
            showinfo("", "Password Changed")

    def __init__(self, email):
        self.root = Tk()
        self.root.geometry("600x600")
        self.globalemail = ""
        self.globalemail = email
        self.lb1 = Label(self.root, text="Change Password")
        self.lb1.grid(row=0, column=1)
        self.lb2 = Label(self.root, text="Enter Old Password *")
        self.lb2.grid(row=1, column=0)
        self.textbox1 = Entry(self.root)
        self.textbox1.grid(row=1, column=1)
        self.lb3 = Label(self.root, text="Enter New Password *")
        self.lb3.grid(row=2, column=0)
        self.textbox2 = Entry(self.root)
        self.textbox2.grid(row=2, column=1)
        self.lb4 = Label(self.root, text="Confirm New Password *")
        self.lb4.grid(row=3, column=0)
        self.textbox3 = Entry(self.root)
        self.textbox3.grid(row=3, column=1)
        self.bt1 = Button(self.root, text="Change", command=self.change)
        self.bt1.grid(row=4, column=1)

        self.root.mainloop()