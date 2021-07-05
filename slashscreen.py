from menu import *
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


class splashscreen:
    def start(self):
        self.progress1["value"] = 0
        self.maxbytes = 100
        self.progress1["maximum"] = 100
        self.read_bytes()
    def read_bytes(self):
        '''simulate reading 500 bytes; update progress bar'''
        self.bytes += 1
        abc = "Loading.... (" + str(self.bytes // 1) + "%)"
        self.lb_blank.config(text=abc)
        self.progress1["value"] = self.bytes
        if self.bytes < self.maxbytes:
            # read more bytes after 100 ms
            self.root.after(50, self.read_bytes)
        else:
            mixer.music.stop()
            self.root.destroy()

            # make obj of screen youj want to open after it

            # x = viewcategories()
            x=menu()


    def __init__(self):
        self.root=Tk()
        #root=Tk()
        #photo = PhotoImage(file="images/dp.jpg")
        #kjk=Label(self.root,image=photo)
        #kjk.pack()
        # self.root.geometry("{0}x{0}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        # self.root.resizable(0, 0)
        def showImg(self):
            load = Image.open("images/dp.jpg")
            render = ImageTk.PhotoImage(load)

            # labels can be text or images
            img = Label(self, image=render)
            img.image = render
            img.place(x=0, y=0)


        self.root.attributes('-fullscreen',True)
        mixer.init()

        # for any background music


        # mixer.music.load('images/a.mp3')
        # mixer.music.play()

        # for any background music


        self.root.config(background="#FFA500")
        self.a = Image.open("images/dp.jpg").resize((800, 700), Image.ANTIALIAS)
        dp = ImageTk.PhotoImage(self.a)
        Label(self.root,image=dp,bg='#FFA500').pack()
        self.lb_blank = Label(self.root, text="",bg="white")


        #ImageTk.PhotoImage(Image.open("images/dp.jpg"))
        #photo.pack()
        #kjk = Label(root,image=photo)

        self.progress1 = ttk.Progressbar(self.root, orient="horizontal", length=400, mode="determinate")
        self.lb_blank.pack()
        self.progress1.pack()
        self.bytes = 0
        self.start()
        self.root.mainloop()
x=splashscreen()
