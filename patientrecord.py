from tkinter import Button, Label, Entry, Tk
from tkinter.messagebox import showinfo

from tkcalendar import *
from connectionfile import *



class patientrecord:
    def insert(self):
        if str(self.textbox2.get()).count("@") != 1:
            showinfo("", "invalid email address")
        elif str(self.textbox2.get()).count(".com") != 1:
            showinfo("", "invalid email address")
        elif not str(self.textbox3.get()).isdigit():
            showinfo("", "invalid mobile number")
        elif len(self.textbox3.get()) != 10:
            showinfo("", "invalid mobile number")
        elif not str(self.textbox7.get()).isdigit():
            showinfo("","invalid age")
        elif int(self.textbox7.get())>100:
            showinfo("","invalid age")
        else:
            s = "insert into patientrecord values(NULL,'" + self.textbox1.get() + "','" + self.textbox2.get() + "','" + self.textbox3.get() + "','" + self.textbox4.get() + "','" + self.textbox5.get() + "','"+str(self.textbox6.get_date())+"','"+str(self.textbox7.get())+"','"+self.textbox8.get()+"','"+self.textbox9.get()+"')"
            conn = connectionfile.connect('')
            cr = conn.cursor()
            cr.execute(s)
            conn.commit()
            showinfo("", "patient record added successfully")
    def __init__(self):
        self.root = Tk()

        self.root.geometry("500x500")
        self.lb1 = Label(self.root, text="patient record")

        self.lb2 = Label(self.root, text="enter name")
        self.textbox1 = Entry(self.root)
        self.lb3 = Label(self.root, text="enter email id")
        self.textbox2 = Entry(self.root)
        self.lb4 = Label(self.root, text="enter mobile")
        self.textbox3 = Entry(self.root)
        self.lb5 = Label(self.root, text="enter spouse name")
        self.textbox4 = Entry(self.root)
        self.lb6 = Label(self.root, text="enter father's name")
        self.textbox5 = Entry(self.root)
        self.lb7 = Label(self.root, text="enter date of birth")
        self.textbox6 =DateEntry(self.root)
        self.lb8 = Label(self.root, text="enter age")
        self.textbox7 = Entry(self.root)
        self.lb9 = Label(self.root, text="known problems")
        self.textbox8 = Entry(self.root)
        self.lb10 = Label(self.root, text="known allergies")
        self.textbox9 = Entry(self.root)

        self.lb1.grid(row=0, column=1)
        self.lb2.grid(row=1, column=0)
        self.lb3.grid(row=2, column=0)
        self.lb4.grid(row=3, column=0)
        self.lb5.grid(row=4, column=0)
        self.lb6.grid(row=5, column=0)
        self.lb7.grid(row=6, column=0)
        self.lb8.grid(row=7, column=0)
        self.lb9.grid(row=8, column=0)
        self.lb10.grid(row=9, column=0)

        self.textbox1.grid(row=1, column=1)
        self.textbox2.grid(row=2, column=1)
        self.textbox3.grid(row=3, column=1)
        self.textbox4.grid(row=4, column=1)
        self.textbox5.grid(row=5, column=1)
        self.textbox6.grid(row=6, column=1)
        self.textbox7.grid(row=7, column=1)
        self.textbox8.grid(row=8, column=1)
        self.textbox9.grid(row=9, column=1)

        self.bt1 = Button(self.root, text="add",command=self.insert)
        self.bt1.grid(row=10, column=1)

        self.root.mainloop()
#.............................

