import random
import time
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

class Registrazione:
    def __init__(self,root):
        self.root = root
        self.root.title("Registrazione Pazienti")
        self.root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
        self.root.configure(background="dark blue")

        ##TITOLO
        titolo = Label(self.root, text=" Registrazione Nuovi Pazienti ",
                            font=("Times New Roman", 45, "bold"), bd=10, relief=GROOVE, bg="#6895e3")
        titolo.pack(side=TOP, fill = X)

        #FRAME principale - dati
        FramePrincipale = Frame(self.root, bd=1, relief=RIDGE, bg="#daf5f7")
        FramePrincipale.place(x=15, y=105, width=500, height=680)

        PazTitolo = Label(FramePrincipale, text="Anagrafica Pazienti", font=("Times New Roman", 20, "bold"), bg="#daf5f7", fg="black")
        PazTitolo.grid(row=0, columnspan=2, pady=5)

        Paz_Date = Label(FramePrincipale, text="Data Odierna", font=("Times New Roman", 15, "bold"), bg="#daf5f7", fg="black")
        Paz_Date.grid(row=1, columnspan=2, pady=5, padx=10, sticky= "w")



        #Frame secondario - dettagli
        dettagli_frame = Frame(self.root, bd=1, relief=RIDGE, bg="#daf5f7")
        dettagli_frame.place(x=550,y=105, width=965, height=680)

        ##



if __name__ == '__main__':
    root = Tk()
    app = Registrazione(root)
    root.mainloop()