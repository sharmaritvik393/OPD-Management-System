from http.client import HTTPConnection
from tkinter import Tk, Label, Entry, Button, simpledialog
from tkinter.messagebox import showinfo

from connectionfile import *
from staffhome import *


class stafflogin:
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
    def login(self):
        email=str(self.textbox1.get())
        if str(self.textbox1.get()).count("@")!=1:
            showinfo("","invalid email address")
        if str(self.textbox1.get()).count(".com")!=1:
            showinfo("", "invalid email address")


        else:
            s="select * from staff where email = '" + self.textbox1.get()+"' and password= '"+self.textbox2.get()+"'"
            conn = connectionfile.connect('')
            cr = conn.cursor()
            n=cr.execute(s)
        if n>0:
            showinfo("","login succesfull")
            self.root.destroy()
            staffhome(email)
        else:
            showinfo("","login fail")
    def forget(self):
        answer=simpledialog.askstring("Input","What is your registered mobile number",parent=self.root)
        if answer is not None:
            s = "select password from staff where mobile='" +answer + "'"
            conn=Connect("127.0.0.1","root","","opd")
            cr = conn.cursor()
            cr.execute(s)
            result = cr.fetchone()
            msg = "your password is "+str(result[0])
            mobileno = answer
            msg = msg.replace(' ', '%20')
            conn = HTTPConnection('server1.vmm.education')
            conn.request('GET','/VMMCloudMessaging/AWS_SMS_Sender?''username=&password=&message=' + msg + '&phone_numbers=' + mobileno)
            response = conn.getresponse()
            print(response.read())
        else:
            print("Enter mobile number")

    def __init__(self):
        self.root=Tk()
        self.root.geometry("400x400")

        self.lb1=Label(self.root,text="enter email")
        self.textbox1=Entry(self.root)
        self.lb2=Label(self.root,text="enter password")
        self.textbox2=Entry(self.root,show="*")

        self.lb1.grid(row=0,column=0)
        self.lb2.grid(row=1,column=0)

        self.textbox1.grid(row=0,column=1)
        self.textbox2.grid(row=1,column=1)

        self.bt1=Button(self.root,text="login",command=self.login)
        self.bt1.grid(row=2,column=1)
        self.bt2=Button(self.root,text="forget password",command=self.forget)
        self.bt2.grid(row=3,column=1)


        self.root.mainloop()
#............................
