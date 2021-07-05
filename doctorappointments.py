from tkinter import Tk, PanedWindow, Button, Label
from tkinter.messagebox import showinfo
from tkinter.ttk import Treeview

from tkcalendar import DateEntry

from connectionfile import *

from reportlab.lib.pagesizes import A5
from reportlab.pdfgen import canvas

import subprocess
import random


class doctorappointments:

    def generatepdf(self):
        name = str(random.randint(0, 100))
        name_pdf = str("doctorbills//a" + str(name) + ".pdf")
        my_canv = canvas.Canvas(name_pdf, pagesize=A5)
        my_canv.setFont('Helvetica', 14)
        my_canv.setLineWidth(.2)
        y = 580
        my_canv.drawString(160, y, 'Doctor Bills')
        my_canv.line(10, y - 3, 400, y - 3)

        my_canv.setFont('Helvetica', 10)
        my_canv.drawString(30, y - 12, "Appointment Id")
        my_canv.drawString(130, y - 12, "Patient Name")
        my_canv.drawString(230, y - 12, "Slot Id")
        my_canv.drawString(330, y - 12, "Fee Amount")
        y = y - 12
        my_canv.line(10, y - 3, 400, y - 3)
        my_canv.setFont('Helvetica', 8)
        y = y - 3
        s = []
        q = "select *from appointment where doctorid='" + str(self.doctorid) + "' and date='" + str(
            self.textbox1.get_date()) + "' and status='done'"

        conn = connectionfile.connect('')
        cr = conn.cursor()

        cr.execute(q)
        result = cr.fetchall()
        for row in result:
            lst=[]
            pid=row[1]
            print(str(pid))
            q2="select patientname  from patientrecord where patientid='"+str(pid)+"'"
            cr.execute(q2)
            rs=cr.fetchone()
            pname=rs[0]
            lst.append(row[0])
            lst.append(pname)
            lst.append(row[4])
            lst.append(row[5])
            s.append(lst)
        tp=0.0


        for i in range(0, len(s)):
            print(s[i][0])
            my_canv.drawString(30, y - 12, str(s[i][0]))
            my_canv.drawString(130, y - 12, str(s[i][1]))
            my_canv.drawString(230, y - 12, str(s[i][2]))
            my_canv.drawString(330, y - 12, str(s[i][3]))
            tp=tp+(float)(s[i][3])
            y = y - 12
        my_canv.line(10, y - 3, 400, y - 3)
        y = y - 3
        my_canv.drawString(230, y - 12, "Total Bill")
        my_canv.drawString(330, y - 12, str(tp))
        my_canv.save()
        subprocess.Popen([name_pdf], shell=True)
        showinfo('','pdf report saved at '+str("doctorbills//a" + str(name) + ".pdf"))

    def show(self):
        self.t1.delete(*self.t1.get_children())
        print("dddd "+str(self.textbox1.get_date())+"  "+str(self.doctorid))
        s = "select * from appointment where doctorid='"+str(self.doctorid)+"' and date='"+str(self.textbox1.get_date())+"' and status='done'"

        conn = connectionfile.connect('')
        cr = conn.cursor()

        cr.execute(s)
        result = cr.fetchall()
        i = 0
        for row in result:
            self.t1.insert("", index=i, values=row)
            i = i + 1

    def __init__(self,did):
        conn = connectionfile.connect('')
        cr = conn.cursor()
        q="select doctorid from doctor where email='"+did+"'"

        cr.execute(q)
        result = cr.fetchone()
        self.doctorid=result[0]
        self.root = Tk()
        self.root.geometry("800x800")

        self.p1 = PanedWindow(self.root)
        self.p2 = PanedWindow(self.root)
        self.p3 = PanedWindow(self.root)

        self.p1.pack()
        self.p2.pack()
        self.p3.pack()

        self.lb1 = Label(self.p1, text="enter appointment")
        self.lb1.grid(row=0,column=0)
        self.textbox1=DateEntry(self.p1)
        self.textbox1.grid(row=0,column=1)
        self.bt1=Button(self.p1,text="search",command=self.show)
        self.bt1.grid(row=0,column=2)


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
        self.bt2=Button(self.p3,text="pdf",command=self.generatepdf)
        self.bt2.grid(row=5,column=2)

        self.t1.pack()
        self.root.mainloop()
#........................................
