
from tkinter import *

from PIL import ImageTk, Image
from tkinter import messagebox, ttk
import Frontend.Register_Page
import Frontend.Admin_Pannel
import Frontend.User_Dashboard
import model.User
import Backend.DBConnect





class Login():
    """This is login window. This window will validate user's credentials and
        redirect them to their personal account or register new users."""

    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")  # Setting title of first window
        self.root.geometry("1067x600+230+40")  # Defining screen size of our app
        self.root.iconbitmap('Images/logo.ico')  # importing logo from "Images" folder
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
        self.db = Backend.DBConnect.DBConnect()
        
        
        self.ttk = ttk
        self.root.resizable(False, False)
        ######################################################Images#################################################
        image = ImageTk.PhotoImage(Image.open("Images/Root_Backgroung.jpg"))  # adding background image in root
        abc = Label(self.root, image=image)  # Placing the image file inside the label
        abc.place(x=0, y=0, relwidth=1, relheight=1)  # place enables to write over a label
        self.frame = LabelFrame(self.root, width=550, height=200, text="Login", relief=RAISED, bd=1,
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
        std_label = Label(self.root, image=self.student_icon, bg="blue", fg="gray10")
        std_label.place(x=482, y=59)
        self.Reg = ImageTk.PhotoImage(Image.open("Images/Register.png"))
        usr_reg = Label(self.root, image=self.Reg)
        usr_reg.place(x=332, y=346)
        self.logn = ImageTk.PhotoImage(Image.open("Images/Login.png"))
        logn_img = Label(self.root, image=self.logn)
        logn_img.place(x=620, y=346)

        ######################################################Buttons And Labels##################################################
        self.button_font = ('Verdana', 15)
        self.labels("UserName", 0, 3)
        self.labels("Password", 4, 3)
        self.usr1 = StringVar("")
        self.pass1 = StringVar("")
        self.entry()

        self.lbl = ttk.Label(self.root, text="Student Login System", font=self.button_font, background="white",
                             foreground="blue")
        self.lbl.place(x=420, y=25)

        self.button("Login", 10, 0, 654, 346, "log")
        self.button("Register", 11, 0, 366, 346, "reg")
        self.butn = Button(self.frame, text="Forgot Password?", fg="blue", anchor="e", command=self.show_pass).grid(
            row=5, column=7, sticky="E")
        abz = ImageTk.PhotoImage(Image.open("Images/Forgot_pass.png"))
        for_pas_img = Label(self.frame, image=abz)
        for_pas_img.place(x=282, y=105)
        ######################################################root Mainloop##################################################
        self.root.mainloop()

    def labels(self, Text, x, y):
        """
        This functions will generate all labels for this window.
        Text = Text to display on widget
        x = Row of widget
        y = column of widget
        :param Text: string
        :param x: int
        :param y: int
        :return: none
        """
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

    def button(self, text_,x,y, ab, cd, comm):
        """
        :param text_: str
        :param x: int
        :param y: int
        :param ab: int
        :param cd: int
        :param comm: str
        :return: None
        """
        """Opens new window depending on user's input
        Here,
        text_ = text to display on widget
        ab = x co-rdinate of widget
        cd = y co-ordinate of widget
        com = button pressed by user(login/register)
        """
        if comm == "log":
            but = ttk.Button(self.root, text=text_,
                             command=self.button_pressed_login, padding=6
                             )
            but.place(x=ab, y=cd)
        else:
            but = ttk.Button(self.root, text=text_, padding=6,
                             command=self.button_pressed_register)
            but.place(x=ab, y=cd)

    def entry(self):
        """Creates Username and Password Entry box for login page
        :return: None
        """
        global pas
        usr = ttk.Entry(self.frame, font=self.button_font, text=self.usr1)
        usr.grid(row=0, column=7)
        pas = ttk.Entry(self.frame, font=self.button_font, text=self.pass1, show="*")
        pas.grid(row=4, column=7)

    def button_pressed_register(self):
        """

        :return: None
        """
        self.root.destroy()
        tk = Tk()
        Frontend.Register_Page.Register(tk)


    def button_pressed_login(self):
        """This function is called when login is pressed and switches window based on credentials entered"""
        global usr_oid, rs_pas, rs_eml, rs_usrnm

        if self.usr1.get() == "root" and self.pass1.get() == "root":
            self.root.destroy()
            tk=Tk()
            Frontend.Admin_Pannel.Admin_login(tk)

        elif self.usr1.get() == "root" and self.pass1.get() != "root":
            messagebox.showerror("Error", "Please enter a valid password!")
            pas.delete(0, END)

        else:
            u = model.User.User(uname=self.usr1.get(), passwd=self.pass1.get())
            query = ("SELECT * FROM user_info WHERE UserName = %s AND Password =%s ")
            values = [u.get_uname(),u.get_passwd()]
            records = self.db.select(query,values)


            if records:
                for i in records:
                    usr_oid = i[4]
                    rs_pas = i[3]
                    rs_eml = i[2]
                    rs_usrnm = i[4]
                    messagebox.showinfo("Welcome", "Welcome  " + str(i[-1]) + str(i[0]) + " " + str(i[1]))
                    self.root.destroy()
                    tk = Tk()
                    Frontend.User_Dashboard.user_login(tk,usr_oid)

            else:
                if len(self.usr1.get()) != 0 and len(self.pass1.get()) != 0:
                    msg = messagebox.askokcancel("Invalid Credentials", "Please Re-check your login details")

                    if msg == True:
                        self.pass1.set("")
                    else:
                        messagebox.showwarning("Message", "Exiting Program")
                        self.root.destroy()

                else:
                    messagebox.showerror("Required Fields Missing", "Please Enter your Credentials")

    def show_pass(self):
        """Function to reset password. User's email address and username is required for this class"""
        global em_entr, un_entr, submt, pass_entry, record123
        self.rs_win = Toplevel(self.root)

        em_lbl = Label(self.rs_win, text="Enter Email Address::: ").grid(row=0, column=0)
        un_lbl = Label(self.rs_win, text="Enter User Name::: ").grid(row=1, column=0)
        self.em_entr = Entry(self.rs_win, font=('Verdana', 12))
        self.em_entr.grid(row=0, column=1)
        self.un_entr = Entry(self.rs_win, font=('Verdana', 12))
        self.un_entr.grid(row=1, column=1)
        sub_btn = Button(self.rs_win, text="Submit",
                         command=lambda: self.check())
        sub_btn.grid(row=2, column=1)
        lebl = Label(self.rs_win, text="Enter New Password::: ")
        lebl.grid(row=3, column=0)
        self.pass_entry = Entry(self.rs_win, state=DISABLED, font=('Verdana', 12))
        self.pass_entry.grid(row=3, column=1)
        submt = Button(self.rs_win, text="Update Password", state=DISABLED,
                       command=self.update_pass)
        submt.grid(row=4, column=0)



    def check(self):
        """If verification is sucessful, reset button is enabled."""
        query = "select * from user_info where EAddress = %s and UserName = %s"
        u = model.User.User(eadd=self.em_entr.get(), uname=self.un_entr.get())
        values = [u.get_eadd(), u.get_uname()]
        rec = self.db.select(query,values)
        if rec:
            self.pass_entry["state"] = NORMAL
            submt["state"] = NORMAL

        else:
            messagebox.showerror("Error","Email Address or Password is wrong!")

    def update_pass(self):
        """This function resets user's password"""
        u = model.User.User(passwd=self.pass_entry.get(), uname=str(self.un_entr.get()))
        que = "update user_info set Password = %s where UserName = %s"
        val = [u.get_passwd(), str(u.get_uname())]
        submt["command"] = self.db.update(que, val)
        messagebox.showinfo("Success", "Password updated successfully")








