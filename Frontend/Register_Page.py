import sqlite3
from tkinter import *

from PIL import ImageTk, Image
from tkinter import messagebox, ttk
import smtplib
from email.message import EmailMessage
from tkcalendar import *
import re
import Frontend.main as master

class Register(master.TKWindow):
    """Here, Phone Number is changed into User Name
    New users are registered here."""


    def __init__(self):
        global img, F_Name, L_Name, E_Add, Passwd, Phone, Passwd2, DoB
        super().__init__()
        self.wel.pack_forget()

        self.root2 = self.root
        self.root2.geometry("960x600+200+0")
        self.root2.title("Softwarica College Registration Form")
        self.root2.resizable("False", "False")
        back_img = ImageTk.PhotoImage(Image.open("Images/Reg_Back.jpg"))
        img = Label(self.root2, image=back_img)
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
        """Creating all the entry boxes and labels for this window"""
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
        """Placing calender in the registration scree for easy selection of dates"""
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
        """Using RE(Regular expression) to validate user's email address and registering user into database if all conditions are satisfied."""
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
