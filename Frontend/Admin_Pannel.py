import sqlite3
from tkinter import *

from PIL import ImageTk, Image
from tkinter import messagebox, ttk
import smtplib
from email.message import EmailMessage
import Frontend.Login_Page
import Backend.DBConnect
class Admin_login():

    """ Administrative page/window of this program.
        Can update, remove student's data. This window
        has administrative access over all other accounts.
        Admin can also send emails through this window."""
    def __init__(self,root):
        super().__init__()
        global oid_num, Mth, Sci, Nep, Eng, Soc, Com, EP, Geo, root3, email_add
        self.root3 = root
        self.root3.geometry("1160x750+200+0")
        self.root3.resizable(False, False)
        self.root3.config(bg="black")
        self.root3.title("Admin Pannel")
        self.Reg_fonts = ('Helvetica', 12)
        self.sft_img = ImageTk.PhotoImage(Image.open("Images/softwarica.png"))  # Placing image inside label
        self.wel = LabelFrame(self.root3, bg="black", highlightbackground="black", highlightcolor="black")
        self.wel.pack(side="top", fill="x")  # Creating frames which will hold college's logo
        self.logo_img = Label(self.wel, image=self.sft_img, bg="black")
        self.logo_img.pack(fill="both", expand=3)
        logo_img = ImageTk.PhotoImage(Image.open("Images/Student2.png"))  # Importing logo
        self.std_log = Label(self.wel, image=logo_img, bg="black")
        self.std_log.place(x=0, y=0)  # Placing logo on left
        self.std_log1 = Label(self.wel, image=logo_img, bg="black")
        self.root3.iconbitmap('Images/logo.ico')


        self.__useremail = "collegeproject961@gmail.com"
        self.__userpass = "Abcde@12345"


        self.del_btn = ttk.Button(self.root3, text="Delete Record", state=DISABLED)
        self.del_btn.place(x=955, y=585, width=200, height=50)

        self.db = Backend.DBConnect.DBConnect()




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
        self.address_label = Label(self.wel, text="Dillibazar, Kathmandu", font=10, bg="black", fg="white")
        self.address_label.place(x=469, y=80)
        self.oooid = Label(self.root3, text="Student's OID::", font=15, bg="black", fg="white")
        self.oooid.place(x=765, y=560)
        self.search = Entry(self.root3, font=self.Reg_fonts)
        self.search.place(x=610, y=460, height=30)
        ttk.Button(self.root3, text="Search", command=self.search_lst).place(x=800, y=460, width=200, height=30)
        ttk.Button(self.root3, text="Reset", command=self.query).place(x=1010, y=460, width=150, height=30)
        self.eee = Label(self.root3, text="F/L Name", bg="black", fg="white", font=10)
        self.eee.place(x=515, y=462)

        self.oid_num = ttk.Entry(self.root3, font=self.Reg_fonts)
        self.oid_num.insert(0, "Double tap on names above")
        self.oid_num["state"] = DISABLED
        self.oid_num.place(x=920, y=560)
        self.std_log1.place(x=1050, y=0)

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

        self.root3.mainloop()

    def ext(self):
        self.root3.destroy()
        tk=Tk()
        Frontend.Login_Page.Login(tk)


    def dark_mode(self):
        """Function for enabling dark mode"""
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
        """Function for reverting back to regular mode."""
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
        try: #If user selects this mode before percentage label is created, this will generate an error. To prevent this error handling is used.
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
        """Function to show student's info in treeview for better readability and manageability."""
        global Name_list, oid_list
        self.search.delete(0, END)
        self.frm = LabelFrame(self.root3, text="User's Details", highlightcolor="Green",
                              highlightbackground="Blue", highlightthickness=3, fg="green", bg="#ffffaa", width=561,
                              height=287)
        self.frm.place(x=598, y=170)
        self.frm.pack_propagate(False)

        self.treeview = ttk.Treeview(self.frm, columns=(1, 2, 3, 4, 5, 6, 7,8), show="headings",
                                     style='Calendar.Treeview', selectmode="extended")
        self.treeview.bind('<Button-1>', self.getrow)
        my_scrl = Scrollbar(self.frm, orient=HORIZONTAL, command=self.treeview.xview)
        my_scrl2 = Scrollbar(self.frm, orient=VERTICAL, command=self.treeview.yview)
        self.treeview.config(xscrollcommand=my_scrl.set)
        self.treeview.config(yscrollcommand=my_scrl2.set)
        my_scrl.pack(side=BOTTOM, fill=X)
        my_scrl2.pack(side=RIGHT, fill=Y)
        self.treeview.pack(fill=BOTH, expand=YES)

        ###########################################Configuring Scrollbar#############################

        self.treeview.heading(1, text="First Name", anchor="sw")
        self.treeview.column(1, minwidth=0, width=80, stretch=False)
        self.treeview.heading(2, text="Last Name", anchor="sw")
        self.treeview.column(2, minwidth=0, width=80, stretch=False)
        self.treeview.heading(3, text="Email Address", anchor="sw")
        self.treeview.column(3, minwidth=0, width=170, stretch=False)
        self.treeview.heading(4, text="Password", anchor="sw")
        self.treeview.column(4, minwidth=0, width=100, stretch=False)
        self.treeview.heading(5, text="User Name", anchor="sw")
        self.treeview.column(5, minwidth=0, width=100, stretch=False)
        self.treeview.heading(6, text="DOB", anchor="sw")
        self.treeview.column(6, minwidth=0, width=100, stretch=False)
        self.treeview.heading(7, text="Class", anchor="sw")
        self.treeview.column(7, minwidth=0, width=50)
        self.treeview.heading(8, text="Section", anchor="sw")
        self.treeview.column(8, minwidth=0, width=50)



    def lables_and_entries(self, Text, X, Y, A, B, vari, col, col1):
        """Generates all labels and entries for this window"""
        self.usr_lbl1 = Label(self.lbl, text=Text, justify=LEFT, compound=LEFT, font=10, bg=col, fg=col1)
        self.usr_lbl1.grid(row=X, column=Y)
        self.usr_lbl = Label(self.lbl, text="Select a Student:", justify=LEFT, compound=LEFT, padx=10, font=10,
                             bg="black",
                             fg="white")
        self.usr_lbl.grid(row=0, column=0)
        self.usr_ent = Entry(self.lbl, textvariable=vari, font=('Verdana', 12), bg=col, fg=col1)
        self.usr_ent.grid(row=A, column=B)

    def getrow(self, event):
        """Get student's OID for performing database operations"""
        try:
            item = self.treeview.item(self.treeview.focus())
            self.f_name1.set(item["values"][0])
            self.l_name1.set(item["values"][1])
            self.u_name1.set(item["values"][4])
            self.cls1.set(item["values"][-3])
            self.sec1.set(item["values"][-2])
            self.e_add1.set(item["values"][2])
            self.oid_num["state"] = NORMAL
            self.oid_num.delete(0, END)
            self.oid_num.insert(0, item["values"][0])
            self.oid_num["state"] = DISABLED
            self.updt1["state"] = NORMAL
            self.del_btn["state"] = NORMAL
        except IndexError:
            print("Please Select a student from this list.")






    def search_lst(self):
        """Creates search window for filtering users"""
        value = [self.search.get(),self.search.get(),self.search.get(),self.search.get()]
        query = "select * from user_info where FName like %s or LName like %s or Class like %s or Section like %s"
        rows = self.db.select(query,value)

        if rows:
            self.treeview.delete(*self.treeview.get_children())
            for ii in rows:
                self.treeview.insert("", "end", values=ii)
        else:
            messagebox.showinfo("User Not Found",
                                "No student with First/Last name " + value[0] + " or Class/Section " + value[0] +
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
        """Function to show marks of selected users in respective entry boxes."""
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
        #To refresh treeview frame after updating entries
        root3.destroy()
        Admin_login()

    def updating_values(self, record):
        """To update student's marks"""
        global Total
        if int(Mth.get()) > 100 or int(Sci.get()) > 100 or int(Nep.get()) > 100 or int(Eng.get()) > 100 or int(
                Soc.get()) > 100 or int(Com.get()) > 100 or int(EP.get()) > 100 or int(Geo.get()) > 100:
            messagebox.showerror("Invalid Marks", "Please enter marks less than or equal to 100.")
        elif int(Mth.get()) < 0 or int(Sci.get()) < 0 or int(Nep.get()) < 0 or int(Eng.get()) < 0 or int(
                Soc.get()) < 0 or int(Com.get()) < 0 or int(EP.get()) < 0 or int(Geo.get()) < 0:
            messagebox.showerror("Invalid Marks", "Please enter marks greater than or equal to 0.")
        else:
            query = "update grades set (Maths = %s, Science = %s,\
                     Nepali= %s, English = %s, Social = %s,Computer = %s, EPH = %s, Geography = %s) where UserName = %s"
            values = [Mth.get(),Sci.get(),Nep.get(),Eng.get(),Soc.get(),Com.get(),EP.get(),Geo.get(),record]

            self.db.update(query,values)

            messagebox.showinfo("Update", "Records Updated")
            self.send_btn["state"] = NORMAL

    def updating_info(self):
        """Cretes new window where user's personal info such as f/l name is displayed which can be changed by admin."""
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
        """Updates personal info such as f/l name."""
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
        """Sends email to the selected users."""
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

tk = Tk()
Admin_login(tk)