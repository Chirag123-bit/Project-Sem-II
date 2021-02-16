
from tkinter import *

from PIL import ImageTk, Image
from tkinter import messagebox, ttk
from tkcalendar import *
import re
import Frontend.Login_Page as master
import model.User
import Backend.DBConnect



class Register():
    """Here, Phone Number is changed into User Name
    New users are registered here."""


    def __init__(self,root):
        global img, F_Name, L_Name, E_Add, Passwd, Username, Passwd2, DoB
        self.root2 = root
        self.root2.geometry("960x600+200+0")
        self.root2.title("Softwarica College Registration Form")
        self.root2.resizable("False", "False")
        self.Reg_fonts = ('Helvetica', 12)
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
        self.db = Backend.DBConnect.DBConnect()

        address_label = Label(self.wel, text="Dillibazar, Kathmandu", font=13, bg="SteelBlue1", fg="blue2")
        address_label.place(x=395, y=80)
        F_Name = StringVar("")
        L_Name = StringVar("")
        E_Add = StringVar("")
        Passwd = StringVar("")
        Username = StringVar("")
        Passwd2 = StringVar("")
        DoB = StringVar("")
        Label(self.root2, text="Softwarica College Registration Form", font=45, width=30,
              ).place(x=305,
                              y=114)
        self.Reg_scrn("First Name", 100, 180, 220, 180, F_Name)
        self.Reg_scrn("Last Name", 495, 180, 616, 180, L_Name)

        self.Reg_scrn("Email Address", 100, 280, 220, 280, E_Add)
        self.Reg_scrn("Password", 495, 280, 616, 280, Passwd)

        self.Reg_scrn("User Name No:", 100, 380, 220, 380, Username)
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
                               command=self.btn_pressed_cancle)
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
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+@gmail.com$'  # This is regex(regular expression) expression for checking if email address is correct
        # Here ^ and $ suggests beginning and end of lime

        ver = (re.search(regex, E_Add.get()))


        if Passwd.get() == Passwd2.get() and (
                len(F_Name.get()) != 0 and len(L_Name.get()) != 0 and len(Passwd.get()) != 0 and len(
            E_Add.get()) != 0 and len(Username.get()) != 0 and len(Passwd2.get()) != 0) and ver != None:

            u = model.User.User(F_Name.get(),L_Name.get(),E_Add.get(),Passwd.get(),Username.get(),
                                self.dob_entry.get(),grade.get(),section.get(),suffix.get())

            query = "INSERT INTO user_info(FName,LName,EAddress,Password,UserName,DOB,Class,Section,Suffix)  \
                                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            values = (u.get_fname(),u.get_lname(),u.get_eadd(),u.get_passwd(),u.get_uname(),
                      u.get_dob(),u.get_cls(),u.get_sec(),u.get_suff())
            self.db.insert(query, values)
            query = "INSERT INTO grades(UserName, Maths,Science,Nepali,English,Social,Computer,EPH,Geography)  \
                                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            values = (u.get_uname(),0,0,0,0,0,0,0,0)
            self.db.insert(query, values)

            messagebox.showinfo("Sucess", "User Added")
            self.btn_pressed_cancle()


        elif Passwd.get() != Passwd2.get():
            messagebox.showerror("Invalid Password", "Please Re-check your Password!!")
            entry1.delete(0, END)

        elif ver == None:
            messagebox.showerror("Invalid Email", "Please enter a valid Email Address!")

        else:
            messagebox.showerror("Required Field Missing", "Please Fill all the given fields!!")
    def btn_pressed_cancle(self):
        self.root2.destroy()
        tk = Tk()
        master.Login(tk)
