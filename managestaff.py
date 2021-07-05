from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
from connectionfile import *
from pymysql import *

class managestaff:
    def search(self):
        if self.cb1.get()=="":
            showinfo('','select staff id')
        else:
            s = "select * from staff where staffid='" + self.cb1.get() + "'"
            conn = connectionfile.connect('')
            cr = conn.cursor()
            cr.execute(s)
            row = cr.fetchone()
            self.textbox1.delete(0, END)
            self.textbox2.delete(0, END)
            self.textbox3.delete(0, END)
            self.textbox4.delete(0, END)
            self.textbox5.delete(0, END)
            self.textbox1.insert(0, str(row[1]))
            self.textbox2.insert(0, str(row[2]))
            self.textbox3.insert(0, str(row[3]))
            self.textbox4.insert(0, str(row[4]))
            self.textbox5.insert(0, str(row[5]))



    def remove(self):
        if self.cb1.get()=="":
            showinfo('','select staff id')
        else:
            s = "delete from staff where staffid=" + self.cb1.get()
            conn = connectionfile.connect('')
            cr = conn.cursor()
            cr.execute(s)
            conn.commit()

            self.textbox1.delete(0,END)
            self.textbox2.delete(0,END)
            self.textbox3.delete(0,END)
            self.textbox4.delete(0,END)
            self.textbox5.delete(0,END)
            conn = connectionfile.connect('')
            s = "select * from staff"
            cr = conn.cursor()
            cr.execute(s)
            result = cr.fetchall()
            x = []
            for row in result:
                x.append(row[0])
            self.cb1['values']=x
            self.cb1.current(0)

            showinfo("", "staff record deleted")

    def update(self):
        s="update staff set name='"+self.textbox1.get()+"',email='"+ self.textbox2.get()+"',mobile='"+ self.textbox3.get()+"',password='"+self.textbox4.get()+"',designation='"+self.textbox5.get()+ "' where staffid='"+self.cb1.get() + "'"

        conn = connectionfile.connect('')
        cr=conn.cursor()
        cr.execute(s)
        conn.commit()
        showinfo("","record updated")

    def __init__(self):
        self.root=Tk()
        self.root.geometry("400x400")
        conn=connectionfile.connect('')
        s="select * from staff"
        cr=conn.cursor()
        cr.execute(s)
        result=cr.fetchall()
        x=[]
        for row in result:
            x.append(row[0])
        self.lb=Label(self.root,text="select staff id")
        self.cb1=Combobox(self.root,values=x,state="readonly")
        self.cb1.grid(row=0,column=1)
        self.bt1=Button(self.root,text="get details",command=self.search)
        self.bt1.grid(row=0,column=2)
        self.lb1 = Label(self.root, text="enter staff name")
        self.textbox1 = Entry(self.root)
        self.lb2 = Label(self.root, text="enter email id")
        self.textbox2 = Entry(self.root)
        self.lb3 = Label(self.root, text="enter mobile")
        self.textbox3 = Entry(self.root)
        self.lb4 = Label(self.root, text="enter password")
        self.textbox4 = Entry(self.root)
        self.lb5 = Label(self.root, text="enter designation")
        self.textbox5 = Entry(self.root)

        self.lb.grid(row=0, column=0)

        self.lb1.grid(row=1, column=0)
        self.lb2.grid(row=2, column=0)
        self.lb3.grid(row=3, column=0)
        self.lb4.grid(row=4, column=0)
        self.lb5.grid(row=5, column=0)

        self.textbox1.grid(row=1, column=1)
        self.textbox2.grid(row=2, column=1)
        self.textbox3.grid(row=3, column=1)
        self.textbox4.grid(row=4, column=1)
        self.textbox5.grid(row=5, column=1)

        self.bt2=Button(self.root,text="delete",command=self.remove)
        self.bt2.grid(row=6,column=0)
        self.bt3=Button(self.root,text="update",command=self.update)
        self.bt3.grid(row=6,column=1)

        self.root.mainloop()
#............................
