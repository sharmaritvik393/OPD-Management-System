from tkinter import Tk, PanedWindow, Entry, Label, Button
from tkinter.ttk import Treeview
from pymysql import *
from connectionfile import *
from addslot import *
class viewdoctor:
    def slotinsert(self):

        f = self.t1.focus()
        d = self.t1.item(f)
        l = d['values']

        if len(l) > 0:
            did = l[0]
            addslot(did)
        else:
            showinfo('', 'select doctor')





    def __init__(self):
        self.root=Tk()
        self.root.geometry("800x800")

        self.p1=PanedWindow(self.root)
        self.p2=PanedWindow(self.root)
        self.p1.pack()
        self.p2.pack()




        self.t1=Treeview(self.p2,column=("doctorid","name","email","mobile"))
        self.t1.heading("doctorid", text="doctorid")

        self.t1.heading("name",text="name")
        self.t1.heading("email",text="email")
        self.t1.heading("mobile",text="mobile")
        s = "select  * from doctor "
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
