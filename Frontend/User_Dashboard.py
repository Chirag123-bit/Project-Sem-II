from tkinter import *

from PIL import ImageTk, Image
from tkinter import  ttk
import Backend.DBConnect

class user_login():
    """Student's personal window where they can view their result. They don't have any administrative control over them.
    Students can only view their result and can not do anything to change the result."""
    def __init__(self,root,user):
        self.root = root
        self.root.geometry("915x453+345+100")
        self.root.config(bg="black")
        self.root.resizable("False", "False")
        self.usr_oid = user

        self.Reg_fonts = ('Helvetica', 12)
        self.sft_img = ImageTk.PhotoImage(Image.open("Images/softwarica.png"))  # Placing image inside label
        self.wel = LabelFrame(self.root, bg="black", highlightbackground="black", highlightcolor="black")
        self.wel.pack(side="top", fill="x")  # Creating frames which will hold college's logo
        self.logo_img = Label(self.wel, image=self.sft_img, bg="black")
        self.logo_img.pack(fill="both", expand=3)
        logo_img = ImageTk.PhotoImage(Image.open("Images/Student2.png"))  # Importing logo
        self.std_log = Label(self.wel, image=logo_img, bg="black")
        self.std_log.place(x=0, y=0)  # Placing logo on left
        self.std_log1 = Label(self.wel, image=logo_img, bg="black")
        self.root.iconbitmap('Images/logo.ico')

        self.lbl = LabelFrame(self.root, text="Student Record", highlightcolor="Green",
                              highlightbackground="Grey", highlightthickness=3, bg="Black", fg="blue", width=561,
                              height=700)
        self.lbl.pack(side="right",fill=X)

        self.lbl2 = LabelFrame(self.root, text="Student Detail", highlightcolor="Green",
                               highlightbackground="Grey", highlightthickness=3, bg="Black", fg="blue", width=661,
                               height=750)
        self.lbl2.pack(side="left",fill=X)

        self.lbl4 = LabelFrame(self.lbl)
        self.lbl4.grid(row=4, column=2, columnspan=3, rowspan=3)



        ttk.Button(self.root,text="Exit",command=self.ext).place(x=350,y=420,width=150, height=35)

        self.lables_and_entries("Math", 1, 0)
        self.lables_and_entries("Science", 2, 0)
        self.lables_and_entries("Nepali", 3, 0)
        self.lables_and_entries("English", 4, 0)
        self.lables_and_entries("Social", 5, 0)
        self.lables_and_entries("Computer", 6, 0)
        self.lables_and_entries("EPH", 7, 0)
        self.lables_and_entries("Geography", 8, 0)
        #####################################################RESULT ENTRY###############################################################
        self.Mth = Entry(self.lbl, font=('Verdana', 12), bg="black", fg="white",width=18)
        self.Mth.grid(row=1, column=1,sticky=NSEW)
        self.Sci = Entry(self.lbl, font=('Verdana', 12), bg="black", fg="white",width=18)
        self.Sci.grid(row=2, column=1,sticky=NSEW)
        self.Nep = Entry(self.lbl, font=('Verdana', 12), bg="black", fg="white",width=18)
        self.Nep.grid(row=3, column=1,sticky=NSEW)
        self.Eng = Entry(self.lbl, font=('Verdana', 12), bg="black", fg="white",width=18)
        self.Eng.grid(row=4, column=1,sticky=NSEW)
        self.Soc = Entry(self.lbl, font=('Verdana', 12), bg="black", fg="white",width=18)
        self.Soc.grid(row=5, column=1,sticky=NSEW)
        self.Com = Entry(self.lbl, font=('Verdana', 12), bg="black", fg="white",width=18)
        self.Com.grid(row=6, column=1,sticky=NSEW)
        self.EP = Entry(self.lbl, font=('Verdana', 12), bg="black", fg="white",width=18)
        self.EP.grid(row=7, column=1,sticky=NSEW)
        self.Geo = Entry(self.lbl, font=('Verdana', 12), bg="black", fg="white",width=18)
        self.Geo.grid(row=8, column=1,sticky=NSEW)
        #####################################################Personal Label#############################################
        self.detail_label("First Name: ", 1, 0)
        self.detail_label("Last Name: ", 2, 0)
        self.detail_label("User Name: ", 3, 0)
        self.detail_label("Class: ", 4, 0)
        self.detail_label("Section: ", 5, 0)
        self.detail_label("Gender: ", 6, 0)
        self.detail_label("Date of Birth: ", 7, 0)
        self.detail_label("Email Address: ", 8, 0)

        #####################################################Personal Entries###############################################################
        self.f_name = Entry(self.lbl2, font=('Verdana', 14), bg="black", fg="white",width=23)
        self.f_name.grid(row=1, column=1,sticky=NSEW)
        self.l_name = Entry(self.lbl2, font=('Verdana', 14), bg="black", fg="white",width=23)
        self.l_name.grid(row=2, column=1,sticky=NSEW)
        self.u_name = Entry(self.lbl2, font=('Verdana', 14), bg="black", fg="white",width=23)
        self.u_name.grid(row=3, column=1,sticky=NSEW)
        self.cls = Entry(self.lbl2, font=('Verdana', 14), bg="black", fg="white",width=23)
        self.cls.grid(row=4, column=1,sticky=NSEW)
        self.sec = Entry(self.lbl2, font=('Verdana', 14), bg="black", fg="white",width=23)
        self.sec.grid(row=5, column=1,sticky=NSEW)
        self.gender = Entry(self.lbl2, font=('Verdana', 14), bg="black", fg="white",width=23)
        self.gender.grid(row=6, column=1,sticky=NSEW)
        self.DOB = Entry(self.lbl2, font=('Verdana', 14), bg="black", fg="white",width=23)
        self.DOB.grid(row=7, column=1,sticky=NSEW)
        self.e_add = Entry(self.lbl2, font=('Verdana', 14), bg="black", fg="white",width=23)
        self.e_add.grid(row=8, column=1,sticky=NSEW)

        #####################################################RESULT Frame###############################################################
        self.lbl3 = LabelFrame(self.lbl, text="Result", highlightcolor="Green", highlightbackground="Grey",
                               highlightthickness=3, bg="Black", fg="blue",width=150,height=110)
        self.lbl3.grid(row=1, column=2, rowspan=6,sticky=NSEW)
        self.lbl4 = LabelFrame(self.lbl, highlightcolor="Green", highlightbackground="Grey",
                               highlightthickness=3, bg="Black",width=150,height=120)
        self.lbl4.grid(row=7, column=2, rowspan=2,sticky=NSEW)

        address_label = Label(self.wel, text="Dillibazar, Kathmandu", font=8, bg="black", fg="blue")
        address_label.place(x=335, y=80)
        rpt_crd = Label(self.root, text="Report Card", font=60, bg="black", fg="blue2")
        rpt_crd.place(x=380, y=115)

        self.db = Backend.DBConnect.DBConnect()

        self.DataBase_Calls()
        self.root.mainloop()
    def ext(self):
        """Exits this window"""
        self.root.destroy()

    def lables_and_entries(self, Text, X, Y):
        """Creates labels for subjects
        Here,
        Text = Text to display on label
        X= Row of widget
        Y= Column of widget"""
        Label(self.lbl, text=Text, justify=LEFT, compound=LEFT, font=10, bg="black", fg="white",width=12).grid(row=X, column=Y)

    def detail_label(self, Text, X, Y):
        """Creates labels for personal informations
                Here,
                Text = Text to display on label
                X= Row of widget
                Y= Column of widget"""
        Label(self.lbl2, text=Text, justify=LEFT, compound=LEFT, font=12, bg="black", fg="white").grid(row=X, column=Y,sticky=NSEW)

    def DataBase_Calls(self):
        """This window wil fetch their result on the basis of the username and OID of the student"""

        query = ("""SELECT * FROM grades WHERE UserName =%s""")
        values = [self.usr_oid]
        records = self.db.select(query,values)

        query="select * from user_info where UserName = %s"
        values=[self.usr_oid]
        per_rec = self.db.select(query,values)
        for marks in records:
            self.root.title(marks[0] + " " + marks[0] + "'s Report Card")
            self.Mth.insert(0, marks[1])
            self.Sci.insert(0, marks[2])
            self.Nep.insert(0, marks[3])
            self.Eng.insert(0, marks[4])
            self.Soc.insert(0, marks[5])
            self.Com.insert(0, marks[6])
            self.EP.insert(0, marks[7])
            self.Geo.insert(0, marks[8])
            ###############################Personal Details#####################################
        for record2 in per_rec:
            self.f_name.insert(0, record2[0])
            self.l_name.insert(0, record2[1])
            self.u_name.insert(0, record2[4])
            self.cls.insert(0, record2[-3])
            self.sec.insert(0, record2[-2])
            if record2[-1] == "Mr.":
                self.gender.insert(0, "Male")
            else:
                self.gender.insert(0, "Female")

            self.DOB.insert(0, record2[5])
            self.e_add.insert(0, record2[2])

        Total = marks[-2]

        self.Mth["state"] = DISABLED
        self.Sci["state"] = DISABLED
        self.Nep["state"] = DISABLED
        self.Eng["state"] = DISABLED
        self.Soc["state"] = DISABLED
        self.Com["state"] = DISABLED
        self.EP["state"] = DISABLED
        self.Geo["state"] = DISABLED

        self.f_name["state"] = DISABLED
        self.l_name["state"] = DISABLED
        self.u_name["state"] = DISABLED
        self.cls["state"] = DISABLED
        self.sec["state"] = DISABLED
        self.DOB["state"] = DISABLED
        self.gender["state"] = DISABLED
        self.e_add["state"] = DISABLED


        total_label = Label(self.lbl3, text=("Total:::: ") , anchor=W,
                            padx=0, font=12, bg="black", fg="white")
        total_label.grid(row=0, column=0,sticky=W)
        Tot = Label(self.lbl3, text=str(Total), font=('Helvetica', 15), bg="black", fg="white",justify=CENTER,anchor=CENTER)
        Tot.grid(row=1,column=0)


        Percentage_label = Label(self.lbl3, text= "\n"+str(("Percentage:: ")), anchor=W,
                                 padx=0, font=12, bg="black", fg="white")
        Percentage_label.grid(row=4, column=0)

        Percen = Label(self.lbl3, text=str(Total / 8),
                                  font=('Helvetica', 15), bg="black", fg="white",justify=CENTER,anchor=CENTER)
        Percen.grid(row=5,column=0,rowspan=2)
        Label(self.lbl4, text="Result:", font=('Helvetica', 16), bg="black", fg="white").pack()
        if (Total / 8) > 80 and (Total / 8) < 100:
            Label(self.lbl4, text="Distinction", font=('Helvetica', 20), fg="green", bg="black").pack()
            Tot.config(fg="green")
            Percen.config(fg="green")
        elif (Total / 8) > 60 and (Total / 8) < 80:
            Label(self.lbl4, text="First Division", font=('Helvetica', 16), fg="orange", bg="black").pack()
            Tot.config(fg="orange")
            Percen.config(fg="orange")
        elif (Total / 8) > 50 and (Total / 8) < 60:
            Label(self.lbl4, text="Second Division", font=('Helvetica', 16), fg="blue", bg="black").pack()
            Tot.config(fg="blue")
            Percen.config(fg="blue")
        elif (Total / 8) > 40 and (Total / 8) < 50:
            Label(self.lbl4, text="Third Division", font=('Helvetica', 16), fg="yellow", bg="black").pack()
            Tot.config(fg="yellow")
            Percen.config(fg="yellow")
        else:
            Label(self.lbl4, text="Fail", font=('Helvetica', 16), fg="red", bg="black").pack()
            Tot.config(fg="red")
            Percen.config(fg="red")