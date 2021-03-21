# Licenza GNU Open Source.Copyleft LiteSoft INC. http://fuckingcopyright.wordpress.com 
# Ogni utente pu� prendere il codice sorgente di questo programma e modificarlo come vuole,
# pu� migliorarlo,sviluppare una propria versione basandosi su questo codice.
# L'utente deve sempre citare la fonte.
# L'utente non deve vendere il programma,il programma deve restare open source e completamente free.
# L'utente pu� condividere con chiunque il programma in questione 

# Mario Linguito , Sviluppatore CEO LiteSoft INC. 

import time
import pickle

class Info: 
    Nome=0
    Company=0
    Sito_Web=0
    def StampaInfo(self):
        print "Sviluppatore:" + str(self.Nome) + "\n" + "Comany:" + str(self.Company) + "\n" + "Sito Web:" + str(self.Sito_Web)
        StampaIstruzioni()

def StampaIstruzioni():
    print "_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-"
    print " [Istruzioni] PyManagement è un programma gestionale"
    print "come tutti gli altri programmi gestionali scritti in C,C++,Vb.net "
    print "e in altri linguaggi di programmazione"
    print ",solamente che questo è scritto in Python,uno dei migliori linguaggi di programmazione" 
    print ".L'interfaccia,anche se a linea di comando,rende il programma molto facile da usare." 
    print "Il programma serve principalmente a gestire database,che poi vengono salvati come file di testo" 
    print "nella cartella dove risiede il programma."
    print "Si può impostare anche una password per rendere il programma " 
    print "più sicuro..." 
    print "Nel programma sono presenti anche alcuni modelli predefiniti,"
    print "per dimostrare all'utente la potenza del programma " 
    print "e possono anche essere usati personalmente..." 
    print "Copyright (C) 2011 LiteSoft " 
              
    
class Password:
    pass
    
def Home():
    Nome=raw_input("Nome e Cognome:")
    Indirizzo=raw_input("Indirizzo e-mail:")
    Eta=input("Età:")
    print "Benvenuto ",Nome,".Indirizzo email:",Indirizzo,"Eta:",Eta
    UltimoUtilizzo(Nome,Indirizzo,Eta)
    try:
        inserisci=raw_input("Password:")
        dati=open("Dati123.dat","r")
        password=str(dati.read())
        if inserisci==password:
            print "Password verificata..."
            Home1(Nome,Indirizzo,Eta)
        else:
            print "Password non riconosciuta..."
    except:
        print "Nessuna Password Impostata..."
        Home1(Nome,Indirizzo,Eta)
        
    
def Home1(Nome,Indirizzo,Eta):
    print "-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-"
    print
    print "______       ______ "                                                      
    print "(_____ \     |  ___ \                                                 _    "
    print " _____) )   _| | _ | | ____ ____   ____  ____  ____ ____   ____ ____ | |_ " 
    print "|  ____/ | | | || || |/ _  |  _ \ / _  |/ _  |/ _  )    \ / _  )  _ \|  _) "
    print "| |    | |_| | || || ( ( | | | | ( ( | ( ( | ( (/ /| | | ( (/ /| | | | |__ "
    print "|_|     \__  |_||_||_|\_||_|_| |_|\_||_|\_|| |\____)_|_|_|\____)_| |_|\___)"
    print "        (____/                         (_____| "                            
    print
    print "-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-"
    print
    print "     A- Crea un nuovo database                D- Modelli"
    print "     B- Accedi ad un database                 E- Info"
    print "     C- Scrivi in un database                 F- Imposta una password"
    print 
    print "-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-"
    print "     X- Exit"
    Scelta=raw_input(">>>")
    while Scelta == "a" or "b" or "c" or "x":
        if Scelta == "a":
            CreaDatabase(Nome,Indirizzo,Eta)
            break
        elif Scelta == "b":
            AccediDatabase(Nome,Indirizzo,Eta)
            break
        elif Scelta == "c":
            ScriviDatabase(Nome,Indirizzo,Eta)
            break
        elif Scelta == "d":
            Esempi(Nome)
            break
        elif Scelta == "e":
            info=Info()
            info.Nome="Mario Linguito"
            info.Company="LiteSoft"
            info.Sito_Web="http://fuckingcopyright.wordpress.com"
            info.StampaInfo()
            print
            print "NOTA:Non si è bloccato il programma,ma devi solo aspettare 5 secondi!"
            print 
            time.sleep(5)
            Home1(Nome,Indirizzo,Eta)
            break
        elif Scelta=="f":
            passw=Password()
            passwo=raw_input("Password:")
            passw.password=(passwo)
            print "La tua password è:"+passw.password
            dati=open("Dati123.dat","w")
            dati.write(passw.password)
            dati.close()
            Home1(Nome,Indirizzo,Eta)
            break
        elif Scelta == "x":
            exit
            break
        else:
            print "Comando non riconosciuto"

def UltimoUtilizzo(Nome,Indirizzo,Eta):
    UltimoU=open("UltimoUtilizzo.dat","w")
    UltimoU.write(Nome+","+Indirizzo+","+str(Eta))
    UltimoU.close()

def CreaDatabase(Nome,Indirizzo,Eta):
    NomeD=raw_input("Nome Database:")
    database=open(NomeD+".dat","w")
    database.write("Database creato da "+Nome+","+Indirizzo+","+str(Eta))
    database.close()
    Home1(Nome,Indirizzo,Eta)
    
def AccediDatabase(Nome,Indirizzo,Eta):
    NomeD=raw_input("Nome Database:")
    try:
        database=open(NomeD,"r")
        leggi=database.read()
        print leggi
        print "\n"
    except:
        print "File non esistente \n"
    Home1(Nome,Indirizzo,Eta)

def ScriviDatabase(Nome,Indirizzo,Eta):
    NomeD=raw_input("Nome Database:")
    try:
        scrivi=raw_input(">>>")
        database=open(NomeD,"w")
        database.write(str(scrivi))
        database.close()
    except:
        print "File non esistente \n"
        
    Home1(Nome,Indirizzo,Eta)

def Esempi(Nome):
    print "Benvenuto "+Nome
    print "Questi sono alcuni modelli"
    HomeEsempi()

def HomeEsempi():
    print "-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-"
    print "I modelli disponibili sono:\n 1- Gestione di una libreria \n 2- Gestione di una videoteca"
    print
    scelta=input(">>>")
    if scelta==1:
        Libreria()
    elif scelta==2:
        Videoteca()
    else:
        Home()
data={}

def Libreria():
    print "-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-"
    print " A- Aggiungi Libro                        D- Lunghezza database"
    print " B- Rimuovi Libro                         E- Cerca un libro"
    print " C- Stampa intero database                F- Salva il database"
    print "-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-"
    print " X- Esci"
    print 
    scelta=raw_input(">>>")
    if scelta=="a":
        NomeA=raw_input("Nome autore libro:")
        NomeL=raw_input("Nome libro:")
        Anno=input("Anno p.:")
        data[NomeA+","+NomeL]=Anno
        print "Libro aggiunto con successo"
        Libreria()
    elif scelta=="b":
        NomeA=raw_input("Nome autore Libro:")
        NomeL=raw_input("Nome Libro:")
        del data[NomeA+","+NomeL]
        print "Libro rimosso con successo..."
        Libreria()
    elif scelta=="c":
        print data
        Libreria()
    elif scelta=="d":
        print len(data)
        print "Operazione eseguita con successo..."
        Libreria()
    elif scelta=="e":
        NomeA=raw_input("Nome autore libro:")
        NomeL=raw_input("Nome libro:")
        risu=data.has_key(NomeA+","+NomeL)
        print risu
        Libreria()
    elif scelta=="f":
        pickle.dump(data,open("Libreria.dat","wb"))
        time.sleep(1)
        print "Operazione Eseguita con successo!"
        Libreria()
    elif scelta=="x":
        exit
    else:
        print "Comando non riconosciuto"

datav={}

def Videoteca():
    print "-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-"
    print " A- Aggiungi Film                        D- Quanti Film ci sono?"
    print " B- Rimuovi Film                         E- Cerca un Film"
    print " C- Visualizza tutti i Film              F- Salva tutti  Film in un file"
    print "-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-"
    print " X- Exit"
    print
    scelta=raw_input(">>>")
    if scelta=="a":
        addFilm=raw_input("Nome Film:")
        addAuthor=raw_input("Nome autore Film:")
        addYear=raw_input("Anno:")
        datav[addFilm + " di " + addAuthor] = addYear
        Videoteca()
    elif scelta=="b":
        addFilm=raw_input("Nome Film:")
        addAuthor=raw_input("Nome autore Film:")
        addYear=raw_input("Anno:")
        del datav[addFilm]
        Videoteca()
    elif scelta=="c":
        print datav
        Videoteca()
    elif scelta=="d":
        print str(len(datav))
        Videoteca()
    elif scelta=="e":
        addFilm=raw_input("Nome Film:")
        addAuthor=raw_input("Nome autore Film:")
        risu=datav.has_key(addFilm+" , "+addAuthor)
        print risu
    elif scelta=="f":
        pickle.dump(data,open("Videoteca.dat","wb"))
        time.sleep(1)
        print "Operazione eseguita con successo!"
        Libreria()
    elif scelta=="x":
        exit 
    else:
        print "Comando non riconosciuto"
    
Home()
