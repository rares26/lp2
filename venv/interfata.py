import tkinter as tk
from tkinter import *

body = tk.Tk() #declarare gui

canvas = tk.Canvas(body, height=700, width=700,bg="#33a6cc") #declarere canvas
canvas.pack() #initializare canvas

butonCalculeaza = tk.Button(body,text="Calculeaza") #declarere buton
butonCalculeaza.pack() #initializare buton

textTitlu = tk.Text(body,height=1,width=18)
textTitlu.place(x=280,y=1)
textTitlu.insert(tk.END,"Calculator Calorii")

inputVarsta = Entry(body,width = 10) #declarere inputVarsta
inputVarsta.place(x=90, y=100) #initializare inputVarsta
textVarsta = tk.Text(body,height=1,width=7)
textVarsta.place(x=15, y=100)
textVarsta.insert(tk.END,"Varsta:")

inputGreutate = Entry(body,width = 10)
inputGreutate.place(x=110, y=150)
textGreutate = tk.Text(body,height=1,width=9)
textGreutate.place(x=15, y=150)
textGreutate.insert(tk.END,"Greutate:")

inputInaltime = Entry(body,width = 10)
inputInaltime.place(x=110, y=200)
textInaltime = tk.Text(body,height=1,width=9)
textInaltime.place(x=15, y=200)
textInaltime.insert(tk.END,"Inaltime:")

inputActivitate = Menubutton(body,text="Activitate",width = 12)
inputActivitate.place(x=130, y=250)
inputActivitate.menu = Menu(inputActivitate,tearoff= 0)
inputActivitate["menu"] = inputActivitate.menu
sedentarVar=StringVar
activitateRedusaVar=StringVar
activVar=StringVar
fActivVar=StringVar
inputActivitate.menu.add_checkbutton(label="Sedentar", variable=sedentarVar)
inputActivitate.menu.add_checkbutton(label="Activitate Redusa",variable=activitateRedusaVar)
inputActivitate.menu.add_checkbutton(label="Activ",variable=activVar)
inputActivitate.menu.add_checkbutton(label="Foarte Activ",variable=fActivVar)
textActivitate = tk.Text(body,height=1,width=12)
textActivitate.place(x=15, y=250)
textActivitate.insert(tk.END,"Activitate:")

barbat=tk.BooleanVar()
femeie=tk.BooleanVar()
checkBarbat = Checkbutton(body,text="Barbat",variable=barbat,width=10)
checkBarbat.place(x=130,y=300)
checkFemeie = Checkbutton(body,text="Femeie",variable=femeie)
checkFemeie.place(x=220,y=300)
textInaltime = tk.Text(body,height=1,width=9)
textInaltime.place(x=15, y=300)
textInaltime.insert(tk.END,"Sex:")




body.mainloop() #initializare GUI
