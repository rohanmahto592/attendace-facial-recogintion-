from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import os
from gtts import gTTS
import time
class login():
    def __init__(self,root):
        self.root=root
        self.root.title("login system")
        self.root.geometry("1100x620+100+50")
        self.root.resizable(0,0)
        self.phone_image=ImageTk.PhotoImage(file="image2.jpg")
        self.images=ImageTk.PhotoImage(file="image2.jpg")
        self.lbl_phone_image=Label(self.root,image=self.phone_image,bd=0).place(x=70,y=100)
        self.bgs=Label(self.root,image=self.images).pack(side="bottom",fill="both",expand="no")

        mytext = ("welcome to login system")
        language = "en"
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save('welcome.mp3')
        os.system("open welcome.mp3")


        loginframe=Frame(self.root,bd=15,relief=SUNKEN,bg="gray")
        loginframe.place(x=450,y=50,width=410,height=500)
        self.username=StringVar()
        self.password=StringVar()
        title=Label(loginframe,text="Login System",font=("Helvetica",40,"bold italic"),bg="gray",fg="#00B0F0").place(x=0,y=30,relwidth=1)
        username=Label(loginframe,text="Username",font=("Helvetica",20,"bold italic"),bg="gray",fg="black").place(x=35,y=110)
        username=Entry(loginframe,textvariable=self.username,font=("Helvetica",15,"bold italic"),bg="#ECECEC").place(x=35,y=150,width=290)
        userpasswrd = Label(loginframe, text="Password", font=("Helvetica", 20, "bold italic"), bg="gray",fg="black").place(x=35, y=190)
        userpasswrd = Entry(loginframe,textvariable=self.password,show="*",font=("Helvetica", 15, "bold italic"), bg="#ECECEC").place(x=35, y=225, width=290)
        loginbutton=Button(loginframe,bd=5,text="Log In",command=self.login,font=("Arial Rounded MT Bold",35),bg="#00B0F0",activebackground="white",fg="#6fbbd3",activeforeground="white",cursor="hand2").place(x=35,y=280,width=290,height=40)
        hr=Label(loginframe,bg="red").place(x=37,y=345,width=290,height=3)
        orr=Label(loginframe,text="OR",bg="white").place(x=165,y=337)
        forget_btn=Button(loginframe,text="Forget Password",font=("Times New Roman",25,"italic"),bg="#00B0F0",cursor="heart",activebackground="red",fg="#6fbbd3",activeforeground="green",bd=0).place(x=88,y=370)

        self.im1=ImageTk.PhotoImage(file="house.png")
        self.im2 = ImageTk.PhotoImage(file="th-1.jpeg")
        self.im3 = ImageTk.PhotoImage(file="233463_full.png")
        self.im4 = ImageTk.PhotoImage(file="Animation-Transparent.png")
        self.im5 = ImageTk.PhotoImage(file="cartoon-business-man-free1.png")
        self.im6 = ImageTk.PhotoImage(file="Chibi-Free-Download-PNG.png")
        self.im7 = ImageTk.PhotoImage(file="book-1773756_640.png")

        self.lbl_change=Label(self.root,bg="gray")
        self.lbl_change.place(x=210,y=135,width=205,height=319)
        self.animate()
    def animate(self):
        self.im=self.im3
        self.im3=self.im2
        self.im2=self.im1
        self.im1=self.im4
        self.im4=self.im5
        self.im5=self.im6
        self.im6=self.im7
        self.im7=self.im
        self.lbl_change.config(image=self.im)
        self.lbl_change.after(2000,self.animate)


    def login(self):
        if self.username.get()=="" or self.password.get()=="":
            messagebox.showerror("Error","All Fields Are Required!!")
            mytext = ("Sorry all fields are required ")
            language = "en"
            myobj = gTTS(text=mytext, lang=language, slow=False)
            myobj.save('welcome.mp3')
            os.system("open welcome.mp3")
            os.remove("../welcome.mp3")

        elif self.username.get()!="Rohan" or self.password.get()!="123456":
            messagebox.showerror("Error","Invalid Username And Password\nTry again with correct credentials!!")
            mytext = ("please enter the valid username and password for authentication")
            language = "en"
            myobj = gTTS(text=mytext, lang=language, slow=False)
            myobj.save('welcome2.mp3')
            os.system("open welcome2.mp3")
            #os.remove("welcome2.mp3")
        else:
            messagebox.showinfo("Information",f"Welcome : {self.username.get()}\nYour Password : {self.password.get()}\nYou have logged in successfully!!")
            mytext = ("You Have been Logged in successfully in Your employee management system")
            language = "en"
            myobj = gTTS(text=mytext, lang=language, slow=False)
            myobj.save('welcome.mp3')
            os.system("open welcome.mp3")
            time.sleep(4)
            #os.remove("welcome.mp3")
            self.root.destroy()





root=Tk()
obj=login(root)
root.mainloop()