from http.client import HTTPConnection
from tkinter import Tk, Label, Button, Entry, simpledialog
from tkinter.messagebox import showinfo

from connectionfile import *
from doctorhome import *
from changepassword1 import *

class doctorlogin:
    def forget(self):
        answer = simpledialog.askstring("Input", "What is your registered mobile number", parent=self.root)
        if answer is not None:
            s = "select password from doctor where mobile='" + answer + "'"
            conn = Connect("127.0.0.1", "root", "", "opd")
            cr = conn.cursor()
            cr.execute(s)
            result = cr.fetchone()
            msg = "your password is " + str(result[0])
            mobileno = answer
            msg = msg.replace(' ', '%20')
            conn = HTTPConnection('server1.vmm.education')
            conn.request('GET',
                         '/VMMCloudMessaging/AWS_SMS_Sender?''username=rupinderkaur&password=DP46MD2M&message=' + msg + '&phone_numbers=' + mobileno)
            response = conn.getresponse()
            print(response.read())
        else:
            print("Enter mobile number")


    def __init__(self):
        self.root=Tk()
        self.root.geometry("400x400")
        self.lb=Label(self.root,text="doctor login")
        self.lb.grid(row=0,column=1)
        self.lb1=Label(self.root,text="email")
        self.lb1.grid(row=1,column=0)
        self.lb2=Label(self.root,text="password")
        self.lb2.grid(row=2,column=0)

        self.textbox1=Entry(self.root)
        self.textbox2=Entry(self.root,show="*")
        self.textbox1.grid(row=1,column=1)
        self.textbox2.grid(row=2,column=1)


        self.bt1=Button(self.root,text="login",command=self.login)
        self.bt1.grid(row=3,column=1)


        self.bt3=Button(self.root,text="forget password",command=self.forget)
        self.bt3.grid(row=4,column=1)

        self.root.mainloop()

    def login(self):
            conn = connectionfile.connect('')
            cr=conn.cursor()
            email=self.textbox1.get()
            password=self.textbox2.get()
            if email=="":
                showinfo(" ","enter email")
            elif password=="":
                showinfo(" ","enter password")

            else:
                s="select * from doctor where email='"+email+"' and password='"+password+"'"
                n=cr.execute(s)
                if n>0:
                    showinfo("","login successful")
                    doctorhome(email)
                    self.root.destroy()

                else:
                    showinfo("","login fail")





#..............................
