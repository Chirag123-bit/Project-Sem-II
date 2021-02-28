from tkinter import *
from PIL import ImageTk, Image
import sqlite3


class TKWindow:
    global abc

    def __init__(self):
        self.root = Tk()
        self.root.title("Login System")
        self.root.geometry("1067x600")  # Defining screen size of our app
        self.Reg_fonts = ('Helvetica', 12)



class Login(TKWindow):

    def __init__(self):
        super().__init__()
        self.root1 = self.root
        image = ImageTk.PhotoImage(Image.open("Images/Root_Backgroung.jpg"))  # adding background image in root
        abc = Label(self.root1, image=image)  # Placing the image file inside the label
        abc.place(x=0, y=0, relwidth=1, relheight=1)  # place enables to write over a label
        self.frame = LabelFrame(self.root1, width=550, height=200, text="Login", relief=RAISED, bd=1,
                                highlightcolor="Green",
                                highlightbackground="Black", highlightthickness=3, cursor="pencil")
        self.frame.place(x=335, y=190)

        self.button_font = ('Verdana', 15)
        self.labels("UserName", 0, 3)
        self.labels("Password", 4, 3)
        self.usr1 = StringVar("")
        self.pass1 = StringVar("")
        self.entry()

        self.lbl = Label(self.root1, text="Student Login System", font=self.button_font)
        self.lbl.place(x=412, y=150)

        self.button("Login", 10, 0, 654, 346, "log")
        self.button("Register", 11, 0, 338, 346, "reg")
        self.root1.mainloop()

    def labels(self, Text, x, y):
        b = Label(self.frame, text=Text, font=self.button_font, bg='grey', anchor=W, width=8)
        b.grid(row=x, column=y, sticky=W)
        b.grid(row=x, column=y, sticky=W)
        c = Label(self.frame, text="")
        c.grid(row=0, column=6)
        d = Label(self.frame, text="")
        d.grid(row=2, column=0)
        e = Label(self.frame, text="")
        e.grid(row=3, column=0)
        f = Label(self.frame, text="")
        f.grid(row=4, column=0)
        g = Label(self.frame, text="")
        g.grid(row=5, column=0)

    def button(self, text_, x, y, ab, cd, comm):
        if comm == "log":
            but = Button(self.root1, text=text_, font=self.button_font, borderwidth=3, command=self.button_pressed_login,
                         highlightbackground="Black", highlightthickness=3,
                         highlightcolor="Green")
            but.grid(row=x, column=y)
            but.place(x=ab, y=cd)
        else:
            but = Button(self.root1, text=text_, font=self.button_font, borderwidth=3,
                         command=self.button_pressed_register)
            but.grid(row=x, column=y)
            but.place(x=ab, y=cd)

    def entry(self):
        usr = Entry(self.frame, font=self.button_font, text=self.usr1, borderwidth=4)
        usr.grid(row=0, column=7)
        pas = Entry(self.frame, font=self.button_font, text=self.pass1, show="*", borderwidth=4)
        pas.grid(row=4, column=7)

    def button_pressed_register(self):
        self.root1.destroy()
        Register()

    def button_pressed_login(self):
        return


class Register(TKWindow):
    def __init__(self):
        global img
        super().__init__()
        self.root2 = self.root
        self.root2.geometry("960x600")
        back_img = ImageTk.PhotoImage(Image.open("Images/Reg_Back.jpg"))
        img = Label(self.root, image=back_img)
        img.place(x=0, y=0, relwidth=1, relheight=1)
        F_Name = StringVar("")
        L_Name = StringVar("")
        E_Add = StringVar("")
        Passwd = StringVar("")
        Phone = StringVar("")
        Passwd2 = StringVar("")
        self.Reg_scrn("First Name", 100, 130, 220, 130, F_Name)
        self.Reg_scrn("Last Name", 495, 130, 616, 130, L_Name)

        self.Reg_scrn("Email Address", 100, 230, 220, 230, E_Add)
        self.Reg_scrn("Password", 495, 230, 616, 230, Passwd)

        self.Reg_scrn("Phone No:", 100, 330, 220, 330, Phone)
        self.Reg_scrn("Password", 495, 330, 616, 330, Passwd2)
        self.Reg_fonts = ('Helvetica', 12)
        self.root2.mainloop()
    def Reg_scrn(self, Text, X, Y, a, b, var):
        global suffix
        labls = Label(self.root2, text=Text, font=self.Reg_fonts, anchor=NW, width=12, borderwidth=2, relief="ridge",
                      justify="center")
        labls.place(x=X, y=Y)
        if Text == "Password":
            entry = Entry(self.root2, font=self.Reg_fonts, text=Text, textvariable=var, show="*", borderwidth=2,
                          justify="center")
            entry.place(x=a, y=b)

        else:
            entry = Entry(self.root2, font=self.Reg_fonts, text=Text, textvariable=var, borderwidth=2, justify="center")
            entry.place(x=a, y=b)

        choices = ["Mr,", "Mrs.", "Miss"]
        suffix = StringVar(self.root2)
        suffix.set("Mr.")

        optbox = OptionMenu(self.root2, suffix, *choices)
        optbox.place(x=410, y=80)
        buttnreg = Button(self.root2, font=self.Reg_fonts, text="Register", width=12, borderwidth=2)
        buttnreg.place(x=505, y=450)
        buttncanc = Button(self.root2, font=self.Reg_fonts, text="Cancle", width=12, borderwidth=2,command=self.root2.destroy)
        buttncanc.place(x=300, y=450)




class Database(Login,Register):
    def __init__(self):
        super().__init__()
        #Establishing the connection To database
        conn = sqlite3.connect("Data.db")
        #Creating cursor to add or retrive data from DB
        c = conn.cursor()

        #Creating Tables for DB
        c.execute("CREATE TABLE"
                  "")





        #Commiting Changes
        conn.commit()
        #Closing Connection
        conn.close()


# ab = TKWindow()
bc = Login()
# ab.__init__()
