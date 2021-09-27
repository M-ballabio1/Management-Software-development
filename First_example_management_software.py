"""
IMPLEMENTARE UN programma per la gestione dei ricoveri di un ospedale. Ogni paziente è organizzato attraverso un dizionario
in cui oltre alla chiavi Nome,Cognome,CF,reparto vengono memorizzati gli esiti degli esami utilizzando come chiave il nome
dell'esame stesso.
L'insieme dei degenti è organizzato con una lista(di dizionari) e il programma deve prevedere diverse funzioni:
-inserimento di un nuovo ricovero,con data ricovero
-inserimento esiti degli esami
-dimissione di un degente
-visualizzazione cartella clinica di un paziente(dati anagrafici e esami)
-visualizzazione tutti esiti di un dato esame
-visualizzazione tutti i ricoveri di un dato reparto.
"""

import tkinter
from tkinter import *

bio= Tk()


inizio1=Frame(bio)
inizio1.pack()

pulsante1=Button(inizio1)
pulsante1["text"] = "Ciao, Mondo!"
pulsante1["background"] = "green"
pulsante1.pack()

bio.mainloop()

def menu():
    print(""" MENU':
    1)INSERIMENTO NUOVO RICOVERO
    2)INSERIMENTO ESITI ESAMI
    3)DIMISSIONE DI UN DEGENTE
    4)VISUALIZZAZIONE CARTELLA CLINICA
    5)VISUALIZZAZIONE TUTTI ESITI DI UN ESAME
    6)VISUALIZZAZIONE TUTTI RICOVERI DI UN REPARTO
    0)EXIT""")
    scelta = int(input("Insersci opzione:"))
    return scelta



def agg_paziente():
    nome=input("inserisci nome: ")
    cognome=input("inserisci cognome: ")
    CF=input("inserisci codice  fiscale: ")
    reparto=int(input("inserisci numero reparto: "))
    data_ricovero=(input("data_ricovero: "))
    paziente = {"nome":nome,                                       #paziente è una variabile locale
                "cognome":cognome,
                "CF":CF,
                "Reparto":reparto,
                "data_ricovero":data_ricovero,
                "esami":{} }

    Insieme_degenti.append(paziente)


def inserimento_esiti():
    CF = input("CF: ")
    esame  = (input("esame: "))
    esito = (input("esito: "))
    for paz in Insieme_degenti:
        if paz["CF"] == CF:                   #dice che se codice fiscale inserito qua è uguale a qualche codice
            paz["esami"][esame] =esito        #presente da qualche parte che abbiamo inserito quando è
            return                            #arrivato un paziente,



Insieme_degenti = []   #



def Dimissione_Degente():
    CF = input("CF: ")
    indice = -1

    for i in range (len(Insieme_degenti)):
        paz = Insieme_degenti[i]
        if paz["CF"] == CF:
            indice = i
            break
    if indice == -1:
        print("paziente non trovato")
    else:
        Insieme_degenti.pop(indice)



def CartellaClinica():
    CF = input("CF: ")
    for paz in Insieme_degenti:
        if paz["CF"] == CF:
            print(paz)



def EsitiSingoloEsame():
    esame = input("esame: ")
    for p in Insieme_degenti:
        diz_esami = p["esami"]
        if esame in diz_esami:
            print("%s %s: %s" % (p["nome"],p["cognome"],diz_esami[esame]))



def RicoveriDatoReparto():
    rep = input("reparto: ")
    for p in Insieme_degenti:
        if p["reparto"] == rep:
            print(p)
"""
    DF = {1: menu,
          2: agg_paziente,
          3: inserimento_esiti,
          4: Dimissione_Degente,
          5: CartellaClinica,
          6: EsitiSingoloEsame,
          7: RicoveriDatoReparto}
"""
while True:
    scelta = menu()
    #try:
        #DF[scelta]()
        #except KeyError as ke:
            #print("scelta sbagliata")
    if scelta == 1:
        agg_paziente()
    elif scelta == 2:
        inserimento_esiti()
    elif scelta ==3:
        Dimissione_Degente()
    elif scelta ==4:
        CartellaClinica()
    elif scelta ==5:
        EsitiSingoloEsame()
    elif scelta ==6:
        RicoveriDatoReparto()
    else:
        print("scelta sbagliata")
