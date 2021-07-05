from tkinter import Tk, Label, Entry, IntVar, Checkbutton, Button
from tkinter.messagebox import showinfo
from tkinter.ttk import Combobox
from connectionfile import *


class addslot:
    def display(self):
        if self.ans1.get() == 1:
            self.lst[0] = 'yes'
            # showinfo("", "monday")
        if self.ans2.get() == 1:
            self.lst[1] = 'yes'
            # showinfo("", "tuesday")
        if self.ans3.get() == 1:
            self.lst[2] = 'yes'
            # showinfo("", "wednesday")
        if self.ans4.get() == 1:
            self.lst[3] = 'yes'
            # showinfo("", "thursday")
        if self.ans5.get() == 1:
            self.lst[4] = 'yes'
            # showinfo("", "friday")
        if self.ans6.get() == 1:
            self.lst[5] = 'yes'
            # showinfo("", "saturday")
        if self.ans7.get() == 1:
            self.lst[6] = 'yes'
            # showinfo("", "sunday")
        s="insert into slots values(NULL,'"+self.textbox1.get()+"','"+self.lst[0]+"','"+self.lst[1]+"','"+self.lst[2]+"','"+self.lst[3]+"','"+self.lst[4]+"','"+self.lst[5]+"','"+self.lst[6]+"','"+str(self.cb1.get())+"','"+str(self.cb2.get())+"')"
        conn=connectionfile.connect('')
        cr = conn.cursor()
        cr.execute(s)
        conn.commit()
        showinfo('','slot added successfully')


    def __init__(self):
        self.root=Tk()
        self.root.geometry("400x400")
        self.lst=['no','no','no','no','no','no','no']

        self.ans1=IntVar()
        self.ans2=IntVar()
        self.ans3=IntVar()
        self.ans4=IntVar()
        self.ans5=IntVar()
        self.ans6=IntVar()
        self.ans7=IntVar()
        conn = connectionfile.connect('')
        s = "select * from doctor"
        cr = conn.cursor()
        cr.execute(s)
        result = cr.fetchall()
        x = []
        for row in result:
            x.append(row[0])
        self.lb = Label(self.root, text="select doctor id")
        self.cb2 = Combobox(self.root, values=x, state="readonly")
        self.ch1=Checkbutton(self.root,text="monday",variable=self.ans1)
        self.ch2=Checkbutton(self.root,text="tuesday",variable=self.ans2)
        self.ch3=Checkbutton(self.root,text="wednesday",variable=self.ans3)
        self.ch4=Checkbutton(self.root,text="thursday",variable=self.ans4)
        self.ch5=Checkbutton(self.root,text="friday",variable=self.ans5)
        self.ch6=Checkbutton(self.root,text="saturday",variable=self.ans6)
        self.ch7=Checkbutton(self.root,text="sunday",variable=self.ans7)

        self.lb1=Label(self.root,text="slot detail")
        self.textbox1=Entry(self.root)
        self.lb.grid(row=0, column=0)
        self.cb2.grid(row=0, column=1)
        self.lb1.grid(row=1,column=0)

        self.textbox1.grid(row=1,column=1)


        self.lb2=Label(self.root,text="maximum capacity")
        self.lb2.grid(row=2,column=0)

        self.cb1=Combobox(self.root,values=(1,2,3,4,5,6,7,8,9),state="readonly")
        self.cb1.grid(row=2,column=1)

        self.ch1.grid(row=3,column=0)
        self.ch2.grid(row=3,column=1)
        self.ch3.grid(row=3,column=2)
        self.ch4.grid(row=4,column=0)
        self.ch5.grid(row=4,column=1)
        self.ch6.grid(row=4,column=2)
        self.ch7.grid(row=5,column=0)


        self.bt1=Button(self.root,text="add slot",command=self.display)
        self.bt1.grid(row=6,column=2)

        self.root.mainloop()
#............................
