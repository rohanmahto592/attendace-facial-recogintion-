from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2
import csv
import mysql.connector
from gtts import gTTS
import os
import io
import time
import datetime
#import log2
import numpy as np
import pandas as pd
import re
import smtplib
from playsound import playsound
from threading import *


class Employee:
    def __init__(self,root):
        self.root=root
        self.root.title("Face recoginition|Employee Attendance System ")

        self.root.geometry("1350x700+0+0")

        title=Label(self.root,text="FACE RECOGINITION | EMPLOYEE ATTENDANCE SYSTEM",bd=20,relief=GROOVE,font=("times new roman",38,"bold italic"),bg="light blue",fg="black")
        title.pack(side=TOP,fill=X)

        ##all variables
        self.name = StringVar()
        self.id = IntVar()
        self.email = StringVar()
        self.phone = IntVar()
        self.gender = StringVar()
        self.dob = StringVar()
        self.job=StringVar()
        self.address = StringVar()
        self.search_by=StringVar()
        self.search_txt=StringVar()
        language = 'en'
        mytext = ("welcome to employeee attendance System")
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save('welcome2.mp3')
        # fh.close()
        os.system("open welcome2.mp3")
        ##manageframe
        def iexit():
            iexits=messagebox.askyesno("Employee attendance System","Do you really want to exit??")
            if iexits>0:
                root.destroy()
                return
        def clear():
            txt_roll.delete(0,END)
            employee_txt.delete(0,END)
            employee_phone_txt.delete(0,END)
            email_txt.delete(0,END)
            gender_txt.delete(0,END)
            date_of_birth_txt.delete(0,END)
            job_txt.delete(0,END)
            address_txt.delete(0,END)

        def adddata():
            sqlcoln=mysql.connector.connect(host='127.0.0.1',user='root',password="Rohan123$",database="newinfo")
            cur=sqlcoln.cursor()
            emailss = email_txt.get()
            genderss = gender_txt.get()
            if txt_roll.get()=='' or employee_txt.get()=='' or employee_phone_txt.get()=='' or email_txt.get()=='' or gender_txt.get()=='' or  date_of_birth_txt.get()=='' or job_txt.get()=='' or address_txt.get()=='':
                messagebox.showwarning("mandatory","All Fields Are Required!!")
            else:
                cur.execute("insert into details5 values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                    txt_roll.get(),
                    employee_txt.get(),
                    employee_phone_txt.get(),
                    email_txt.get(),
                    gender_txt.get(),
                    date_of_birth_txt.get(),
                    job_txt.get(),
                    address_txt.get()
                ))
                if not (re.match("[^@]+@[^@]+\.[^@]+",emailss)) or (re.match(genderss,"^M(ale)?$|^F(emale)?$|^O(thers)?$")):
                    messagebox.showinfo("email Error","please check your  email address, either '@' is missing or 'gmail.com'!!\n OR\n Check your gender section!!")

                else:
                    senderemail = "rohanmahto592@gmail.com"
                    senderpassword = "Rohan123.$"
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(senderemail, senderpassword)
                    if server:
                        messagebox.showinfo("Security","Login Successfully!!")
                        server.sendmail(senderemail,"komalmahto22@gmail.com","New details of employee added up!!")
                        messagebox.showinfo("Email","Email has been sent successfully to the authority!!")
                        sqlcoln.commit()
                        sqlcoln.close()
                        messagebox.showinfo("Employee Management System", "Record Has Been Saved Successfully")
                        language = 'en'

                        mytext = ("Record Has Been Saved Successfully in your database  and  displayed on window")
                        myobj = gTTS(text=mytext, lang=language, slow=False)
                        myobj.save('welcome2.mp3')

                        os.system("open welcome2.mp3")
                        displaydata()
                    else:
                        messagebox.showerror("Login Error","Connection Failed,Please connect again")


        def displaydata():
            sqlcoln = mysql.connector.connect(host='127.0.0.1', user='root', password="Rohan123$",database="newinfo")
            cur = sqlcoln.cursor()
            cur.execute("select * from details5")
            result=cur.fetchall()
            if len(result)!=0:
                employee_tree.delete(*employee_tree.get_children())
            for row in result:
                employee_tree.insert('',END,values=row)
                sqlcoln.commit()
            sqlcoln.close()

        def update():
            sqlcoln = mysql.connector.connect(host='127.0.0.1', user='root', password="Rohan123$", database="newinfo")
            cur = sqlcoln.cursor()
            cur.execute("update details5 set name=%s,phone=%s,email=%s,gender=%s,date_birth=%s,job=%s,address=%s where id=%s",(
                txt_roll.get(),
                employee_phone_txt.get(),
                email_txt.get(),
                gender_txt.get(),
                date_of_birth_txt.get(),
                job_txt.get(),
                address_txt.get(),
                employee_txt.get()

            ))
            sqlcoln.commit()

            clear()
            sqlcoln.close()

            messagebox.showinfo("Employee Management System", "Record Updated Successfully")
            mytext = ("record updated successfully in your database and updated data  has been displayed on your screen")
            language="en"
            myobj = gTTS(text=mytext, lang=language,slow=False)
            myobj.save('welcome2.mp3')
            # fh.close()
            os.system("open welcome2.mp3")
            senderemail = "rohanmahto592@gmail.com"
            senderpassword = "Rohan123.$"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(senderemail, senderpassword)
            messagebox.showinfo("Security", "Login Successfully!!")
            server.sendmail(senderemail, "kailashmahto735185@gmail.com", "An update has been done by the admin!!")
            messagebox.showinfo("Email", "Email,about the changes made by the admin has been sent successfully to the authority!!")
            displaydata()
        def learnersinfo(ev):
            viewinfo=employee_tree.focus()
            learnerdata=employee_tree.item(viewinfo)
            row=learnerdata['values']
            print(row)
            txt_roll.delete(0,END)
            txt_roll.insert(END,row[0])
            employee_txt.delete(0,END)
            employee_txt.insert(END,row[1])
            employee_phone_txt.delete(0,END)
            employee_phone_txt.insert(END,row[2])
            email_txt.delete(0,END)
            email_txt.insert(END,row[3])
            gender_txt.delete(0,END)
            gender_txt.insert(END,row[4])
            date_of_birth_txt.delete(0,END)
            date_of_birth_txt.insert(END,row[5])
            job_txt.delete(0,END)
            job_txt.insert(END,row[6])
            address_txt.delete(0,END)
            address_txt.insert(END,row[7])

            #mytext = ("all the details has been filled  in your employee details section")
            #language = "en"
            #myobj = gTTS(text=mytext, lang=language, slow=False)
            #myobj.save('welcome.mp3')
            # fh.close()
            #os.system("open welcome.mp3")





        def deletes():
            sqlcoln = mysql.connector.connect(host='127.0.0.1', user='root', password="Rohan123$", database="newinfo")
            cur = sqlcoln.cursor()
            cur.execute("delete from details5 where id=%s",(employee_txt.get(),))

            sqlcoln.commit()

            sqlcoln.close()
            messagebox.showinfo("Employee Management System", "Record successfully deleted,Thank you!!")
            clear()
            mytext = ("Record successfully deleted from your database ,Thank you!!")
            language = "en"
            myobj = gTTS(text=mytext, lang=language,slow=False)
            myobj.save('welcome2.mp3')
            # fh.close()
            os.system("open welcome2.mp3")
            senderemail = "rohanmahto592@gmail.com"
            senderpassword = "Rohan123.$"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(senderemail, senderpassword)
            messagebox.showinfo("Security", "Login Successfully!!")
            server.sendmail(senderemail, "komalmahto22@gmail.com", "One record  has been deleted by the admin!!")
            messagebox.showinfo("Email", "Email, about the changes made by the admin has been sent successfully to the authority!!")
            displaydata()
        def searchdata():
            sqlcoln = mysql.connector.connect(host='127.0.0.1', user='root', password="Rohan123$", database="newinfo")
            cur = sqlcoln.cursor()
            cur.execute("select * from details5 where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
            result = cur.fetchall()
            if len(result) != 0:
                employee_tree.delete(*employee_tree.get_children())
                for row in result:
                    employee_tree.insert('', END, values=row)
                sqlcoln.commit()
            sqlcoln.close()
            mytext = ("search completed  from your database ,Thank you!!")
            language = "en"
            myobj = gTTS(text=mytext, lang=language, slow=False)
            myobj.save('welcome2.mp3')
            # fh.close()
            os.system("open welcome2.mp3")
        def openfile():
            global result
            global my_image
            result=filedialog.askopenfilename(initialdir=os.getcwd(),title="Select file",filetypes=(("jpeg","*.jpg"),("PNG file","*.png"),("All Files","*.*")))
            print(result)
            my_image=Image.open(result)
            my_image.thumbnail((360,170))
            b=io.BytesIO()
            my_image.save(b,'gif')
            my_image=ImageTk.PhotoImage(my_image)
            label_frame.configure(image=my_image)
            label_frame.image=my_image
            if not result:
                exit()
            file=filedialog.asksaveasfilename(title="Select file for saving",defaultextension=".png",filetypes=(("jpeg","*.jpg"),("PNG file","*.png"),("All Files","*.*")))
            with open(file,'w') as f:
                f.write(result)


                f.close()
                messagebox.showinfo("File", "File Saved Successfully in Images Folder!!")
        def is_number(s):
            try:
                float(s)
                return True
            except ValueError:
                pass
            try:
                import unicodedata
                unicodedata.numeric(s)
                return True
            except (TypeError,ValueError):
                pass
            return False
        def sound():
            playsound('/Users/rohanmahto/PycharmProjects/pythonProject/dev/sorry.mp3')


        def TakeImages():
            id=(employee_txt.get())
            name=(txt_roll.get())
            if(is_number(id) and name.isalpha()):
                cam=cv2.VideoCapture(0)
                detector=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                samplenum=0
                while(True):
                    ret, img=cam.read()

                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=detector.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=5)

                    for(x,y,w,h) in faces:
                        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
                        samplenum=samplenum+1
                        cv2.imwrite("/Users/rohanmahto/PycharmProjects/pythonProject/Studss/TrainImage/"+name +'.'+id+'.'+str(samplenum)+".png",gray[y:y+h,x:x+h])
                        cv2.imshow('Frame',img)
                    if cv2.waitKey(20) & 0xFF == ord('q'):
                        break
                    elif samplenum>20:
                        break
                cam.release()
                cv2.destroyAllWindows()

                #message.configure(text=res)
                messagebox.showinfo(" Saved Image","Image Saved Successfully in your Database for Testing Purpose\n\n Thank You for your Time!!")
        def train_image():
            messagebox.showinfo("Tranning Process","Wait a While,Till Your Image Tranning Process Is Being Completed....!!!")

            recognizer=cv2.face.LBPHFaceRecognizer_create()
            detector=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            face,Id=getImagesAndLabels("/Users/rohanmahto/PycharmProjects/pythonProject/Studss/TrainImage/")
            recognizer.train(face,np.array(Id))
            recognizer.save("/Users/rohanmahto/PycharmProjects/pythonProject/dev/TranningImageLabel/trainner.yml")
            mytext = ("Image Training Processed has Been Completed , Thank you For Your Patience")
            language = "en"
            myobj = gTTS(text=mytext, lang=language, slow=False)
            myobj.save('welcome2.mp3')
            os.system("open welcome2.mp3")


        def getImagesAndLabels(path):
            imagepaths=[os.path.join(path,f) for f in os.listdir(path)]
            faces=[]
            ids=[]
            for imagepath in imagepaths:
                pilimage=Image.open(imagepath).convert("L")
                imagenp=np.array(pilimage,'uint8')
                id=int(os.path.split(imagepath)[-1].split(".")[1])
                faces.append(imagenp)
                ids.append(id)
            return faces,ids

        def track_image():
            recognizer = cv2.face.LBPHFaceRecognizer_create()
            recognizer.read("/Users/rohanmahto/PycharmProjects/pythonProject/dev/TranningImageLabel/trainner.yml")
            facecascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            eye_detect = cv2.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")

            font = cv2.FONT_HERSHEY_SIMPLEX

            col_names = ['Id', 'Name', 'Date', 'Time']
            attendance = pd.DataFrame(columns=col_names)
            cam=cv2.VideoCapture(0)
            while True:
                ret, img = cam.read()
                print(img)
                c=0
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = facecascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
                print(faces)
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)
                    roi_gray = gray[y:y + h, x:x + w]
                    roi_color = img[y:y + h, x:x + w]
                    eyes = eye_detect.detectMultiScale(roi_gray)
                    for (ex, ey, ew, eh) in eyes:
                        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 5)
                    Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
                    if (conf <50):
                        c=1;

                        ts = time.time()
                        date = datetime.datetime.fromtimestamp(ts).strftime('%y-%m-%d')
                        timestamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                        tt = str(Id)
                        dit=str(date)
                        times=str(timestamp)


                        cv2.putText(img,"ID-"+" "+ str(tt)+" "+ str(dit)+" "+str(times), (x, y + h), font,2, (255, 255, 255), 2)

                    else:
                        Id = "unknown"
                        tt = str(Id)
                        ts = time.time()
                        timestamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                        times = str(timestamp)

                        if (conf > 75):
                            c=0;
                            cv2.medianBlur(img[y:y + h, x:x + w], 35)
                            noOffile = len(os.listdir("../ImagesUnknown")) + 1
                            cv2.imwrite("/Users/rohanmahto/PycharmProjects/pythonProject/ImagesUnknown/Image/" + str(noOffile) + ".png", img[y:y + h, x:x + w])
                        cv2.putText(img,"Name-"+str(tt)+" "+str(times),(x,y+h),font,1,(255,255,255),2)
                        cv2.putText(img,"Warning!!",(x,y),font,2,(0,0,255),4)

                        xy=Thread(target=sound)
                        xy.start()
                        xy.join(timeout=7)




                cv2.imshow('Show', img)
                if cv2.waitKey(100) & 0xFF == ord('q'):
                    break


            ts = time.time()
            date = datetime.datetime.fromtimestamp(ts).strftime('%y-%m-%d')
            timestamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
            Hour, Minute, Second = timestamp.split(":")
            row=['ID','TIME','DATE',Id,timestamp,date]

            cam.release()

            if c==1:

                with open("Stud\datetime.csv", 'a+') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerow(row)
                csvFile.close()

                cv2.destroyAllWindows()
                messagebox.showinfo("Identification","You Are a Member of the  Rohan's Software Company....Thank You For Being the part of our Company!!")

            else:
                cv2.destroyAllWindows()



        manageframe=Frame(self.root,bd=15,relief=RIDGE,bg="gray")
        manageframe.place(x=10,y=94,width=615,height=700)
        m_title=Label(manageframe,text="Employee Details",bd=10,relief=RIDGE,font=("times new roman",20,"bold italic"),fg="white",bg="gray")
        m_title.grid(row=0,columnspan=2,padx=120,pady=5)
        lbl_roll=Label(manageframe,text="Name(Mr./Mrs./Km.):",font=("times new roman",20,"bold italic"),fg="black",bg="gray")
        lbl_roll.grid(row=1,column=0,padx=8,pady=8,sticky="w")
        txt_roll=Entry(manageframe,textvariable=self.name,bd=8,relief=GROOVE,justify=CENTER,font=("times new roman",20,"italic"))
        txt_roll.grid(row=1,column=1,padx=8,pady=8,sticky="w")
        #### image frame
        label_frame=Label(manageframe,bd=14,relief=GROOVE,bg="gray")
        label_frame.place(x=450,y=10,width=127,height=200)

        employee_id = Label(manageframe, text="Employee ID :", font=("times new roman", 20, "bold italic"), fg="black",bg="gray")
        employee_id.grid(row=2, column=0, padx=8, pady=8, sticky="w")
        employee_txt = Entry(manageframe,textvariable=self.id, bd=8, relief=GROOVE,justify=CENTER, font=("times new roman", 20, "italic"))
        employee_txt.grid(row=2, column=1, padx=8, pady=8, sticky="w")

        employee_phone = Label(manageframe, text="Phone No :", font=("times new roman", 20, "bold italic"), fg="black",bg="gray")
        employee_phone.grid(row=3, column=0, padx=8, pady=8, sticky="w")
        employee_phone_txt = Entry(manageframe,textvariable=self.phone, bd=8, relief=GROOVE, justify=CENTER,font=("times new roman", 20, "italic"))
        employee_phone_txt.grid(row=3, column=1, padx=8, pady=8, sticky="w")
        employee_phone_txt.columnconfigure(0, weight=10)
        employee_phone_txt.grid_propagate(False)


        email = Label(manageframe, text="Email Id :", font=("times new roman", 20, "bold italic"), fg="black",bg="gray")
        email.grid(row=4, column=0, padx=8, pady=8, sticky="w")
        email_txt = Entry(manageframe,textvariable=self.email, bd=8, relief=GROOVE,justify=CENTER, font=("times new roman", 20, "italic"))
        email_txt.grid(row=4, column=1, padx=8, pady=8, sticky="w")
        email_txt.columnconfigure(0,weight=10)
        email_txt.grid_propagate(False)

        gender = Label(manageframe, text="Gender :", font=("times new roman", 20, "bold italic"), fg="black",bg="gray")
        gender.grid(row=5, column=0, padx=8, pady=8, sticky="w")
        gender_txt=Entry(manageframe,textvariable=self.gender,bd=8,relief =GROOVE,font=("times new roman",20,"italic"),justify=CENTER)
        gender_txt.grid(row=5,column=1,padx=8,pady=8,sticky="w")

        date_of_birth = Label(manageframe, text="D.O.B :", font=("times new roman", 20, "bold italic"), fg="black",bg="gray")
        date_of_birth.grid(row=6, column=0, padx=8, pady=8, sticky="w")
        date_of_birth_txt = Entry(manageframe,textvariable=self.dob, bd=8, relief=GROOVE,justify=CENTER ,font=("times new roman", 20, "italic"))
        date_of_birth_txt.grid(row=6, column=1, padx=8, pady=8, sticky="w")

        job_title = Label(manageframe, text="Job Title :", font=("times new roman", 20, "bold italic"), fg="black",bg="gray")
        job_title.grid(row=7, column=0, padx=8, pady=8, sticky="w")
        job_txt = Entry(manageframe, textvariable=self.job, bd=8, relief=GROOVE, justify=CENTER,font=("times new roman", 20, "italic"))
        job_txt.grid(row=7, column=1, padx=8, pady=8, sticky="w")

        address = Label(manageframe, text="Address :", font=("times new roman",20, "bold italic"), fg="black",bg="gray")
        address.grid(row=8, column=0, padx=8, pady=8, sticky="w")
        address_txt = Entry(manageframe, bd=8, relief=GROOVE,justify=CENTER, font=("times new roman", 20, "italic"))
        address_txt.grid(row=8, column=1, padx=8, pady=8, sticky="w")
        address_txt.columnconfigure(0,weight=10)
        address_txt.grid_propagate(False)



        ##button frame
        btnframe = Frame(manageframe, bd=10, relief=GROOVE, bg="gray")
        btnframe.place(x=10, y=570, width=550,height=87)
        addbtn=Button(btnframe,text="Add",bd=10,relief=GROOVE,width=10,font=("times new roman",15, "italic"),command=adddata).grid(row=0,column=0,padx=10,pady=6)
        clrbtn = Button(btnframe, text="Clear", bd=10, relief=GROOVE, width=10,font=("times new roman", 15, "italic"),command=clear).grid(row=0, column=1, padx=10, pady=6)
        updatebtn = Button(btnframe, text="Update", bd=10, relief=GROOVE, width=10,font=("times new roman", 15, "italic"),command=update).grid(row=0, column=2, padx=10, pady=6)
        clrallbtn = Button(btnframe, text="Delete", bd=10, relief=GROOVE, width=10,font=("times new roman", 15, "italic"),command=deletes).grid(row=0, column=3, padx=10, pady=6)
        trainbtn = Button(btnframe, text="Take Image", bd=10, relief=GROOVE, width=10,font=("times new roman", 15, "italic"),command=TakeImages).grid(row=0, column=4, padx=10, pady=6)
        testnbtn = Button(btnframe, text="Train Image", bd=10, relief=GROOVE, width=10,font=("times new roman", 15, "italic"),command=train_image).grid(row=1, column=1, padx=10, pady=6)
        showbtn = Button(btnframe, text="Show Data", bd=10, relief=GROOVE, width=10,font=("times new roman", 15, "italic"),command=displaydata).grid(row=1, column=0, padx=10, pady=6)
        exitnbtn = Button(btnframe, text="Track Image", bd=10, relief=GROOVE, width=10,font=("times new roman", 15, "italic"),command=track_image).grid(row=1, column=2, padx=10, pady=6)
        browsebtn=Button(manageframe,text="Add Image",width=10,font=("times new roman", 15, "italic"),command=openfile).place(x=470,y=220)
        trackbtn=Button(btnframe,text="Exit",width=10,font=("times new roman", 15, "italic"),command=iexit).grid(row=1,column=3,padx=10,pady=6)
        #detail frame
        detailsframe = Frame(self.root,bd=15, relief=RIDGE, bg="gray")
        detailsframe.place(x=630, y=94, width=800, height=700)
        search_label=Label(detailsframe,text="Search By :",fg="orange",font=("times new roman",18,"bold italic"))
        search_label.grid(row=0,column=0,padx=10,pady=3,sticky="w")
        combo_search = ttk.Combobox(detailsframe,textvariable=self.search_by, font=("times new roman",18, "italic"), state="readonly")
        combo_search['values'] = ("name", "id","Phone","email","gender","job")
        combo_search.grid(row=0, column=1, padx=8, pady=8, sticky="w")
        entrys = Entry(detailsframe,textvariable=self.search_txt, bd=5, relief=GROOVE, justify=CENTER,font=("times new roman",15, "italic"))
        entrys.grid(row=0, column=2, padx=8, pady=8, sticky="w")
        searchbtn = Button(detailsframe, text="Search", bd=15, relief=GROOVE, width=10,font=("times new roman", 18, "italic"),command=searchdata).grid(row=0, column=3, padx=10, pady=6)
        showallbtn = Button(detailsframe, text="Show All", bd=15, relief=GROOVE, width=10,font=("times new roman", 18, "italic"),command=displaydata).grid(row=0, column=4, padx=10, pady=6)
        ## table frame
        table_frame=Frame(detailsframe,bd=10,relief=GROOVE,bg="gray")
        table_frame.place(x=10,y=55,width=740,height=600)
        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        employee_tree=ttk.Treeview(table_frame,columns=("Name","employee Id","phone","email","gender","dob","job title","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=employee_tree.xview)
        scroll_y.config(command=employee_tree.yview)
        employee_tree.heading("Name",text="Name(Mr./Mrs./Km.)")
        employee_tree.heading("employee Id", text="Employee ID")
        employee_tree.heading("phone", text="Phone No")
        employee_tree.heading("email", text="Email Id")
        employee_tree.heading("gender", text="Gender")
        employee_tree.heading("dob", text="D.O.B")
        employee_tree.heading("job title", text="Job Title")
        employee_tree.heading("address", text="Address")
        employee_tree['show'] = 'headings'

        employee_tree.column("Name",width=150)
        employee_tree.column("employee Id", width=110)
        employee_tree.column("phone", width=150)
        employee_tree.column("email", width=250)
        employee_tree.column("gender", width=100)
        employee_tree.column("dob", width=120)
        employee_tree.column("job title", width=170)
        employee_tree.column("address", width=260)
        employee_tree.pack(fill=BOTH,expand=1)
        employee_tree.bind("<ButtonRelease-1>",learnersinfo)
        displaydata()

root=Tk()
ob=Employee(root)
root.mainloop()