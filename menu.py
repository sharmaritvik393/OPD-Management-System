from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import askopenfile
from PIL import Image,ImageTk
from connectionfile import *
from shutil import copyfile
from os import path
from pathlib import Path
# pip install pyttsx3 pypiwin32
from tkinter import ttk
from pygame import mixer
from menu import *

from tkinter import *
from adddoctor import *
from addslot import *
from addstaff import *
from doctorappointments import *
from doctorlogin import *
from managestaff import *
from patientrecord import *
from patientscreen import *
from viewdoctor import *
from viewpatients import *
from viewstaff import *
from bookappointment import *
from stafflogin import *
from changepassword1 import *

class menu:
    def fire1(self):
        obj1=addstaff()
    def fire2(self):
        obj2=viewstaff()
    def fire3(self):
        obj3=managestaff()
    def fire4(self):
        obj4=stafflogin()
    def fire5(self):
        obj5=patientrecord()
    def fire6(self):
        obj6=viewpatients()
    def fire7(self):
        obj7=adddoctor()
    def fire8(self):
        obj8=viewdoctor()
    def fire9(self):
        obj9=addslot()
    def fire10(self):
        obj10=doctorappointments()
    def fire11(self):
        obj11=patientscreen()
    def fire12(self):
        obj12=doctorlogin()
    def fire13(self):
        obj13=bookappointment()

    def __init__(self):
        self.root=Tk()
        self.root.geometry("1024x800")
        self.mymenu=Menu(self.root)
        self.root.title("Welcome to My OPD Software")
        self.root.config(menu=self.mymenu)
        self.submenu1=Menu(self.mymenu,tearoff=False)
        self.mymenu.add_cascade(label="Manage Staff",menu=self.submenu1)
        self.submenu1.add_cascade(label="Add Staff", command=self.fire1)
        self.submenu1.add_cascade(label="View Staff",command=self.fire2)
        self.submenu1.add_cascade(label="Staff Information",command=self.fire3)

        self.submenu2 = Menu(self.mymenu, tearoff=False)
        self.mymenu.add_cascade(label="Manage patient", menu=self.submenu2)
        self.submenu2.add_cascade(label="Add patient", command=self.fire5)
        self.submenu2.add_cascade(label="View patient", command=self.fire6)

        self.submenu3 = Menu(self.mymenu, tearoff=False)
        self.mymenu.add_cascade(label="Manage doctor", menu=self.submenu3)
        self.submenu3.add_cascade(label="Add doctor", command=self.fire7)
        self.submenu3.add_cascade(label="View doctor", command=self.fire8)
        self.submenu3.add_cascade(label="Add slot", command=self.fire9)

        self.submenu4 = Menu(self.mymenu, tearoff=False)
        self.mymenu.add_cascade(label="Bookappointment", menu=self.submenu4)
        self.submenu4.add_cascade(label="Patient Screen", command=self.fire11)
        self.submenu4.add_cascade(label="Book Appointments", command=self.fire13)

        self.submenu5 = Menu(self.mymenu, tearoff=False)
        self.mymenu.add_cascade(label="Login", menu=self.submenu5)
        self.submenu5.add_cascade(label="Doctor Login", command=self.fire12)
        self.submenu5.add_cascade(label="Staff Login", command=self.fire4)

        self.root.mainloop()
#...................................



