#Importieren der Module
from tkinter import *
from tkinter import ttk
import tkinter as tk
import random
import pyperclip as pc

#Fenster einstellungen
generator =tk.Tk()
generator.geometry("400x350")
generator.resizable(False,False)
generator.title("Password Generator")
tabControl=ttk.Notebook(generator)

pwgen=ttk.Frame(tabControl)
pwlist=ttk.Frame(tabControl)

tabControl.add(pwgen,text='PW Generator')
tabControl.add(pwlist,text='PW List')
tabControl.pack(expand=1,fill="both")

#globale Variabeln Speichern
auswahl = 1
password =""

#--------------------------------------------Passwort-Generieren--------------------------------------------------------#
#Funktion Passwort Generieren
#Passwort Variablen erstellen
upperletter1=chr(random.randint(65,90))
upperletter2=chr(random.randint(65,90))    
upperletter3=chr(random.randint(65,90))
upperletter4=chr(random.randint(65,90))

lowerletter1 = chr(random.randint(97,122))
lowerletter2 = chr(random.randint(97,122))
lowerletter3 = chr(random.randint(97,122))
lowerletter4 = chr(random.randint(97,122))

numletter1 = chr(random.randint(48,57))
numletter2 = chr(random.randint(48,57))
numletter3 = chr(random.randint(48,57))
numletter4 = chr(random.randint(48,57))

punctuaionletter1 = chr(random.randint(33,47))
punctuaionletter2 = chr(random.randint(33,47))
punctuaionletter3 = chr(random.randint(33,47))
punctuaionletter4 = chr(random.randint(33,47))

#Generierung des Passwords
def shuffel (string):
    templist = list(string)
    random.shuffle(templist)
    return''.join(templist)
#Berechnung des Passwords
def schwach ():
    global auswahl, password
    auswahl = 1
    password = upperletter1+upperletter2+lowerletter1+lowerletter2+numletter1+numletter2+punctuaionletter1+punctuaionletter2

def normal ():
    global auswahl,password
    password = upperletter1+upperletter2+upperletter3+lowerletter1+lowerletter2+lowerletter3+numletter1+numletter2+numletter3+punctuaionletter1+punctuaionletter2+punctuaionletter3

def stark ():
    global auswahl,password
    password = upperletter1+upperletter2+upperletter3+upperletter4+lowerletter1+lowerletter2+lowerletter3+lowerletter4+numletter1+numletter2+numletter3+numletter4+punctuaionletter1+punctuaionletter2+punctuaionletter3+punctuaionletter4

#Ausführung des berechnen Button
def  berechnen():
    global auswahl,password
    if auswahl == 1 :
        password=str(shuffel(password))
        password1.config(text=password)

    elif auswahl == 2 :
        password = upperletter1+upperletter2+upperletter3+lowerletter1+lowerletter2+lowerletter3+numletter1+numletter2+numletter3+punctuaionletter1+punctuaionletter2+punctuaionletter3
        password=str(shuffel(password))
        password1.config(text=password)
        
    elif auswahl == 3 :
        password = upperletter1+upperletter2+upperletter3+upperletter4+lowerletter1+lowerletter2+lowerletter3+lowerletter4+numletter1+numletter2+numletter3+numletter4+punctuaionletter1+punctuaionletter2+punctuaionletter3+punctuaionletter4
        password=str(shuffel(password))
        password1.config(text=password) 

#Erstellung und Funktion des Copy Button
def copyit(*args):
    pc.copy(password1.cget("text"))

#Password ausgabe & Bind des Copybutton
password1 =Label(pwgen,bg="lightgray",justify=CENTER, text="",font=('times',20))
password1.place(x=75,y=200 ,width=250)
password1.bind("<Button-3>", copyit)

copybutton=Button(pwgen,bg="green",text="Copy", command=copyit ,cursor='hand2' )
copybutton.place(x=268 ,y= 160 , width= 50 ,height=30)

#Überschrift im Fenster
Label(pwgen, text="Willkommen im Password Generator :) ",font=('times',15,'bold','italic')).place(x=35,y=10)

#text für die Raidobutton
Label(pwgen, text="Wählen sie eine Sicherheitsstufe!",padx=20,font=('times',12,'bold','italic')).place(x=70, y=72)

#Setzen der default einstellung der Radiobutton
default = tk.IntVar() 
default.set(1)

#Erstellung der Radiobutton
r1 = Radiobutton(pwgen, text="Schwach", value=1, variable=default, command=schwach).place(x=70,y=115)
r2 = Radiobutton(pwgen, text="Normal", value=2, variable=default, command=normal).place(x=175,y=115)
r3 = Radiobutton(pwgen, text="Stark", value=3, variable=default, command=stark).place(x=270,y=115)

#Berechnen-Button erstellen
passwordgenerieren = Button(pwgen,bg='#FBD975',text="Password Generieren" ,cursor='hand2',command=berechnen,justify=CENTER ,padx=25)
passwordgenerieren.place(x=85 ,y=160,width=180 ,height=30)

#---------------------------------Passwort Liste-------------------------------------------------------------------------#

Label(pwlist, text="""Passwort Liste""",justify=CENTER,padx=20,font=('times',15,'bold','italic')).pack()

#---------------------------------Footer---------------------------------------------------------------------------------#
#Fußzeile für Copyright
crlabel=Label(generator ,text="© Copyright by DravenSoft since 2021",font=1).pack(side="bottom")

#Mainloop  für das Fenster
generator.mainloop()