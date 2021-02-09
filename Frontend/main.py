from tkinter import *

from PIL import ImageTk, Image





class TKWindow():
    """This is main window which will be inherited by all the classes expect "Database class" """
    def __init__(self):
        self.root = Tk()
        self.root.title("Login Page") #Setting title of first window
        self.root.geometry("1067x600+230+40")  # Defining screen size of our app
        self.root.iconbitmap('Images/logo.ico') # importing logo from "Images" folder
        self.Reg_fonts = ('Helvetica', 12)
        self.sft_img = ImageTk.PhotoImage(Image.open("Images/softwarica.png")) #Placing image inside label
        self.wel = LabelFrame(self.root, bg="black", highlightbackground="black", highlightcolor="black")
        self.wel.pack(side="top", fill="x") #Creating frames which will hold college's logo
        self.logo_img = Label(self.wel, image=self.sft_img, bg="black")
        self.logo_img.pack(fill="both", expand=3)
        logo_img = ImageTk.PhotoImage(Image.open("Images/Student2.png")) #Importing logo
        self.std_log = Label(self.wel, image=logo_img, bg="black")
        self.std_log.place(x=0, y=0) #Placing logo on left
        self.std_log1 = Label(self.wel, image=logo_img, bg="black")
        self.root.iconbitmap('Images/logo.ico')






