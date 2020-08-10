import sqlite3
from tkinter import *

from PIL import ImageTk, Image
from tkinter import messagebox, ttk
import smtplib
from email.message import EmailMessage
from tkcalendar import *
import re
from abc import ABC, abstractmethod



class TKWindow():
    def __init__(self):
        self.root = Tk()
        self.root.title("Login Page")
        self.root.geometry("1067x600+230+40")  # Defining screen size of our app
        self.root.iconbitmap('Images/logo.ico')
        self.Reg_fonts = ('Helvetica', 12)
        self.sft_img = ImageTk.PhotoImage(Image.open("Images/softwarica.png"))
        self.wel = LabelFrame(self.root, bg="black", highlightbackground="black", highlightcolor="black")
        self.wel.pack(side="top", fill="x")
        self.logo_img = Label(self.wel, image=self.sft_img, bg="black")
        self.logo_img.pack(fill="both", expand=3)
        logo_img = ImageTk.PhotoImage(Image.open("Images/Student2.png"))
        self.std_log = Label(self.wel, image=logo_img, bg="black")
        self.std_log.place(x=0, y=0)
        self.std_log1 = Label(self.wel, image=logo_img, bg="black")
        self.root.iconbitmap('Images/logo.ico')

    def switch_class(self,name=None):
        self.new_class = name
        if name is not None:
            self.new_class()

        else:
            self.root.destroy()




class Login(TKWindow):

    def __init__(self):
        super().__init__()
        self.ttk = ttk
        self.root1 = self.root
        self.root1.resizable(False, False)
        ######################################################Images#################################################
        image = ImageTk.PhotoImage(Image.open("Images/Root_Backgroung.jpg"))  # adding background image in root
        abc = Label(self.root1, image=image)  # Placing the image file inside the label
        abc.place(x=0, y=0, relwidth=1, relheight=1)  # place enables to write over a label
        self.frame = LabelFrame(self.root1, width=550, height=200, text="Login", relief=RAISED, bd=1,
                                highlightcolor="blue", fg="blue",
                                highlightbackground="Black", highlightthickness=5)
        self.frame.place(x=328, y=190)
        self.user_ico = ImageTk.PhotoImage(Image.open("Images/Login_image.png"))
        User_label = Label(self.frame, image=self.user_ico)
        User_label.grid(row=0, column=0)
        self.password_icon = ImageTk.PhotoImage(Image.open("Images/Password_image.png"))
        Password_Label = Label(self.frame, image=self.password_icon)
        Password_Label.grid(row=4, column=0)
        self.student_icon = ImageTk.PhotoImage(Image.open("Images/Student3.png"))
        std_label = Label(self.root1, image=self.student_icon, bg="blue", fg="gray10")
        std_label.place(x=482, y=59)
        self.Reg = ImageTk.PhotoImage(Image.open("Images/Register.png"))
        usr_reg = Label(self.root1, image=self.Reg)
        usr_reg.place(x=332, y=346)
        self.logn = ImageTk.PhotoImage(Image.open("Images/Login.png"))
        logn_img = Label(self.root1, image=self.logn)
        logn_img.place(x=620, y=346)

        ######################################################Buttons And Labels##################################################
        self.button_font = ('Verdana', 15)
        self.labels("UserName", 0, 3)
        self.labels("Password", 4, 3)
        self.usr1 = StringVar("")
        self.pass1 = StringVar("")
        self.entry()

        self.lbl = ttk.Label(self.root1, text="Student Login System", font=self.button_font, background="white",
                             foreground="blue")
        self.lbl.place(x=420, y=25)

        self.button("Login", 10, 0, 654, 346, "log")
        self.button("Register", 11, 0, 366, 346, "reg")
        self.butn = Button(self.frame, text="Forgot Password?", fg="blue", anchor="e", command=self.show_pass).grid(
            row=5, column=7, sticky="E")
        abz = ImageTk.PhotoImage(Image.open("Images/Forgot_pass.png"))
        for_pas_img = Label(self.frame, image=abz)
        for_pas_img.place(x=282, y=105)
        ######################################################Root1 Mainloop##################################################
        self.root1.mainloop()

    def labels(self, Text, x, y):
        b = Label(self.frame, text=Text, font=self.button_font, anchor=W, width=8,
                  fg="blue")
        b.grid(row=x, column=y, sticky=W)
        c = Label(self.frame, text="")
        c.grid(row=0, column=6)
        d = Label(self.frame, text="")
        d.grid(row=2, column=0)
        e = Label(self.frame, text="")
        e.grid(row=3, column=0)

        g = Label(self.frame, text="")
        g.grid(row=5, column=0)

    def button(self, text_, x, y, ab, cd, comm):
        if comm == "log":
            but = ttk.Button(self.root1, text=text_,
                             command=self.button_pressed_login, padding=6
                             )
            but.place(x=ab, y=cd)
        else:
            but = ttk.Button(self.root1, text=text_, padding=6,
                             command=self.button_pressed_register)
            but.place(x=ab, y=cd)

    def entry(self):
        global pas
        usr = ttk.Entry(self.frame, font=self.button_font, text=self.usr1)
        usr.grid(row=0, column=7)
        pas = ttk.Entry(self.frame, font=self.button_font, text=self.pass1, show="*")
        pas.grid(row=4, column=7)

    def button_pressed_register(self):
        self.root1.destroy()
        TKWindow.switch_class(TKWindow,Register)

    def button_pressed_login(self):
        global usr_oid, rs_pas, rs_eml, rs_usrnm

        if self.usr1.get() == "root" and self.pass1.get() == "root":
            self.root1.destroy()
            TKWindow.switch_class(TKWindow,Admin_login)

        elif self.usr1.get() == "root" and self.pass1.get() != "root":
            messagebox.showerror("Error", "Please enter a valid password!")
            pas.delete(0, END)

        else:
            conn = sqlite3.connect("Login_Data.db")
            c = conn.cursor()

            find_user = ("SELECT *,oid FROM Data WHERE user_name = ? AND password =? ")
            c.execute(find_user, [(self.usr1.get()), (self.pass1.get())])
            result = c.fetchall()

            if result:
                for i in result:
                    usr_oid = i[17]
                    rs_pas = i[1]
                    rs_eml = i[3]
                    rs_usrnm = i[4]
                    messagebox.showinfo("Welcome", "Welcome  " + str(i[13]) + str(i[0]) + " " + str(i[2]))
                    self.root1.destroy()
                    TKWindow.switch_class(TKWindow,user_login)

            else:
                if len(self.usr1.get()) != 0 and len(self.pass1.get()) != 0:
                    msg = messagebox.askokcancel("Invalid Credentials", "Please Re-check your login details")

                    if msg == True:
                        self.pass1.set("")
                    else:
                        messagebox.showwarning("Message", "Exiting Program")
                        self.root1.destroy()

                else:
                    messagebox.showerror("Required Fields Missing", "Please Enter your Credentials")

    def show_pass(self):
        global em_entr, un_entr, submt, pass_entry, record123
        self.rs_win = Toplevel(self.root1)
        em_lbl = Label(self.rs_win, text="Enter Email Address::: ").grid(row=0, column=0)
        un_lbl = Label(self.rs_win, text="Enter User Name::: ").grid(row=1, column=0)
        em_entr = Entry(self.rs_win, font=('Verdana', 12))
        em_entr.grid(row=0, column=1)
        un_entr = Entry(self.rs_win, font=('Verdana', 12))
        un_entr.grid(row=1, column=1)
        sub_btn = Button(self.rs_win, text="Submit",
                         command=lambda: Database.checking_cred(Database, em_entr.get(), un_entr.get()))
        sub_btn.grid(row=2, column=1)
        lebl = Label(self.rs_win, text="Enter New Password::: ")
        lebl.grid(row=3, column=0)
        pass_entry = Entry(self.rs_win, state=DISABLED, font=('Verdana', 12))
        pass_entry.grid(row=3, column=1)
        submt = Button(self.rs_win, text="Update Password", state=DISABLED)
        submt.grid(row=4, column=0)


    def check(self):
        pass_entry["state"] = NORMAL
        submt["state"] = NORMAL
        submt["command"] = lambda: Database.replce_pass(Database, pass_entry.get())





class Register(TKWindow):
    """Here, Phone Number is changed into User Name"""

    def __init__(self):
        global img, F_Name, L_Name, E_Add, Passwd, Phone, Passwd2, DoB
        super().__init__()
        self.wel.pack_forget()
        self.root2 = self.root
        self.root2.geometry("960x600+200+0")
        self.root2.title("Softwarica College Registration Form")
        self.root2.resizable("False", "False")
        back_img = ImageTk.PhotoImage(Image.open("Images/Reg_Back.jpg"))
        img = Label(self.root, image=back_img)
        img.place(x=0, y=0, relwidth=1, relheight=1)

        self.sft_img = ImageTk.PhotoImage(Image.open("Images/softwarica.png"))
        self.wel = LabelFrame(self.root2, bg="SteelBlue1", highlightbackground="blue", highlightcolor="black")
        self.wel.pack(side="top", fill="x")
        self.logo_img = Label(self.wel, image=self.sft_img, bg="SteelBlue1")
        self.logo_img.pack(fill="both", expand=3)

        logo_img = ImageTk.PhotoImage(Image.open("Images/Student2.png"))
        self.std_log = Label(self.wel, image=logo_img, bg="SteelBlue1")
        self.std_log.place(x=0, y=0)
        self.std_log12 = Label(self.wel, image=logo_img, bg="SteelBlue1").place(y=0, x=850)

        address_label = Label(self.wel, text="Dillibazar, Kathmandu", font=13, bg="SteelBlue1", fg="blue2")
        address_label.place(x=395, y=80)
        F_Name = StringVar("")
        L_Name = StringVar("")
        E_Add = StringVar("")
        Passwd = StringVar("")
        Phone = StringVar("")
        Passwd2 = StringVar("")
        DoB = StringVar("")
        Label(self.root2, text="Softwarica College Registration Form", font=45, width=30,
              ).place(x=305,
                              y=114)
        self.Reg_scrn("First Name", 100, 180, 220, 180, F_Name)
        self.Reg_scrn("Last Name", 495, 180, 616, 180, L_Name)

        self.Reg_scrn("Email Address", 100, 280, 220, 280, E_Add)
        self.Reg_scrn("Password", 495, 280, 616, 280, Passwd)

        self.Reg_scrn("User Name No:", 100, 380, 220, 380, Phone)
        self.Reg_scrn("Confirm Pass", 495, 380, 616, 380, Passwd2)
        Button(self.root2, text="Date Of Birth", command=self.reg_cal).place(x=100, y=480)
        self.dob_entry = Entry(self.root2, font=self.Reg_fonts)
        self.dob_entry.place(x=220, y=480)

        self.Reg_fonts = ('Helvetica', 12)

        self.root2.mainloop()

    def Reg_scrn(self, Text, X, Y, a, b, var):
        global suffix, entry1, grade, section
        labls = Label(self.root2, text=Text, font=self.Reg_fonts, anchor=NW, width=12, borderwidth=2, relief="ridge",
                      justify="center")
        labls.place(x=X, y=Y)
        if Text == "Password" or Text == "Confirm Pass":
            entry1 = ttk.Entry(self.root2, font=self.Reg_fonts, text=Text, textvariable=var, show="*",
                               justify="center")
            entry1.place(x=a, y=b)

        else:
            entry = ttk.Entry(self.root2, font=self.Reg_fonts, text=Text, textvariable=var, justify="center")
            entry.place(x=a, y=b)

        choices = ["Mr.", "Mr.", "Mrs.", "Miss."]
        suffix = StringVar(self.root2)
        suffix.set("Mr")

        Label(self.root2, text="Class", font=self.Reg_fonts, anchor=NW, borderwidth=2, width=5, relief="ridge",
              justify="center").place(x=495, y=480)
        choices1 = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        grade = StringVar(self.root2)
        grade.set(1)

        Label(self.root2, text="Section", font=self.Reg_fonts, anchor=NW, borderwidth=2, width=7, relief="ridge",
              justify="center").place(x=612, y=480)
        choices2 = ["A", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        section = StringVar(self.root2)
        section.set("A")

        optbox = ttk.OptionMenu(self.root2, suffix, *choices)
        optbox.place(x=423, y=167)
        optgrade = ttk.OptionMenu(self.root2, grade, *choices1)
        optgrade.place(x=550, y=480)

        optsec = ttk.OptionMenu(self.root2, section, *choices2)
        optsec.place(x=686, y=480)

        buttnreg = ttk.Button(self.root2, text="Register", padding=8,
                              command=self.submit)
        buttnreg.place(x=505, y=550)
        buttncanc = ttk.Button(self.root2, text="Cancle", padding=8,
                               command=self.root2.destroy)
        buttncanc.place(x=300, y=550)

    def reg_cal(self):
        global caln, cal_frame, btn
        cal_frame = Frame(self.root2).pack()
        caln = Calendar(cal_frame, selectmode="day", year=2020, month=6, day=12)
        caln.pack()

        btn = Button(cal_frame, text="Save Date", font=self.Reg_fonts, anchor=NW, width=12, borderwidth=2,
                     relief="ridge",
                     justify="center", command=self.placing_dob)
        btn.pack()

    def placing_dob(self):
        self.dob_entry.delete(0, END)
        self.dob_entry.insert(0, caln.get_date())
        caln.destroy()
        btn.destroy()

    def submit(self):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+@gmail.com$'  # This is regex(regular expression) expression
        # Here ^ and $ suggests beggining and end of lime
        # 
        # Establishing the connection To database
        conn = sqlite3.connect("Login_Data.db")
        # Creating cursor to add or retrive data from DB
        c = conn.cursor()
        ver = (re.search(regex, E_Add.get()))
        find_user = ("SELECT * FROM Data WHERE user_name = ? ")
        c.execute(find_user, [(Phone.get())])
        result = c.fetchall()
        if result:
            messagebox.showerror("Invalid Username", "This username is already taken. Please enter another username.")

        elif Passwd.get() == Passwd2.get() and (
                len(F_Name.get()) != 0 and len(L_Name.get()) != 0 and len(Passwd.get()) != 0 and len(
            E_Add.get()) != 0 and len(Phone.get()) != 0 and len(Passwd2.get()) != 0) and ver != None:
            # Inserting Data into DB
            c.execute(
                """INSERT INTO Data VALUES(:f_name,:password,:l_name,:e_address,:user_name,:Maths,:Science,:Nepali,
                :English,:Social,:Computer,:EPH,:Geography,:suffix,:DOB,:Class,:Section) """,
                {
                    "f_name": F_Name.get(),
                    "password": Passwd.get(),
                    "l_name": L_Name.get(),
                    "e_address": E_Add.get(),
                    "user_name": Phone.get(),
                    "Maths": 0,
                    "Science": 0,
                    "Nepali": 0,
                    "English": 0,
                    "Social": 0,
                    "Computer": 0,
                    "EPH": 0,
                    "Geography": 0,
                    "suffix": suffix.get(),
                    "DOB": self.dob_entry.get(),
                    "Class": grade.get(),
                    "Section": section.get()
                })

            # Commiting Changes
            conn.commit()
            # Closing Connection
            conn.close()
            messagebox.showinfo("Sucess", "User Added")
            self.root2.destroy()
            Login()


        elif Passwd.get() != Passwd2.get():
            messagebox.showerror("Invalid Password", "Please Re-check your Password!!")
            entry1.delete(0, END)
        elif ver == None:
            messagebox.showerror("Invalid Email", "Please enter a valid Email Address!")




        else:
            messagebox.showerror("Required Field Missing", "Please Fill all the given fields!!")


class Database(ABC):
    def __init__(self):
        # Establishing the connection To database
        self.conn = sqlite3.connect("Login_Data.db")
        # Creating cursor to add or retrive data from DB
        self.c = self.conn.cursor()


        # Creating Tables for DB
    @abstractmethod
    def creating_db(self):
        self.c.execute("""CREATE TABLE Data(
                           First_Name text,
                           password text,
                           Last_Name text,
                           Email_Address text,
                           user_name text,
                           Maths integer DEFAULT 0 NOT NULL,
                           Science integer DEFAULT 0 NOT NULL,
                           Nepali integer DEFAULT 0 NOT NULL,
                           English integer DEFAULT 0 NOT NULL,
                           Social integer DEFAULT 0 NOT NULL,
                           Computer integer DEFAULT 0 NOT NULL,
                           EPH integer DEFAULT 0 NOT NULL,
                           Geography integer DEFAULT 0 NOT NULL,
                           suffix integer,
                           DOB integer,
                           Class text,
                           Section text



                           )""")

        # Commiting Changes
        self.conn.commit()
        # Closing Connection
        self.conn.close()

    def checking_cred(self, eml, usrnm):
        global ur_oid
        self.conn = sqlite3.connect("Login_Data.db")
        self.c = self.conn.cursor()
        find_user = ("SELECT *,oid FROM Data WHERE Email_Address = ? AND user_name =? ")
        self.c.execute(find_user, [eml, usrnm])
        result = self.c.fetchall()

        if result:
            print("Sucess")
            for i in result:
                ur_oid = i[17]
            Login.check(Login)
        else:
            messagebox.showerror("Invalid Credentials", "Please verify your Email/Username")


    def replce_pass(self, new_pass):
        self.conn = sqlite3.connect("Login_Data.db")
        self.c = self.conn.cursor()
        self.c.execute("""UPDATE Data SET
                    password = :passwd

                    WHERE oid =:oid """,
                       {
                           "passwd": new_pass,

                           "oid": ur_oid
                       })
        self.conn.commit()
        # Closing Connection
        self.conn.close()
        messagebox.showinfo("Sucess", "Password Updated! \n Please close this window to proceed.")


    def Delete(self, oid_list, oid_num):
        conn = sqlite3.connect("Login_Data.db")
        c = conn.cursor()
        id = int(oid_num)
        print(id)
        if id in oid_list:
            c.execute("""DELETE from Data WHERE oid =  """ + str(id))
            conn.commit()
            conn.close()
            messagebox.showinfo("Sucess", "User Deleted")
            Admin_login.refresh(Admin_login)


        else:
            messagebox.showerror("Failed", "Please Enter a Valid OID!")


class Admin_login(TKWindow):
    def __init__(self):
        super().__init__()
        global oid_num, Mth, Sci, Nep, Eng, Soc, Com, EP, Geo, root3, email_add
        self.root3 = self.root
        root3 = self.root3
        self.root3.geometry("1160x750+200+0")
        self.root3.resizable(False, False)
        self.root3.config(bg="black")
        self.root3.title("Admin Pannel")

        self.__useremail = "collegeproject961@gmail.com"
        self.__userpass = "Abcde@12345"


        self.del_btn = ttk.Button(self.root3, text="Delete Record", state=DISABLED)
        self.del_btn.place(x=955, y=585, width=200, height=50)

        self.address_label = Label(self.wel, text="Dillibazar, Kathmandu", font=10, bg="black", fg="white")
        self.address_label.place(x=469, y=80)
        logo_img = ImageTk.PhotoImage(Image.open("Images/Student2.png"))
        std_log = Label(self.wel, image=logo_img, bg="black")
        std_log.place(x=0, y=0)
        self.std_log1 = Label(self.wel, image=logo_img, bg="black")
        self.std_log1.place(x=1050, y=0)
        ttk.Button(self.root3,text="Exit",command=self.ext).place(x=960,y=700,width=200, height=50)

        self.dark_value = StringVar(value="On")
        self.dark_frm = LabelFrame(self.root3, text="Dark Mode", bg="black", fg="white")
        self.dark_frm.place(x=542, y=585, width=206, height=115)
        self.Dark_modelbl = Label(self.dark_frm, text="Dark Mode:", font=4, bg="black", fg="white")
        self.Dark_modelbl.pack()
        self.col = ("black", "white")
        R1 = Radiobutton(self.dark_frm, text="Off", variable=self.dark_value, value=("black", "white"), font=3,
                         bg="grey",
                         fg="black", indicatoron=0, width=10, command=self.reg_mode)
        R1.pack()
        R2 = Radiobutton(self.dark_frm, text="On", variable=self.dark_value, value=("white", "black"), justify=LEFT,
                         font=3, bg="grey", fg="black", indicatoron=0, width=10, command=self.dark_mode)
        R2.pack()

        self.welcome = Label(self.root3, text="Admin's Control Panel", bg="black", fg="white", font=('chiller', 30),
                             width=25)
        self.welcome.place(x=390, y=120)
        self.oooid = Label(self.root3, text="Student's OID::", font=15, bg="black", fg="white")
        self.oooid.place(x=765, y=560)
        self.search = Entry(self.root3, font=self.Reg_fonts)
        self.search.place(x=610, y=460, height=30)
        ttk.Button(self.root3, text="Search", command=self.search_lst).place(x=800, y=460, width=200, height=30)
        ttk.Button(self.root3, text="Reset", command=self.query).place(x=1010, y=460, width=150, height=30)
        self.eee = Label(self.root3, text="F/L Name", bg="black", fg="white", font=10)
        self.eee.place(x=515, y=462)

        self.oid_num = ttk.Entry(self.root, font=self.Reg_fonts)
        self.oid_num.insert(0, "Double tap on names above")
        self.oid_num["state"] = DISABLED
        self.oid_num.place(x=920, y=560)

        self.lbl = LabelFrame(self.root3, text="Student Record", highlightcolor="Green",
                              highlightbackground="Grey", highlightthickness=3, bg="Black", fg="gold", height=287,
                              width=310)
        self.lbl.place(x=0, y=170)
        self.lbl.pack_propagate(False)

        Mth, Sci, Nep, Eng, Soc, Com, EP, Geo = StringVar(""), StringVar(""), StringVar(""), StringVar(""), StringVar(
            ""), StringVar(""), StringVar(""), StringVar("")
        self.lbl2 = LabelFrame(self.lbl, highlightcolor="Red",
                               highlightbackground="grey", highlightthickness=3, bg="black", fg="green")

        self.lbl2.grid(row=2, column=2, rowspan=6, columnspan=6)

        self.lables_and_entries("Math", 1, 0, 1, 1, Mth, "black", "white")
        self.lables_and_entries("Science", 2, 0, 2, 1, Sci, "black", "white")
        self.lables_and_entries("Nepali", 3, 0, 3, 1, Nep, "black", "white")
        self.lables_and_entries("English", 4, 0, 4, 1, Eng, "black", "white")
        self.lables_and_entries("Social", 5, 0, 5, 1, Soc, "black", "white")
        self.lables_and_entries("Computer", 6, 0, 6, 1, Com, "black", "white")
        self.lables_and_entries("EPH", 7, 0, 7, 1, EP, "black", "white")
        self.lables_and_entries("Geography", 8, 0, 8, 1, Geo, "black", "white")
        ttk.Button(self.root3, text="Update Marks", command=self.updating_values).place(x=180, y=462, width=200,
                                                                                        height=43)
        self.updt1 = ttk.Button(self.root3, text="Update Info", command=self.updating_info, state=DISABLED)
        self.updt1.place(x=750, y=585, width=200, height=50)
        self.send_btn = ttk.Button(self.root3, text="Send E-mail", command=self.__Gmail_msg, state=DISABLED)
        self.send_btn.place(x=340, y=585, width=200, height=50)
        self.msg_frm = LabelFrame(self.root3, bg="white")
        self.msg_frm.place(x=0, y=510)
        to_lbl = Label(self.msg_frm, text="To: ", font=('Verdana', 12), anchor=E).grid(row=0, column=0, sticky=W)
        self.eml_add_lbl = Entry(self.msg_frm, font=('Verdana', 12), state=DISABLED, justify=LEFT, width=25)
        self.eml_add_lbl.grid(row=0, column=1, sticky=SW)
        self.txt_box = Text(self.msg_frm, height=13, width=40, bg="black", fg="chartreuse2")
        self.txt_box.grid(row=1, column=0, columnspan=2)
        mssg = open("Default_message", "r")
        self.txt_box.insert(END, mssg.read())


        self.f_name1 = StringVar()
        self.l_name1 = StringVar()
        self.u_name1 = StringVar()
        self.cls1 = StringVar()
        self.sec1 = StringVar()
        self.gender1 = StringVar()
        self.DOB1 = StringVar()
        self.e_add1 = StringVar()
        self.txt_box["state"] = DISABLED
        self.query()
        self.Oid_box()

        self.root3.mainloop()

    def ext(self):
        self.root3.destroy()
        Login()

    def dark_mode(self):
        self.col = ("black", "white")
        self.root3.config(bg="black")
        self.lbl.config(bg="black", fg="white")
        self.Dark_modelbl.config(bg="black", fg="white")
        self.dark_frm.config(bg="black", fg="white")
        self.wel.destroy()
        self.wel = LabelFrame(self.root, bg="black", highlightbackground="black", highlightcolor="black")
        self.wel.pack(side="top", fill="x")
        self.logo_img = Label(self.wel, image=self.sft_img, bg="black")
        self.logo_img.pack(fill="both", expand=3)
        self.logo_img = ImageTk.PhotoImage(Image.open("Images/Student2.png"))
        self.std_log = Label(self.wel, image=self.logo_img, bg="black")
        self.std_log.place(x=0, y=0)
        self.std_log1 = Label(self.wel, image=self.logo_img, bg="black")
        self.std_log1.place(x=1050,y=0)
        self.address_label = Label(self.wel, text="Dillibazar, Kathmandu", font=10, bg="black", fg="white")
        self.address_label.place(x=469, y=80)

        self.usr_ent.config(bg="black", fg="white")
        self.usr_lbl1.config(bg="black", fg="white")
        self.welcome.config(bg="black", fg="white")
        self.search.config(bg="white", fg="black",font=15)
        self.eee.config(bg="black", fg="white")
        self.oooid.config(bg="black", fg="white")
        self.txt_box.config(bg="black", fg="chartreuse2")

        self.lables_and_entries("Math", 1, 0, 1, 1, Mth, "black", "white")
        self.lables_and_entries("Science", 2, 0, 2, 1, Sci, "black", "white")
        self.lables_and_entries("Nepali", 3, 0, 3, 1, Nep, "black", "white")
        self.lables_and_entries("English", 4, 0, 4, 1, Eng, "black", "white")
        self.lables_and_entries("Social", 5, 0, 5, 1, Soc, "black", "white")
        self.lables_and_entries("Computer", 6, 0, 6, 1, Com, "black", "white")
        self.lables_and_entries("EPH", 7, 0, 7, 1, EP, "black", "white")
        self.lables_and_entries("Geography", 8, 0, 8, 1, Geo, "black", "white")

        self.lbl2.config(bg="black", fg="white")
        self.usr_lbl.config(bg="black", fg="white")
        try:
            self.lbl2.grid_forget()
            self.lbl2.grid(row=2, column=2, rowspan=6, columnspan=6)
            self.Percentage_label.grid_forget()
            self.Percentage_label.grid(row=5, column=2, rowspan=2)
            self.total_label.config(bg="black", fg="white")
            self.pert.config(bg="black", fg="white")
            self.Percentage_label.config(bg="black")
        except:
            pass

    def reg_mode(self):
        self.col = ("snow", "black")
        self.root3.config(bg="seashell")
        self.lbl.config(bg="azure2", fg="black")
        self.dark_frm.config(bg="snow", fg="black")
        self.Dark_modelbl.config(bg="snow", fg="black")
        self.usr_ent.config(bg="azure2", fg="black")
        self.usr_lbl1.config(bg="azure2", fg="black")
        self.welcome.config(bg="seashell", fg="black")
        self.search.config(bg="light yellow", fg="orange2",font=15)
        self.eee.config(bg="white", fg="black")
        self.oooid.config(bg="white", fg="black")
        self.wel.destroy()
        self.wel = LabelFrame(self.root3, bg="snow", highlightbackground="snow", highlightcolor="snow")
        self.wel.pack(side="top", fill="x")
        self.logo_img = Label(self.wel, image=self.sft_img, bg="snow")
        self.logo_img.pack(fill="both", expand=3)
        self.logo_img = ImageTk.PhotoImage(Image.open("Images/Student2.png"))
        std_log22 = Label(self.wel,image=self.logo_img,bg="snow",fg="blue")
        std_log22.place(x=0, y=0)
        std_log111 = Label(self.wel,image=self.logo_img,bg="snow",fg="blue")
        std_log111.place(x=1050, y=0)
        self.address_label = Label(self.wel, text="Dillibazar, Kathmandu", font=10, bg="snow", fg="blue")
        self.address_label.place(x=469, y=78)

        self.lables_and_entries("Math", 1, 0, 1, 1, Mth, "azure2", "black")
        self.lables_and_entries("Science", 2, 0, 2, 1, Sci, "azure2", "black")
        self.lables_and_entries("Nepali", 3, 0, 3, 1, Nep, "azure2", "black")
        self.lables_and_entries("English", 4, 0, 4, 1, Eng, "azure2", "black")
        self.lables_and_entries("Social", 5, 0, 5, 1, Soc, "azure2", "black")
        self.lables_and_entries("Computer", 6, 0, 6, 1, Com, "azure2", "black")
        self.lables_and_entries("EPH", 7, 0, 7, 1, EP, "azure2", "black")
        self.lables_and_entries("Geography", 8, 0, 8, 1, Geo, "azure2", "black")

        self.lbl2.config(bg="snow", fg="black")
        self.usr_lbl.config(bg="azure2", fg="black")
        try:
            self.lbl2.grid_forget()
            self.lbl2.grid(row=2, column=2, rowspan=6, columnspan=6)
            self.Percentage_label.grid_forget()
            self.Percentage_label.grid(row=5, column=2, rowspan=2)
            self.total_label.config(bg="snow", fg="black")
            self.Percentage_label.config(bg="snow")
            self.pert.config(bg="snow", fg="black")
        except:
            pass
        self.txt_box.config(bg="old lace", fg="gray0")

    def query(self):
        global Name_list, oid_list
        self.search.delete(0, END)
        self.frm = LabelFrame(self.root3, text="User's Details", highlightcolor="Green",
                              highlightbackground="Blue", highlightthickness=3, fg="green", bg="#ffffaa", width=561,
                              height=287)
        self.frm.place(x=598, y=170)
        self.frm.pack_propagate(False)

        self.treeview = ttk.Treeview(self.frm, columns=(1, 2, 3, 4, 5, 6, 7), show="headings",
                                     style='Calendar.Treeview', selectmode="extended")
        self.treeview.bind('<Double-Button-1>', self.getrow)
        my_scrl = Scrollbar(self.frm, orient=HORIZONTAL, command=self.treeview.xview)
        my_scrl2 = Scrollbar(self.frm, orient=VERTICAL, command=self.treeview.yview)
        self.treeview.config(xscrollcommand=my_scrl.set)
        self.treeview.config(yscrollcommand=my_scrl2.set)
        my_scrl.pack(side=BOTTOM, fill=X)
        my_scrl2.pack(side=RIGHT, fill=Y)
        self.treeview.pack(fill=BOTH, expand=YES)

        ###########################################Configuring Scrollbar#############################

        self.treeview.heading(1, text="OID", anchor="sw")
        self.treeview.column(1, minwidth=0, width=40, stretch=False)
        self.treeview.heading(2, text="First Name", anchor="sw")
        self.treeview.column(2, minwidth=0, width=100, stretch=False)
        self.treeview.heading(3, text="Last Name", anchor="sw")
        self.treeview.column(3, minwidth=0, width=100, stretch=False)
        self.treeview.heading(4, text="Class", anchor="sw")
        self.treeview.column(4, minwidth=0, width=100, stretch=False)
        self.treeview.heading(5, text="Section", anchor="sw")
        self.treeview.column(5, minwidth=0, width=100, stretch=False)
        self.treeview.heading(6, text="User Name", anchor="sw")
        self.treeview.column(6, minwidth=0, width=100, stretch=False)
        self.treeview.heading(7, text="Email Address", anchor="sw")
        self.treeview.column(7, minwidth=0, width=200)

        conn = sqlite3.connect("Login_Data.db")
        c = conn.cursor()
        c.execute("""SELECT *,oid FROM Data""")
        records = c.fetchall()
        print_record = ""
        Name_list = list()
        oid_list = list()
        for record in records:
            self.treeview.insert("", "end",
                                 values=(
                                 record[17], record[0], record[2], record[15], record[16], record[4], record[3]))
            abcde = record[0] + " " + record[2]
            Name_list.append(abcde)
            bcd = record[17]
            oid_list.append(bcd)

        Label(self.frm, text=print_record).pack(side="left")

        conn.commit()
        conn.close()

    def lables_and_entries(self, Text, X, Y, A, B, vari, col, col1):
        self.usr_lbl1 = Label(self.lbl, text=Text, justify=LEFT, compound=LEFT, font=10, bg=col, fg=col1)
        self.usr_lbl1.grid(row=X, column=Y)
        self.usr_lbl = Label(self.lbl, text="Select a Student:", justify=LEFT, compound=LEFT, padx=10, font=10,
                             bg="black",
                             fg="white")
        self.usr_lbl.grid(row=0, column=0)
        self.usr_ent = Entry(self.lbl, textvariable=vari, font=('Verdana', 12), bg=col, fg=col1)
        self.usr_ent.grid(row=A, column=B)

    def getrow(self, event):
        try:
            item = self.treeview.item(self.treeview.focus())
            self.f_name1.set(item["values"][1])
            self.l_name1.set(item["values"][2])
            self.u_name1.set(item["values"][5])
            self.cls1.set(item["values"][3])
            self.sec1.set(item["values"][4])
            self.e_add1.set(item["values"][6])
            self.oid_num["state"] = NORMAL
            self.oid_num.delete(0, END)
            self.oid_num.insert(0, item["values"][0])
            self.oid_num["state"] = DISABLED
            self.updt1["state"] = NORMAL
            self.del_btn["state"] = NORMAL
        except IndexError:
            print("Please Select a student from this list.")




    def Oid_box(self):
        global stud_name, Name_list, oid_entry
        stud_name = StringVar("")
        stud_name.set("Select a Student")
        stud_name.trace("w", self.opt_call)
        optmen = OptionMenu(self.lbl, stud_name, *Name_list)
        optmen.grid(row=0, column=1)
        oid_entry = Entry(self.lbl, font=('Verdana', 12), bg="white", fg="black")
        oid_entry.grid(row=0, column=2, padx=0, pady=0)

        self.del_btn["command"] = lambda: Database.Delete(Database, oid_list, self.oid_num.get())

    def search_lst(self):
        value = self.search.get()
        conn = sqlite3.connect("Login_Data.db")
        c = conn.cursor()
        query = """SELECT oid,  First_Name,  Last_Name, Class, Section, user_name, Email_Address FROM Data WHERE
                    First_Name LIKE ? OR Last_Name LIKE ? OR Class LIKE ? OR Section LIKE ?"""
        c.execute(query, [value, value, value, value])
        rows = c.fetchall()
        if rows:
            self.treeview.delete(*self.treeview.get_children())
            for ii in rows:
                self.treeview.insert("", "end", values=ii)
            conn.close()
        else:
            messagebox.showinfo("User Not Found",
                                "No student with First/Last name " + value + " or Class/Section " + value +
                                " found in our records")

    def opt_call(self, *args):

        oid_entry["state"] = NORMAL
        oid_entry.delete(0, END)
        stud_index = (Name_list.index((stud_name.get())))
        oid_entry.insert(0, oid_list[stud_index])
        oid_entry["state"] = DISABLED
        try:
            self.Percentage_label.grid_forget()
        except:
            pass

        self.showing_values_in_entries()

    def showing_values_in_entries(self):
        global Total, email_add
        self.txt_box["state"] = NORMAL
        self.send_btn["state"] = NORMAL
        oid = oid_entry.get()
        conn = sqlite3.connect("Login_Data.db")
        c = conn.cursor()
        c.execute("""SELECT * FROM Data WHERE OID =""" + oid)
        records = c.fetchall()
        for marks in records:
            email = marks[3]
            Mth.set(marks[5])
            Sci.set(marks[6])
            Nep.set(marks[7])
            Eng.set(marks[8])
            Soc.set(marks[9])
            Com.set(marks[10])
            EP.set(marks[11])
            Geo.set(marks[12])
        email_add = email

        conn.close()
        Total = (int(Mth.get()) + int(Sci.get()) + int(Nep.get()) + int(Eng.get()) + int(Soc.get()) + int(
            Com.get()) + int(EP.get()) + int(Geo.get()))

        self.total_label = Label(self.lbl2,
                                 text=("    Total::             " + "\n" + "            " + str(Total)) + '\n',
                                 justify=LEFT, compound=LEFT,
                                 padx=0, font=4, bg=self.col[0], fg=self.col[1])
        self.total_label.grid(row=1, column=2, rowspan=2)
        self.pert = Label(self.lbl2, text="Percentage:: ", justify=LEFT, compound=LEFT, padx=0, font=4, bg=self.col[0],
                          fg=self.col[1])
        self.pert.grid(row=4, column=2)
        self.Percentage_label = Label(self.lbl2, text=(str(Total / 8)), justify=LEFT, compound=LEFT,
                                      padx=0, font=10, bg=self.col[0], fg=self.col[1])
        if (Total / 8) >= 80 and (Total / 8) <= 100:
            self.Percentage_label["fg"] = "green"
        elif (Total / 8) >= 60 and (Total / 8) < 80:
            self.Percentage_label["fg"] = "blue"
        elif (Total / 8) >= 50 and (Total / 8) < 60:
            self.Percentage_label["fg"] = "orange"
        elif (Total / 8) >= 40 and (Total / 8) < 50:
            self.Percentage_label["fg"] = "Grey"
        else:
            self.Percentage_label["fg"] = "red"
        self.Percentage_label.grid_forget()
        self.Percentage_label.grid(row=5, column=2, rowspan=2)
        self.eml_add_lbl["state"] = NORMAL
        self.eml_add_lbl.delete(0, END)
        self.eml_add_lbl.insert(END, email)
        self.eml_add_lbl["state"] = DISABLED

    def refresh(self):
        root3.destroy()
        Admin_login()

    def updating_values(self):
        global Total
        if int(Mth.get()) > 100 or int(Sci.get()) > 100 or int(Nep.get()) > 100 or int(Eng.get()) > 100 or int(
                Soc.get()) > 100 or int(Com.get()) > 100 or int(EP.get()) > 100 or int(Geo.get()) > 100:
            messagebox.showerror("Invalid Marks", "Please enter marks less than or equal to 100.")
        elif int(Mth.get()) < 0 or int(Sci.get()) < 0 or int(Nep.get()) < 0 or int(Eng.get()) < 0 or int(
                Soc.get()) < 0 or int(Com.get()) < 0 or int(EP.get()) < 0 or int(Geo.get()) < 0:
            messagebox.showerror("Invalid Marks", "Please enter marks greater than or equal to 0.")
        else:
            conn = sqlite3.connect("Login_Data.db")
            c = conn.cursor()
            record = oid_entry.get()
            c.execute("""UPDATE Data SET
                        Maths = :math,
                        Science = :sci,
                        Nepali = :nepa,
                        English = :engl,
                        Social = :soci,
                        Computer = :compu,
                        EPH = :ep,
                        Geography = :geog

                        WHERE oid =:oid """, {
                "math": Mth.get(),
                "sci": Sci.get(),
                "nepa": Nep.get(),
                "engl": Eng.get(),
                "soci": Soc.get(),
                "compu": Com.get(),
                "ep": EP.get(),
                "geog": Geo.get(),

                "oid": record
            })
            conn.commit()
            conn.close()
            messagebox.showinfo("Update", "Records Updated")
            self.send_btn["state"] = NORMAL

    def updating_info(self):
        self.oid_num["state"] = DISABLED
        self.info_win = Toplevel(self.root3, bg="black")
        f_name = Entry(self.info_win, font=('Verdana', 12), bg="black", fg="white", textvariable=self.f_name1)
        f_name.grid(row=1, column=1)
        l_name = Entry(self.info_win, font=('Verdana', 12), bg="black", fg="white", textvariable=self.l_name1)
        l_name.grid(row=2, column=1)
        u_name = Entry(self.info_win, font=('Verdana', 12), bg="black", fg="white", textvariable=self.u_name1)
        u_name.grid(row=3, column=1)
        cls = Entry(self.info_win, font=('Verdana', 12), bg="black", fg="white", textvariable=self.cls1)
        cls.grid(row=4, column=1)
        sec = Entry(self.info_win, font=('Verdana', 12), bg="black", fg="white", textvariable=self.sec1)
        sec.grid(row=5, column=1)

        e_add = Entry(self.info_win, font=('Verdana', 12), bg="black", fg="white", textvariable=self.e_add1)
        e_add.grid(row=6, column=1)
        updt1 = Button(self.info_win, text="Update Info", command=lambda: self.updating_recs(f_name.get(), l_name.get(),
                                                                                             u_name.get(), cls.get(),
                                                                                             sec.get(), e_add.get()),
                       height=2, width=35)
        updt1.grid(row=7, column=0, rowspan=2, columnspan=2, padx=10)
        self.detail_label("First Name: ", 1, 0)
        self.detail_label("Last Name: ", 2, 0)
        self.detail_label("User Name: ", 3, 0)
        self.detail_label("Class: ", 4, 0)
        self.detail_label("Section: ", 5, 0)
        self.detail_label("Email Address: ", 6, 0)

    def detail_label(self, Text, X, Y):
        Label(self.info_win, text=Text, justify=LEFT, compound=LEFT, font=10, bg="black", fg="white").grid(row=X,
                                                                                                           column=Y)

    def updating_recs(self, f_name, l_name, u_name, cls, sec, e_add):
        conn = sqlite3.connect("Login_Data.db")
        c = conn.cursor()
        c.execute("""UPDATE Data SET
                                First_Name = :f_name,
                                Last_Name = :l_name,
                                user_name = :u_name,
                                Class = :cls,
                                Section = :sec,
                                Email_Address = :eml

                                WHERE oid =:oid """, {
            "f_name": f_name,
            "l_name": l_name,
            "u_name": u_name,
            "cls": cls,
            "sec": sec,
            "eml": e_add,
            "oid": self.oid_num.get()
        })
        conn.commit()
        conn.close()
        messagebox.showinfo("Update", "Records Updated")
        self.info_win.destroy()
        self.query()


    def __Gmail_msg(self):
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465)as smtp:
                Email_address = self.__useremail
                Email_pass = self.__userpass
                msg = EmailMessage()
                msg["Subject"] = "Academic Records Updated!!"
                msg["From"] = Email_address
                msg["To"] = email_add
                msg.set_content(self.txt_box.get(1.0, END))
                smtp.login(Email_address, Email_pass)
                smtp.send_message(msg)
                messagebox.showinfo("Sucess", "Message Sent!")

        except Exception as e:
            messagebox.showerror("Error!", str(e))








class user_login(TKWindow):
    def __init__(self):
        super().__init__()
        self.root4 = self.root
        self.root4.geometry("915x453+345+100")
        self.root4.config(bg="black")
        self.root4.resizable("False", "False")
        self.lbl = LabelFrame(self.root4, text="Student Record", highlightcolor="Green",
                              highlightbackground="Grey", highlightthickness=3, bg="Black", fg="blue", width=561,
                              height=700)
        self.lbl.pack(side="right",fill=X)
        self.lbl2 = LabelFrame(self.root4, text="Student Detail", highlightcolor="Green",
                               highlightbackground="Grey", highlightthickness=3, bg="Black", fg="blue", width=661,
                               height=750)
        self.lbl2.pack(side="left",fill=X)
        self.lbl4 = LabelFrame(self.lbl)
        self.lbl4.grid(row=4, column=2, columnspan=3, rowspan=3)
        igm = ImageTk.PhotoImage(Image.open("Images/Student2.png"))
        Label(self.wel, image=igm, bg="black").place(x=0, y=0)
        Label(self.wel, image=igm, bg="black").place(x=760, y=0)
        address_label = Label(self.wel, text="Dillibazar, Kathmandu", font=8, bg="black", fg="blue")
        address_label.place(x=335, y=80)
        rpt_crd = Label(self.root4,text="Report Card", font=20,bg="black",fg="snow")
        rpt_crd.place(x=365,y=115)

        ttk.Button(self.root4,text="Exit",command=self.ext).place(x=350,y=420,width=150, height=35)

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

        self.DataBase_Calls()
        self.root4.mainloop()
    def ext(self):
        self.root4.destroy()
        Login()

    def lables_and_entries(self, Text, X, Y):
        Label(self.lbl, text=Text, justify=LEFT, compound=LEFT, font=10, bg="black", fg="white",width=12).grid(row=X, column=Y)

    def detail_label(self, Text, X, Y):
        Label(self.lbl2, text=Text, justify=LEFT, compound=LEFT, font=12, bg="black", fg="white").grid(row=X, column=Y,sticky=NSEW)

    def DataBase_Calls(self):

        conn = sqlite3.connect("Login_Data.db")
        c = conn.cursor()
        c.execute("""SELECT * FROM Data WHERE OID =""" + str(usr_oid))
        records = c.fetchall()
        for marks in records:
            self.root4.title(marks[0] + " " + marks[2] + "'s Report Card")
            self.Mth.insert(0, marks[5])
            self.Sci.insert(0, marks[6])
            self.Nep.insert(0, marks[7])
            self.Eng.insert(0, marks[8])
            self.Soc.insert(0, marks[9])
            self.Com.insert(0, marks[10])
            self.EP.insert(0, marks[11])
            self.Geo.insert(0, marks[12])
            ###############################Personal Details#####################################
            self.f_name.insert(0, marks[0])
            self.l_name.insert(0, marks[2])
            self.u_name.insert(0, marks[4])
            self.cls.insert(0, marks[15])
            self.sec.insert(0, marks[16])
            if marks[13] == "Mr.":
                self.gender.insert(0, "Male")
            else:
                self.gender.insert(0, "Female")

            self.DOB.insert(0, marks[14])
            self.e_add.insert(0, marks[3])

        Total = (
                int(self.Mth.get()) + int(self.Sci.get()) + int(self.Nep.get()) + int(self.Eng.get()) + int(
            self.Soc.get()) + int(self.Com.get())
                + int(self.EP.get()) + int(self.Geo.get()))

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

        c.close()

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


bc = TKWindow
bc.switch_class(bc,Login)

