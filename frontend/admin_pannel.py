from tkinter import *

from PIL import ImageTk, Image
from tkinter import messagebox, ttk
import smtplib
from email.message import EmailMessage
import frontend.login_page
import backend.dbconnect
import model.grades
import model.user
import backend.searching_sorting
import os



class Admin_login():
    """ Administrative page/window of this program.
        Can update, remove student's data. This window
        has administrative access over all other accounts.
        Admin can also send emails through this window."""

    def __init__(self, root):
        global usname, Mth, Sci, Nep, Eng, Soc, Com, EP, Geo, root3, email_add
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
        self.user = StringVar()

        self.__useremail = "collegeproject961@gmail.com"
        self.__userpass = "Abcde@12345"

        self.del_btn = ttk.Button(self.root3, text="Delete Record", state=DISABLED, command=self.delete_user)
        self.del_btn.place(x=955, y=585, width=200, height=50)

        self.db = backend.dbconnect.DBConnect()

        ttk.Button(self.root3, text="Exit", command=self.ext).place(x=960, y=700, width=200, height=50)

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
        self.oousname = Label(self.root3, text="Student's UserName", font=12, bg="black", fg="white")
        self.oousname.place(x=736, y=556)
        self.search = Entry(self.root3, font=self.Reg_fonts, state=DISABLED)
        self.search.place(x=610, y=460, height=30)
        ttk.Button(self.root3, text="Search", command=self.search_user).place(x=800, y=460, width=200, height=30)
        ttk.Button(self.root3, text="Reset", command=self.query).place(x=1010, y=460, width=150, height=30)

        self.selected_search_method = StringVar()
        self.selected_search_method.set("Search By")
        methods = ["First Name", "Last Name"]
        self.opt2 = OptionMenu(self.root3, self.selected_search_method, *methods)
        self.opt2.config(width=16, font=('Verdana', 10))
        self.selected_search_method.trace("w", self.get_search_item)
        self.opt2.place(x=430, y=460)

        self.usname = ttk.Entry(self.root3, font=self.Reg_fonts)
        self.usname.insert(0, "Double tap on names above")
        self.usname["state"] = DISABLED
        self.usname.place(x=920, y=560)
        self.std_log1.place(x=1050, y=0)

        self.lbl = LabelFrame(self.root3, text="Student Record", highlightcolor="Green",
                              highlightbackground="Grey", highlightthickness=3, bg="Black", fg="gold", height=300,
                              width=310)
        self.lbl.place(x=0, y=169)
        self.lbl.pack_propagate(False)

        Mth, Sci, Nep, Eng, Soc, Com, EP, Geo = StringVar(""), StringVar(""), StringVar(""), StringVar(""), StringVar(
            ""), StringVar(""), StringVar(""), StringVar("")
        self.lbl2 = LabelFrame(self.lbl, highlightcolor="Red",
                               highlightbackground="grey", highlightthickness=3, bg="black", fg="green")

        self.lbl2.grid(row=2, column=2, rowspan=6, columnspan=6,padx=(20, 20))

        self.lables_and_entries("Math", 1, 0, 1, 1, Mth, "black", "white")
        self.lables_and_entries("Science", 2, 0, 2, 1, Sci, "black", "white")
        self.lables_and_entries("Nepali", 3, 0, 3, 1, Nep, "black", "white")
        self.lables_and_entries("English", 4, 0, 4, 1, Eng, "black", "white")
        self.lables_and_entries("Social", 5, 0, 5, 1, Soc, "black", "white")
        self.lables_and_entries("Computer", 6, 0, 6, 1, Com, "black", "white")
        self.lables_and_entries("EPH", 7, 0, 7, 1, EP, "black", "white")
        self.lables_and_entries("Geography", 8, 0, 8, 1, Geo, "black", "white")

        ttk.Button(self.root3, text="Update Marks",
                   command=lambda: self.updating_values()).place(x=160, y=462, width=200,
                                                                                              height=40)
        self.updt1 = ttk.Button(self.root3, text="Update Info", command=self.updating_info, state=DISABLED)
        self.updt1.place(x=750, y=585, width=200, height=50)
        self.send_btn = ttk.Button(self.root3, text="Send E-mail", command=self.__Gmail_msg, state=DISABLED)
        self.send_btn.place(x=340, y=585, width=200, height=50)
        self.msg_frm = LabelFrame(self.root3, bg="white")
        self.msg_frm.place(x=0, y=510)
        to_lbl = Label(self.msg_frm, text="To: ", font=('Verdana', 12), anchor=E).grid(row=0, column=0, sticky=W)
        self.eml_add_lbl = Entry(self.msg_frm, font=('Verdana', 12), state=DISABLED, justify=LEFT, width=25)
        self.eml_add_lbl.grid(row=0, column=1, sticky=SW)
        self.txt_box = Text(self.msg_frm, height=13, width=40, bg="black", fg="orange")
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
        self.passwd = StringVar()
        self.txt_box["state"] = DISABLED


        query = "select UserName from user_info"
        users = self.db.select(query)

        list_of_users = []
        for i in users:
            list_of_users.append(i[0])
        self.selected_user = StringVar()
        self.selected_user.set("Select a User")
        self.opt = OptionMenu(self.lbl, self.selected_user, *list_of_users)
        self.opt.config(width=16, font=('Verdana', 12))
        self.opt.grid(row=0, column=1)
        self.selected_user.trace("w", self.opt_call)

        self.sort_method = StringVar()
        self.sort_method.set("Select a method")
        method_list = ["First Name", "Last Name", "Class"]
        self.sort_opt = OptionMenu(self.root3, self.sort_method, *method_list)
        self.sort_opt.config(width=16, font=('Verdana', 12))
        self.sort_opt.place(x=990, y=135)
        self.sort_method.trace("w", self.sort_option)
        self.sort_lbl = Label(self.root3, text="Sort By:", justify=LEFT, compound=LEFT, padx=9, font=9,
                             bg="black",
                             fg="white")
        self.sort_lbl.place(x=870,y=135)
        self.query()


        self.root3.mainloop()

    def ext(self):
        """Function for exiting Admin Panel and returning to login page"""
        self.root3.destroy()
        tk = Tk()
        frontend.login_page.Login(tk)

    def get_search_item(self,*args):
        """A mediator function which enables search entry box when search mode is chosen"""
        self.search.configure(state = NORMAL)



    def dark_mode(self):
        """Function for enabling dark mode
        :return: None
        """
        self.col = ("black", "white")
        self.root3.config(bg="black")
        self.lbl.config(bg="black", fg="white")
        self.Dark_modelbl.config(bg="black", fg="white")
        self.dark_frm.config(bg="black", fg="white")
        self.wel.destroy()
        self.wel = LabelFrame(self.root3, bg="black", highlightbackground="black", highlightcolor="black")
        self.wel.pack(side="top", fill="x")
        self.logo_img = Label(self.wel, image=self.sft_img, bg="black")
        self.logo_img.pack(fill="both", expand=3)
        self.logo_img = ImageTk.PhotoImage(Image.open("Images/Student2.png"))
        self.std_log = Label(self.wel, image=self.logo_img, bg="black")
        self.std_log.place(x=0, y=0)
        self.std_log1 = Label(self.wel, image=self.logo_img, bg="black")
        self.std_log1.place(x=1050, y=0)
        self.address_label = Label(self.wel, text="Dillibazar, Kathmandu", font=10, bg="black", fg="white")
        self.address_label.place(x=469, y=80)
        self.oousname.config(bg="black",fg="white")

        self.usr_ent.config(bg="black", fg="white")
        self.usr_lbl1.config(bg="black", fg="white")
        self.welcome.config(bg="black", fg="white")
        self.search.config(bg="white", fg="black", font=15)
        self.sort_lbl.config(bg="black", fg="white")
        self.oousname.config(bg="black", fg="white")
        self.txt_box.config(bg="black", fg="orange")

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
        self.sort_lbl.config(bg="black",fg="white")
        try:
            self.lbl2.grid_forget()
            self.lbl2.grid(row=2, column=2, rowspan=6, columnspan=6,padx=(20, 20))
            self.Percentage_label.grid_forget()
            self.Percentage_label.grid(row=5, column=2, rowspan=2)
            self.total_label.config(bg="black", fg="white")
            self.pert.config(bg="black", fg="white")
            self.Percentage_label.config(bg="black")
        except:
            pass

    def reg_mode(self):
        """Function for reverting back to regular mode.
        :return: None
        """
        self.col = ("snow", "black")
        self.root3.config(bg="seashell")
        self.lbl.config(bg="azure2", fg="black")
        self.dark_frm.config(bg="snow", fg="black")
        self.Dark_modelbl.config(bg="snow", fg="black")
        self.usr_ent.config(bg="azure2", fg="black")
        self.usr_lbl1.config(bg="azure2", fg="black")
        self.welcome.config(bg="seashell", fg="black")
        self.search.config(bg="light yellow", fg="orange2", font=15)
        self.sort_lbl.config(bg="white", fg="black")
        self.oousname.config(bg="white", fg="black")
        self.wel.destroy()
        self.wel = LabelFrame(self.root3, bg="snow", highlightbackground="snow", highlightcolor="snow")
        self.wel.pack(side="top", fill="x")
        self.logo_img = Label(self.wel, image=self.sft_img, bg="snow")
        self.logo_img.pack(fill="both", expand=3)
        self.logo_img = ImageTk.PhotoImage(Image.open("Images/Student2.png"))
        std_log22 = Label(self.wel, image=self.logo_img, bg="snow", fg="blue")
        std_log22.place(x=0, y=0)
        std_log111 = Label(self.wel, image=self.logo_img, bg="snow", fg="blue")
        std_log111.place(x=1050, y=0)
        self.address_label = Label(self.wel, text="Dillibazar, Kathmandu", font=10, bg="snow", fg="blue")
        self.address_label.place(x=469, y=78)
        self.sort_lbl.config(bg="seashell",fg="black")
        self.oousname.config(bg="seashell",fg="black")

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
        try:  # If user selects this mode before percentage label is created, this will generate an error. To prevent this error handling is used.
            self.lbl2.grid_forget()
            self.lbl2.grid(row=2, column=2, rowspan=6, columnspan=6,padx=(20, 20))
            self.Percentage_label.grid_forget()
            self.Percentage_label.grid(row=5, column=2, rowspan=2)
            self.total_label.config(bg="snow", fg="black")
            self.Percentage_label.config(bg="snow")
            self.pert.config(bg="snow", fg="black")
        except:
            pass
        self.txt_box.config(bg="old lace", fg="gray0")

    def query(self):
        """Function to show student's info in treeview for better readability and manageability.
        :return: None
        """
        global Name_list, usname_list
        self.sort_method.set("Select a method")
        self.selected_search_method.set("Search By")
        self.search.delete(0, END)
        self.frm = LabelFrame(self.root3, text="User's Details", highlightcolor="Green",
                              highlightbackground="Blue", highlightthickness=3, fg="green", bg="#ffffaa", width=561,
                              height=287)
        self.frm.place(x=598, y=170)
        self.frm.pack_propagate(False)

        self.treeview = ttk.Treeview(self.frm, columns=(1, 2, 3,4,5,6,7,8), show="headings",
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
        self.treeview.heading(4, text="User Name", anchor="sw")
        self.treeview.column(4, minwidth=0, width=100, stretch=False)
        self.treeview.heading(5, text="DOB", anchor="sw")
        self.treeview.column(5, minwidth=0, width=100, stretch=False)
        self.treeview.heading(6, text="Class", anchor="sw")
        self.treeview.column(6, minwidth=0, width=50)
        self.treeview.heading(7, text="Section", anchor="sw")
        self.treeview.column(7, minwidth=0, width=50)
        self.treeview.heading(8, text="Suffix", anchor="sw")
        self.treeview.column(8, minwidth=0, width=50)

        query = "select * from user_info"
        records = self.db.select(query)
        for record in records:
            self.treeview.insert("", "end",
                                 values=(
                                     record[0], record[1], record[2], record[3], record[4], record[5],
                                     record[6], record[7]

                                 ))
        self.search.configure(state = DISABLED)



    def lables_and_entries(self, Text, X, Y, A, B, vari, col, col1):

        """Generates all labels and entries for this window
        Here,
        Text = Text to display on widget
        X = Row of label widget
        Y= Column of label widget
        A = Row of Entry Widget
        B= Column of Entry Widget
        vari = Variable to store values returned by entry widgets
        col = Background color of widget
        col1 = Foreground color of widget

        :param Text: str
        :param X: int
        :param Y: int
        :param A: int
        :param B: int
        :param vari: str
        :param col: str
        :param col1: str
        :return:None

        """
        self.usr_lbl1 = Label(self.lbl, text=Text, justify=LEFT, compound=LEFT, font=10, bg=col, fg=col1)
        self.usr_lbl1.grid(row=X, column=Y)
        self.usr_lbl = Label(self.lbl, text="Select a Student:", justify=LEFT, compound=LEFT, padx=10, font=10,
                             bg="black",
                             fg="white")
        self.usr_lbl.grid(row=0, column=0)
        self.usr_ent = Entry(self.lbl, textvariable=vari, font=('Verdana', 12), bg=col, fg=col1)
        self.usr_ent.grid(row=A, column=B)


    def getrow(self, event):

        """
        This is the handler function for treeview.
        Get student's Details for performing Update/Delete operations
        :param event: str
        :return: None
        """

        try:
            item = self.treeview.item(self.treeview.focus())
            self.f_name1.set(item["values"][0])
            self.l_name1.set(item["values"][1])
            self.u_name1.set(item["values"][4])
            self.cls1.set(item["values"][5])
            self.sec1.set(item["values"][6])
            self.e_add1.set(item["values"][2])
            self.user.set(item["values"][3])
            self.usname["state"] = NORMAL
            self.usname.delete(0, END)
            self.usname.insert(0, item["values"][0])
            self.usname["state"] = DISABLED
            self.updt1["state"] = NORMAL
            self.del_btn["state"] = NORMAL
            query = "select Password from login where UserName = %s"
            value = (self.user.get(),)
            pas = self.db.select(query,value)
            self.passwd.set(pas[0][0])
        except IndexError:
            pass

    def sort_option(self,*args):
        """This function is called when a user chooses sorting option from option menu.
        This Function is responsible for calling sorting method which is located at
        backend package."""
        global index
        chosen_option = self.sort_method.get()
        if chosen_option == "First Name":
            index = 0
        elif chosen_option == "Last Name":
            index = 1
        elif chosen_option == "Class":
            index = -3
        query = "select * from user_info"
        try:
            sorted_record = backend.searching_sorting.sorting.insertion_sort(backend.searching_sorting.searching,
                                                                             self.db.select(query), index)
            self.treeview.delete(*self.treeview.get_children())
            for ii in sorted_record:
                self.treeview.insert("", "end", values=ii)
        except:
            pass


    def search_user(self,*args):
        """This function is called when a user chooses searching option from option menu.
                This Function is responsible for calling searching method which is located at
                backend package."""
        global index
        method = self.selected_search_method.get()
        query = "select * from user_info"
        lists = self.db.select(query)
        if method == "First Name":
            index = 0
        elif method == "Last Name":
            index = 1

        search_object = backend.searching_sorting.searching(lists)
        user = search_object.linear_search(index,self.search.get())
        self.treeview.delete(*self.treeview.get_children())
        if user:
            for ii in user:
                self.treeview.insert("", "end", values=ii)

        else:
            messagebox.showinfo("User Not Found",
                                "No student with First/Last name " + self.search.get() + " found in our records")





    def opt_call(self, *args):
        """This function is called when an user is selected from dropdown menu.
        This function simply removes previous entry values and call showing_values_in_entry which will
        insert marks of selected student in entry box."""
        try:
            self.Percentage_label.grid_forget()
        except:
            pass

        self.showing_values_in_entries()

    def showing_values_in_entries(self):
        """Function to show marks of selected users in respective entry boxes."""
        global Total, marks
        selected_user = self.selected_user.get()
        self.txt_box["state"] = NORMAL
        self.send_btn["state"] = NORMAL
        usename = str(selected_user)
        query = "select * from grades where UserName = %s"
        value = (usename,)
        records = self.db.select(query, value)

        for marks in records:
            Mth.set(marks[1])
            Sci.set(marks[2])
            Nep.set(marks[3])
            Eng.set(marks[4])
            Soc.set(marks[5])
            Com.set(marks[6])
            EP.set(marks[7])
            Geo.set(marks[8])

        Total = marks[-2]
        self.total_label = Label(self.lbl2,
                                 text=("    Total::             " + "\n" + "            " + str(Total)) + '\n',
                                 justify=LEFT, compound=LEFT,
                                 padx=0, font=4, bg=self.col[0], fg=self.col[1])
        self.total_label.grid(row=1, column=2, rowspan=2)
        self.pert = Label(self.lbl2, text="Percentage:: ", justify=LEFT, compound=LEFT, padx=0, font=4, bg=self.col[0],
                          fg=self.col[1])
        self.pert.grid(row=4, column=2)
        self.Percentage_label = Label(self.lbl2, text=(str(Total / 8)), justify=LEFT, compound=LEFT,
                                      padx=0, font=30, bg=self.col[0], fg=self.col[1])
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
        query = "select EAddress from user_info where UserName =%s "
        values = (self.selected_user.get(),)
        self.email = self.db.select(query,values)
        self.eml_add_lbl.insert(END, self.email)
        self.eml_add_lbl["state"] = DISABLED


    def updating_values(self):
        """To update student's marks"""
        global Total
        g = model.grades.Grades(Mth.get(), Sci.get(), Nep.get(), Eng.get(), Soc.get(), Com.get(), EP.get(), Geo.get(),
                                self.selected_user.get())
        if int(g.get_math()) > 100 or int(g.get_science()) > 100 or int(g.get_nepali()) > 100 \
                or int(g.get_english()) > 100 or int(g.get_social()) > 100 or int(g.get_computer()) > 100 \
                or int(g.get_eph()) > 100 or int(g.get_geography()) > 100:

            messagebox.showerror("Invalid Marks", "Please enter marks less than or equal to 100.")


        elif int(g.get_math()) < 0 or int(g.get_science()) < 0 or int(g.get_nepali()) < 0 or int(g.get_english()) < 0 \
                or int(g.get_social()) < 0 or int(g.get_computer()) < 0 or int(g.get_eph()) < 0 \
                or int(g.get_geography()) < 0:

            messagebox.showerror("Invalid Marks", "Please enter marks greater than or equal to 0.")


        else:
            query = "replace into  grades(Maths, Science, Nepali, English, Social, Computer, EPH, Geography,UserName)\
                     values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"

            values = [g.get_math(), g.get_science(), g.get_nepali(), g.get_english(), g.get_social(), g.get_computer(),
                      g.get_eph(), g.get_geography(), g.get_username()]

            self.db.update(query, values)

            messagebox.showinfo("Update", "Records Updated")
            self.send_btn["state"] = NORMAL

    def updating_info(self):
        """Cretes new window where user's personal info such as f/l name is displayed which can be changed by admin."""
        self.usname["state"] = DISABLED
        self.info_win = Toplevel(self.root3, bg="black")
        f_name = Entry(self.info_win, font=('Verdana', 12), bg="black", fg="white", textvariable=self.f_name1)
        f_name.grid(row=1, column=1)
        l_name = Entry(self.info_win, font=('Verdana', 12), bg="black", fg="white", textvariable=self.l_name1)
        l_name.grid(row=2, column=1)
        u_name = Entry(self.info_win, font=('Verdana', 12), bg="black", fg="white", textvariable=self.u_name1)
        u_name.grid(row=3, column=1)
        u_pas = Entry(self.info_win, font=('Verdana', 12), bg="black", fg="white", textvariable=self.passwd)
        u_pas.grid(row=4, column=1)
        cls = Entry(self.info_win, font=('Verdana', 12), bg="black", fg="white", textvariable=self.cls1)
        cls.grid(row=5, column=1)
        sec = Entry(self.info_win, font=('Verdana', 12), bg="black", fg="white", textvariable=self.sec1)
        sec.grid(row=6, column=1)

        e_add = Entry(self.info_win, font=('Verdana', 12), bg="black", fg="white", textvariable=self.e_add1)
        e_add.grid(row=7, column=1)
        updt1 = Button(self.info_win, text="Update Info", command=self.updating_recs,
                       height=2, width=35)
        updt1.grid(row=8, column=0, rowspan=2, columnspan=2, padx=10)
        self.detail_label("First Name: ", 1, 0)
        self.detail_label("Last Name: ", 2, 0)
        self.detail_label("User Name: ", 3, 0)
        self.detail_label("Password: ", 4, 0)
        self.detail_label("Class: ", 5, 0)
        self.detail_label("Section: ", 6, 0)
        self.detail_label("Email Address: ", 7, 0)

    def detail_label(self, Text, X, Y):
        """This function creates all the labels for info_win window.
        Text = Text to display on widget
        X=Row of widget
        Y=Column of widget
        """
        Label(self.info_win, text=Text, justify=LEFT, compound=LEFT, font=10, bg="black", fg="white").grid(row=X,
                                                                                                           column=Y)

    def updating_recs(self):
        """Updates personal info such as f/l name."""
        query = """UPDATE user_info SET
                                FName = %s,
                                LName = %s,
                                Class = %s,
                                Section = %s,
                                EAddress = %s

                                WHERE UserName = %s """

        u = model.user.User(fname=self.f_name1.get(), lname=self.l_name1.get(), cls=self.cls1.get(),
                            sec=self.sec1.get(),
                            eadd=self.e_add1.get(), uname=self.user.get(), passwd=self.passwd.get())
        values = [u.get_fname(), u.get_lname(), u.get_cls(), u.get_sec(), u.get_eadd(), u.get_uname()]

        self.db.update(query, values)
        query = "update login set Password = %s where UserName = %s"
        value = [u.get_passwd(),u.get_uname()]
        self.db.update(query,value)

        messagebox.showinfo("Update", "Records Updated")
        self.info_win.destroy()
        self.query()

    def __Gmail_msg(self):
        """Sends email to the selected users."""
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465)as smtp:
                Email_address = os.environ.get("UserEmail")
                Email_pass = os.environ.get("UserPassword")
                msg = EmailMessage()
                msg["Subject"] = "Academic Records Updated!!"
                msg["From"] = Email_address
                msg["To"] = self.email[0][0]
                msg.set_content(self.txt_box.get(1.0, END))
                smtp.login(Email_address, Email_pass)
                smtp.send_message(msg)
                messagebox.showinfo("Sucess", "Message Sent!")

        except Exception as e:
            print(e)
            messagebox.showerror("Error!", str(e))

    def delete_user(self):
        query = "delete from user_info where UserName = %s"
        u = model.user.User(uname=self.user.get())
        value = (u.get_uname(),)
        self.db.delete(query, value)
        messagebox.showinfo("Success", "User Record deleted")
        self.query()


