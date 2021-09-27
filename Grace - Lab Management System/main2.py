# IMPORT MODULE

# model
# https://www.youtube.com/watch?v=9QGdK8tD1Rw

import random
import time
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from PIL import Image, ImageTk
import cv2
import numpy as np
import pandas as pd


# MAIN

def main():
    root = Tk()
    app = finestra1(root)
    root.mainloop()


class finestra1:
    def __init__(self, master):
        self.master = master
        self.master.title("GRACE - Lab Management System")
        self.master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth(), master.winfo_screenheight()))  # definisco dimensioni finestra GUI
        self.master.configure(bg="dark blue")  # configurare sfondo finestra principale

        self.frame = Frame(self.master, bg="lightblue")
        self.frame.pack()

        load = Image.open("health-medical-laboratory6.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self.master, image=render, bg='dark blue')
        img.image = render
        img.place(x=350, y=430)

        self.Username = StringVar()
        self.Password = StringVar()

        # creazione frame titolo principale

        self.LabelTitle = Label(self.frame, text=" GRACE - Lab Management System ",
                                font=("Times New Roman", 45, "bold"), bd=10, relief=GROOVE)
        self.LabelTitle.grid(row=0, column=1, columnspa=2, pady=10)
        # creazione frame accesso pazienti registrazione
        self.Accessoframe1 = Frame(self.frame, width=1000, height=300, bd=10, relief=SUNKEN)
        self.Accessoframe1.grid(row=1, column=1, columnspan=2, pady=10)
        # creazione frame accesso area pazienti
        """
        self.Accessoframe2 = Frame(self.frame, width= 1500, height=300, bd=10, relief=SUNKEN)
        self.Accessoframe2.grid(row = 3, column = 1, columnspan = 2 , pady = 15)
        """
        # creazione frame accesso area riservata personale
        self.Accessoframe3 = Frame(self.frame, width=1000, height=300, bd=10, relief=SUNKEN)
        self.Accessoframe3.grid(row=6, column=1, columnspan=2, pady=5)

        self.button_reg = Button(self.Accessoframe3, text="Registrazione pazienti",
                                 font=("Times New Roman", 15, "bold"),
                                 command=self.finestra_Registrazione, state=DISABLED)
        self.button_reg.grid(row=1, column=0, padx=10, pady=10)
        """
        self.button_paz = Button(self.Accessoframe3, text="Esami di laboratorio", font=("Times New Roman", 15, "bold"),
                                 command=self.finestra_AreaPazienti)
        self.button_paz.grid(row=1, column=1, padx=10, pady=10)

        self.button_paz = Button(self.Accessoframe3, text="Esami strumentali", font=("Times New Roman", 15, "bold"),
                                 command=self.finestra_AreaPazienti)
        self.button_paz.grid(row=2, column=1, padx=10, pady=10)

        self.button_paz = Button(self.Accessoframe3, text="Area consulto medico", font=("Times New Roman", 15, "bold"),
                                 command=self.finestra_AreaPazienti)
        self.button_paz.grid(row=2, column=1, padx=10, pady=10)

        self.button_paz = Button(self.Accessoframe3, text="Prenotazione prestazione", font=("Times New Roman", 15, "bold"),
                                 command=self.finestra_AreaPazienti)
        self.button_paz.grid(row=2, column=1, padx=10, pady=10)

        """
        self.button_ris = Button(self.Accessoframe3, text="Area Riservata Personale",
                                 font=("Times New Roman", 15, "bold"),
                                 command=self.finestra_AreaRiservata, state=DISABLED)
        self.button_ris.grid(row=1, column=2, padx=10, pady=10)

        # parte per inizializzazione username e password:
        self.LabelUsername = Label(self.Accessoframe1, text="Nome utente", font=("Times New Roman", 15, "bold"), bd=3)
        self.LabelUsername.grid(row=1, column=1)

        self.textUsername = Entry(self.Accessoframe1, font=("Times New Roman", 15, "bold"), bd=3,
                                  textvariable=self.Username)
        self.textUsername.grid(row=1, column=2, padx=40, pady=10)

        self.labelPassword = Label(self.Accessoframe1, text="Password", font=("Times New Roman", 15, "bold"), bd=3)
        self.labelPassword.grid(row=2, column=1)

        self.textPassword = Entry(self.Accessoframe1, font=("Times New Roman", 15, "bold"), show="*", bd=3,
                                  textvariable=self.Password)
        self.textPassword.grid(row=2, column=2, padx=40, pady=10)

        # pulsante login - reset - exit
        self.button_accesso = Button(self.Accessoframe1, text="Accedi", width=10, font=("Times New Roman", 15, "bold"),
                                     command=self.login_sistema)
        self.button_accesso.grid(row=10, column=1, padx=10, pady=10)

        self.button_reset = Button(self.Accessoframe1, text="Reset", width=10, font=("Times New Roman", 15, "bold"),
                                   command=self.reset_button)
        self.button_reset.grid(row=10, column=2, padx=10, pady=10)

        self.button_esci = Button(self.Accessoframe1, text="Esci", width=10, font=("Times New Roman", 15, "bold"),
                                  command=self.exit_button)
        self.button_esci.grid(row=10, column=3, padx=10, pady=10)

    def login_sistema(self):
        user = self.Username.get()
        pswd = self.Password.get()

        # se username o password sono sbagliati allora è tutto disabilitato
        if (user == str("admin") and (pswd == str("admin"))):
            self.button_reg.config(state=NORMAL)
            self.button_ris.config(state=NORMAL)
        else:
            tkinter.messagebox.askyesno("GRACE - Lab Management System", "Nome utente o password non validi")
            self.button_reg.config(state=DISABLED)
            self.button_ris.config(state=DISABLED)

        self.Username.set("")
        self.Password.set("")
        self.textUsername.focus()

    def reset_button(self):
        self.button_reg.config(state=NORMAL)
        self.button_ris.config(state=NORMAL)

        self.Username.set("")
        self.Password.set("")
        self.textUsername.focus()

    def exit_button(self):
        self.exit = tkinter.messagebox.askyesno("GRACE - Lab Management System", "Sei sicuro di voler uscire?")
        if self.exit > 0:
            self.master.destroy()  # chiude la finestra principale
            return

    # definizione di tutte le finestre
    def finestra_Registrazione(self):
        self.newWindow = Toplevel(self.master)
        self.app = Registrazione(self.newWindow)

    def finestra_AreaPazienti(self):
        self.newWindow = Toplevel(self.master)
        self.app = finestra3(self.newWindow)

    def finestra_AreaRiservata(self):
        self.newWindow = Toplevel(self.master)
        self.app = finestra3(self.newWindow)


########### finestra 2 #############

class Registrazione:
    def __init__(self,root):
        self.root = root
        self.root.title("Registrazione Pazienti")
        self.root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
        self.root.configure(background="dark blue")

        ############ DEFINIRE riquadri scrittura ##############
        #orario

        DataRegistrazione = StringVar()
        DataRegistrazione.set(time.strftime("%d/%m/%y"))

        #definire
        Ref = StringVar()
        Cognome = StringVar()
        Nome = StringVar()
        Telefono_numero = StringVar()
        Codice_Fiscale = StringVar()
        Indirizzo = StringVar()
        Costo = StringVar()

        #other var1
        var1 = StringVar()
        var2 = StringVar()
        var3 = StringVar()
        var4 = StringVar()
        var5 = IntVar()

        Membri_Lab = StringVar()
        Membri_Lab.set("0")

        ###funzioni###

        def escibtt():
            escibtt = tkinter.messagebox.askyesno("Tool Registrazione pazienti", "Sei sicuro di voler uscire?")
            if escibtt > 0:
                root.destroy()
                return

        def resetbtt():
            Nome.set("")
            Cognome.set("")
            Ref.set("")
            Telefono_numero.set("")
            Codice_Fiscale.set("")
            Indirizzo.set("")
            var1.set("")
            var2.set("")
            var3.set("")
            var4.set("")
            var5.set("")
            Membri_Lab.set("")
            Paz_sesso_cbox.current(0)
            Paz_doc_cbox.current(0)
            Paz_ass_cbox.current(0)
            Paz_pag_cbox.current(0)

        def reseeetBUT():
            reseeetBUT = tkinter.messagebox.askokcancel("Tool Registrazione pazienti", "Sei sicuro di voler resettare?")
            if reseeetBUT > 0:
                resetbtt()
            elif reseeetBUT <= 0:
                resetbtt()
                dettagli_labeltxt.delete("1.0", END)
                return

        def ReferenceID():
            R_number = random.randint(10000,999999)
            randomnumber = str(R_number)
            Ref.set(randomnumber)

        def costo_Membri():

            if (var5.get() == 1):      #quando il box è cliccato
                Paz_costo_testo.configure(state = NORMAL)
                item = float(50)
                Membri_Lab.set(str(item)+ " €")
            elif (var5.get() == 0):
                Paz_costo_testo.configure(state = DISABLED)
                Membri_Lab.set("0")

        def Registra_Paz():
            ReferenceID()
            dettagli_labeltxt.insert(END,"    "+ DataRegistrazione.get()+ "            \t" + Ref.get()+ "                  " +
                                     Cognome.get()+ "                        \t"+ Nome.get()+ "                  " +Telefono_numero.get()+"           "+
                                     Indirizzo.get()+ "              "+ Paz_sesso_cbox.get()+"                  "+ Membri_Lab.get()+"\n")



        ########### DEFINIRE frame ##############
        ##TITOLO
        titolo = Label(self.root, text=" Registrazione Nuovi Pazienti ",
                            font=("Times New Roman", 45, "bold"), bd=10, relief=GROOVE, bg="#6895e3")
        titolo.pack(side=TOP, fill = X)

        #FRAME principale - dati
        FramePrincipale = Frame(self.root, bd=1, relief=RIDGE, bg="#daf5f7")
        FramePrincipale.place(x=15, y=105, width=500, height=680)

        #### SOTTOFRAME PRINCIPALE ####

        PazTitolo = Label(FramePrincipale, text="Anagrafica Pazienti", font=("Times New Roman", 20, "bold"), bg="#daf5f7", fg="black")
        PazTitolo.grid(row=0, columnspan=2, pady=5)

        #DATA (#inserisce di default la data odierna grazie al modulo "time")
        Paz_Date = Label(FramePrincipale, text="Data Odierna", font=("Times New Roman", 15, "bold"), bg="#daf5f7", fg="black")
        Paz_Date.grid(row=1, column=0, pady=5, padx=10, sticky= "w")
        Paz_Date_testo = Entry(FramePrincipale, font = ("Times New Roman", 15, "bold"), textvariable=DataRegistrazione)
        Paz_Date_testo.grid(row=1, column=1, pady=5, padx=10, sticky= "w")

        #ID REFERENCE (compilato di default dopo)
        Paz_ID_ref = Label(FramePrincipale, text="ID ", font=("Times New Roman", 15, "bold"), bg="#daf5f7",
                         fg="black")
        Paz_ID_ref.grid(row=2, column=0, pady=5, padx=10, sticky="w")
        Paz_ID_ref = Entry(FramePrincipale, font=("Times New Roman", 15, "bold"), state=DISABLED, text=Ref)
        Paz_ID_ref.grid(row=2, column=1, pady=5, padx=10, sticky="w")

        # COGNOME
        Paz_Cognome = Label(FramePrincipale, text="Cognome", font=("Times New Roman", 15, "bold"), bg="#daf5f7",
                            fg="black")
        Paz_Cognome.grid(row=3, column=0, pady=5, padx=10, sticky="w")
        Paz_Cognome_testo = Entry(FramePrincipale, font=("Times New Roman", 15, "bold"), textvariable=Cognome)
        Paz_Cognome_testo.grid(row=3, column=1, pady=5, padx=10, sticky="w")

        #NOME
        Paz_Nome = Label(FramePrincipale, text="Nome", font=("Times New Roman", 15, "bold"), bg="#daf5f7",
                         fg="black")
        Paz_Nome.grid(row=4, column=0, pady=5, padx=10, sticky="w")
        Paz_Nome_testo = Entry(FramePrincipale, font=("Times New Roman", 15, "bold"), textvariable=Nome)
        Paz_Nome_testo.grid(row=4, column=1, pady=5, padx=10, sticky="w")

        #TELEFONO
        Paz_Telefono = Label(FramePrincipale, text="Numero di Telefono", font=("Times New Roman", 15, "bold"), bg="#daf5f7",
                         fg="black")
        Paz_Telefono.grid(row=5, column=0, pady=5, padx=10, sticky="w")
        Paz_Telefono_testo = Entry(FramePrincipale, font=("Times New Roman", 15, "bold"), textvariable=Telefono_numero)
        Paz_Telefono_testo.grid(row=5, column=1, pady=5, padx=10, sticky="w")

        #INDIRIZZO
        Paz_Indirizzo = Label(FramePrincipale, text="Indirizzo", font=("Times New Roman", 15, "bold"),
                             bg="#daf5f7",
                             fg="black")
        Paz_Indirizzo.grid(row=6, column=0, pady=5, padx=10, sticky="w")
        Paz_Indirizzo_testo = Entry(FramePrincipale, font=("Times New Roman", 15, "bold"),
                                   textvariable=Indirizzo)
        Paz_Indirizzo_testo.grid(row=6, column=1, pady=5, padx=10, sticky="w")

        #CODICE FISCALE
        Paz_CF = Label(FramePrincipale, text="Codice Fiscale", font=("Times New Roman", 15, "bold"),
                             bg="#daf5f7",
                             fg="black")
        Paz_CF.grid(row=7, column=0, pady=5, padx=10, sticky="w")
        Paz_CF_testo = Entry(FramePrincipale, font=("Times New Roman", 15, "bold"),
                                   textvariable=Codice_Fiscale)
        Paz_CF_testo.grid(row=7, column=1, pady=5, padx=10, sticky="w")

        #SESSO (tendina per poter scegliere)
        Paz_sesso = Label(FramePrincipale, text="Sesso", font=("Times New Roman", 15, "bold"),
                       bg="#daf5f7",
                       fg="black")
        Paz_sesso.grid(row=8, column=0, pady=5, padx=10, sticky="w")
        Paz_sesso_cbox = ttk.Combobox(FramePrincipale, font=("Times New Roman", 15, "bold"),
                             textvariable=var1, state="readonly", width=18)
        Paz_sesso_cbox['values'] = ("","Maschio","Femmina","Altro")
        Paz_sesso_cbox.current(0)
        Paz_sesso_cbox.grid(row=8, column=1, pady=5, padx=10, sticky="w")

        # TIPOLOGIA DOCUMENTO (tendina per poter scegliere)
        Paz_doc = Label(FramePrincipale, text="Documento riconoscimento", font=("Times New Roman", 15, "bold"),
                        bg="#daf5f7",
                        fg="black")
        Paz_doc.grid(row=9, column=0, pady=5, padx=10, sticky="w")
        Paz_doc_cbox = ttk.Combobox(FramePrincipale, font=("Times New Roman", 15, "bold"),
                                    textvariable=var2, state="readonly", width=18)
        Paz_doc_cbox['values'] = ("", "Carta d'identità", "Tessera Sanitaria", "Patente di Guida")
        Paz_doc_cbox.current(0)
        Paz_doc_cbox.grid(row=9, column=1, pady=5, padx=10, sticky="w")

        # ASSICURAZIONI o SCONTO MEMBRI LAB (tendina per poter scegliere)
        Paz_ass = Label(FramePrincipale, text="Sconti parziali o totali", font=("Times New Roman", 15, "bold"),
                        bg="#daf5f7",
                        fg="black")
        Paz_ass.grid(row=10, column=0, pady=5, padx=10, sticky="w")
        Paz_ass_cbox = ttk.Combobox(FramePrincipale, font=("Times New Roman", 15, "bold"),
                                    textvariable=var3, state="readonly", width=18)
        Paz_ass_cbox['values'] = ("", "Assicurazione", "Membro Laboratorio")
        Paz_ass_cbox.current(0)
        Paz_ass_cbox.grid(row=10, column=1, pady=5, padx=10, sticky="w")

        #TIPOLOGIA PAGAMENTO PRESTAZIONE (tendina per poter scegliere)
        Paz_pag = Label(FramePrincipale, text="Pagamento prestazione", font=("Times New Roman", 15, "bold"),
                          bg="#daf5f7",
                          fg="black")
        Paz_pag.grid(row=11, column=0, pady=5, padx=10, sticky="w")
        Paz_pag_cbox = ttk.Combobox(FramePrincipale, font=("Times New Roman", 15, "bold"),
                                      textvariable=var4, state="readonly", width=18)
        Paz_pag_cbox['values'] = ("", "Contanti", "Carte Credito/Debito", "Bonfico", "Paypal")
        Paz_pag_cbox.current(0)
        Paz_pag_cbox.grid(row=11, column=1, pady=5, padx=10, sticky="w")

        #DETTAGLIO COSTO MEMEBRI O NON MEMBRI

        Paz_costo = Checkbutton(FramePrincipale, text="Costo prestazione",variable=var5, font=("Times New Roman", 15, "bold"),
                          bg="#daf5f7", onvalue = 1, offvalue = 0, command=costo_Membri)
        Paz_costo.grid(row=12, column=0, pady=5, padx=10, sticky="w")
        Paz_costo_testo = Entry(FramePrincipale, font=("Times New Roman", 15, "bold"),
                             textvariable=Membri_Lab, state=DISABLED, justify= RIGHT)
        Paz_costo_testo.grid(row=12, column=1, pady=5, padx=10, sticky="w")





        #Frame secondario - dettagli
        dettagli_frame = Frame(self.root, bd=1, relief=RIDGE, bg="#daf5f7")
        dettagli_frame.place(x=550,y=105, width=965, height=680)

        ##
        dettagli_label = Label(dettagli_frame, font=("Times New Roman", 15, "bold"), pady = 10, padx =2, width = 80,
                               text = "Data\t    Ref ID\t           Cognome\t            Nome            Telefono           Indirizzo           Sesso             Costo ")
        dettagli_label.grid(row=0, column=0, columnspan=4, sticky="w")
        dettagli_labeltxt = Text(dettagli_frame, width=123, height=34, font=("Times New Roman", 11, "bold"),
                                 bg="#daf5f7")
        dettagli_labeltxt.grid(row=1, column=0, columnspan=4)

        ### CONFERMA BUTTON ####

        receiptbtn = Button(dettagli_frame, padx= 15, bd=5, font=("Times New Roman", 15, "bold"), bg="#36a30f",
                            width = 20, text="Conferma Dati", command=Registra_Paz)
        receiptbtn.grid(row=2, column=0)

        resetbtn = Button(dettagli_frame, padx=15, bd=5, font=("Times New Roman", 15, "bold"), bg="gray",
                            width=20, text="Reset", command=reseeetBUT)
        resetbtn.grid(row=2, column=1)

        exittbtn = Button(dettagli_frame, padx=15, bd=5, font=("Times New Roman", 15, "bold"), bg="red",
                            width=20, text="Esci", command=escibtt)
        exittbtn.grid(row=2, column=2)


######## finestra 3 #############

class finestra3:
    def __init__(self, master):
        self.master = master
        self.master.title("Area Riservata Personale")
        self.master.geometry("1400x750+0+0")
        self.frame = Frame(self.master, )
        self.frame.pack()


if __name__ == '__main__':
    main()



