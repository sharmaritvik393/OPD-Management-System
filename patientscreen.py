from tkinter import Tk, PanedWindow, Button, Label, Entry
from tkinter.messagebox import showinfo
from tkinter.ttk import Treeview, Combobox

from tkcalendar import DateEntry

from connectionfile import *
import pyttsx3

class patientscreen:
    def sound(self,s1,s2):
        # One time initialization
        engine = pyttsx3.init()

        # Set properties _before_ you add things to say
        engine.setProperty('rate', 150)  # Speed percent (can go over 100)
        engine.setProperty('volume', 0.9)  # Volume 0-1

        # Queue up things to say.
        # There will be a short break between each one
        # when spoken, like a pause between sentences.
        engine.say(s1)
        engine.say(s2)

        # Flush the say() queue and play the audio
        engine.runAndWait()

        # Program will not continue execution until
        # all speech is done talking

    def show(self):
        conn = connectionfile.connect('')
        cr = conn.cursor()
        q= "select tokens from appointment where doctorid='" + str(self.cb2.get()) + "' and date='" + str(
            self.textbox1.get_date()) + "' and status='pending'"
        cr.execute(q)
        rs=cr.fetchone()
        tkn= (int)(rs[0])


        self.sound("Attention Everyone", "Next Turn is of Token no "+str(tkn))
        self.t1.delete(*self.t1.get_children())
        print(str(self.textbox1.get_date()))
        s = "select * from appointment where doctorid='"+str(self.cb2.get())+"' and date='"+str(self.textbox1.get_date())+"' and status='pending'"


        cr.execute(s)
        result = cr.fetchall()
        i = 0
        for row in result:
            self.t1.insert("", index=i, values=row)
            i = i + 1

    def done(self):
        f=self.t1.focus()
        d=self.t1.item(f)
        l=d["values"]
        if len(l)>0:
            tn=(int)(l[8])+1
            self.sound("Attention Everyone", "Next Turn is of Token no "+str(tn))
            appointmentid=l[0]
            s="update appointment set status='done' where appointmentid='"+str(appointmentid)+"'"
            conn = connectionfile.connect('')
            cr = conn.cursor()

            cr.execute(s)
            conn.commit()
            for row in self.t1.get_children():
                self.t1.delete(row)
            s="select *from appointment where doctorid='"+str(self.cb2.get())+"' and date='"+str(self.textbox1.get_date())+"' and status='pending'"
            conn = connectionfile.connect('')
            cr = conn.cursor()
            cr.execute(s)
            result = cr.fetchall()
            showinfo("","status updated successfully")
            i = 0
            for row in result:
                self.t1.insert("", index=i, values=row)
                i = i + 1
        else:
            showinfo("","select any appointment in view")

    def __init__(self):
        self.root = Tk()
        self.root.geometry("800x800")

        self.p1 = PanedWindow(self.root)
        self.p2 = PanedWindow(self.root)
        self.p3 = PanedWindow(self.root)

        self.p1.pack()
        self.p2.pack()
        self.p3.pack()

        self.lb1 = Label(self.p1, text="enter appointment")
        self.lb1.grid(row=0,column=1)
        self.textbox1=DateEntry(self.p1)
        self.textbox1.grid(row=1,column=2)
        self.bt1=Button(self.p1,text="search",command=self.show)
        self.bt1.grid(row=1,column=3)
        a = "select *from doctor"
        conn = connectionfile.connect('')
        cr=conn.cursor()
        cr.execute(a)
        result = cr.fetchall()
        y = []
        for row in result:
            y.append(row[0])

        self.lb4 = Label(self.p1, text="select doctor id")
        self.cb2 = Combobox(self.p1, values=y, state="readonly")
        self.lb4.grid(row=1,column=0)
        self.cb2.grid(row=1,column=1)

        self.t1 = Treeview(self.p2, column=("appointmentid","patientid", "doctorid", "date", "slotid", "amount", "typeofbooking", "paymentrecieved", "token", "status",
        "diagonsis"))

        self.t1.heading("appointmentid", text="pateintid")
        self.t1.heading("patientid", text="pateint name")

        self.t1.heading("doctorid", text="doctor id")
        self.t1.heading("date", text="date")
        self.t1.heading("slotid", text="slot id")
        self.t1.heading("amount", text="amount")
        self.t1.heading("typeofbooking", text="type of booking")
        self.t1.heading("paymentrecieved", text="payment recieved")
        self.t1.heading("token", text="token")
        self.t1.heading("status", text="status")
        self.t1.heading("diagonsis", text="diagonsis")

        self.t1.column("appointmentid", width=70)
        self.t1.column("patientid", width=70)

        self.t1.column("doctorid",width=70)
        self.t1.column("date", width=70)
        self.t1.column("slotid", width=70)
        self.t1.column("amount", width=70)
        self.t1.column("typeofbooking",width=70)
        self.t1.column("paymentrecieved", width=70)
        self.t1.column("token",width=70)
        self.t1.column("status",width=70)
        self.t1.column("diagonsis", width=70)


        self.t1["show"] = "headings"
        self.textbox2=Entry(self.p3)
        self.textbox2.grid(row=4,column=0)
        self.bt2=Button(self.p3,text="done",command=self.done)
        self.bt2.grid(row=5,column=1)


        self.t1.pack()
        self.root.mainloop()
#........................................
