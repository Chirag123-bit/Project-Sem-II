
from tkinter import *

from PIL import ImageTk, Image
from tkinter import messagebox, ttk
import Frontend.Register_Page
import Frontend.main as master







class Login(master.TKWindow):
    """This is login window. This window will validate user's credentials and redirect them to their personal account or register new users."""
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
        """This functions will generate all labels for this window."""
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
        """Opens new window depending on user's input(login/register)"""
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
        Frontend.Register_Page.Register()


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
        """Function to reset password. User's email address and username is required for this class"""
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
        """If verification is sucessful, reset button is enabled."""
        pass_entry["state"] = NORMAL
        submt["state"] = NORMAL
        submt["command"] = lambda: Database.replce_pass(Database, pass_entry.get())


login = Login()