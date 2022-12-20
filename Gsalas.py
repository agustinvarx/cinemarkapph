import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
import tkinter.messagebox as tkMsgbox
import sqlite3

class Salas(tk.Toplevel):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        #setting title
        self.title("undefined")
        #setting window size
        width=373
        height=505
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        etiqueta1=tk.Label(self)
        etiqueta1["bg"] = "#f2f2f2"
        ft = tkFont.Font(family='calibri bold',size=16)
        etiqueta1["font"] = ft
        etiqueta1["fg"] = "#009688"
        etiqueta1["justify"] = "center"
        etiqueta1["text"] = "Cinemark App"
        etiqueta1.place(x=80,y=10,width=201,height=30)

        etiqueta2=tk.Label(self)
        etiqueta2["bg"] = "#009688"
        ft = tkFont.Font(family='calibri bold',size=12)
        etiqueta2["font"] = ft
        etiqueta2["fg"] = "#ffffff"
        etiqueta2["justify"] = "center"
        etiqueta2["text"] = "nombre de la sala"
        etiqueta2.place(x=20,y=80,width=130,height=30)

        etiqueta3=tk.Label(self)
        etiqueta3["bg"] = "#009688"
        ft = tkFont.Font(family='calibri bold',size=12)
        etiqueta3["font"] = ft
        etiqueta3["fg"] = "#ffffff"
        etiqueta3["justify"] = "center"
        etiqueta3["text"] = "capacidad"
        etiqueta3.place(x=20,y=150,width=130,height=30)

        GLabel_404=tk.Label(self)
        GLabel_404["bg"] = "#009688"
        ft = tkFont.Font(family='calibri bold',size=12)
        GLabel_404["font"] = ft
        GLabel_404["fg"] = "#ffffff"
        GLabel_404["justify"] = "center"
        GLabel_404["text"] = "pelicula"
        GLabel_404.place(x=20,y=220,width=130,height=30)

        etiqueta4=tk.Label(self)
        etiqueta4["bg"] = "#009688"
        ft = tkFont.Font(family='calibri bold',size=12)
        etiqueta4["font"] = ft
        etiqueta4["fg"] = "#ffffff"
        etiqueta4["justify"] = "center"
        etiqueta4["text"] = "formato"
        etiqueta4.place(x=20,y=290,width=125,height=30)

        lista =["2D","3D"]
        fromato_d = ttk.Combobox(self,state="readonly",values=lista,name="formato")
        fromato_d.place(x = 206,y=290)

        entry_sala=tk.Entry(self,name="sala")
        entry_sala["borderwidth"] = "1px"
        ft = tkFont.Font(family='calibri',size=12)
        entry_sala["font"] = ft
        entry_sala["fg"] = "#333333"
        entry_sala["justify"] = "center"
        entry_sala["text"] = ""
        entry_sala.place(x=180,y=80,width=168,height=30)

        entry_capacidad=tk.Entry(self,name="capacidad")
        entry_capacidad["borderwidth"] ="1px"
        ft = tkFont.Font(family='calibri',size=12)
        entry_capacidad["font"] = ft
        entry_capacidad["fg"] = "#333333"
        entry_capacidad["justify"] = "center"
        entry_capacidad["text"] = ""
        entry_capacidad.place(x=180,y=150,width=170,height=30)

        entry_pelicula=tk.Entry(self,name="pelicula")
        entry_pelicula["borderwidth"] = "1px"
        ft = tkFont.Font(family='calibri',size=12)
        entry_pelicula["font"] = ft
        entry_pelicula["fg"] = "#333333"
        entry_pelicula["justify"] = "center"
        entry_pelicula["text"] = ""
        entry_pelicula.place(x=180,y=220,width=170,height=30)

        btn_crear=tk.Button(self)
        btn_crear["bg"] = "#009688"
        ft = tkFont.Font(family='calibri bold',size=12)
        btn_crear["font"] = ft
        btn_crear["fg"] = "#ffffff"
        btn_crear["justify"] = "center"
        btn_crear["text"] = "Crear sala"
        btn_crear["relief"] = "flat"
        btn_crear.place(x=90,y=360,width=189,height=30)
        btn_crear["command"] = self.command_crear

        btn_exit=tk.Button(self)
        btn_exit["bg"] = "#d45858"
        ft = tkFont.Font(family='calibri bold',size=12)
        btn_exit["font"] = ft
        btn_exit["fg"] = "#ffffff"
        btn_exit["justify"] = "center"
        btn_exit["text"] = "Salir"
        btn_exit["relief"] = "flat"
        btn_exit.place(x=90,y=440,width=189,height=30)
        btn_exit["command"] = self.command_exit

    def get_value(self,name):
        return self.nametowidget(name).get()


    def command_crear(self):
        salas = self.get_value("sala")
        total = self.get_value("capacidad")
        peliculas = self.get_value("pelicula")
        dimension = self.get_value("formato")

        if salas == "" or peliculas == "" or dimension == "":
          tkMsgbox.showwarning(self.title(),"Todos los campos deben estar completos!")
        else:
          conexion = sqlite3.connect("cinemark.db")
          cursor = conexion.cursor()
          cursor.execute("""CREATE TABLE IF NOT EXISTS 'SALAS'
                            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            NOMBRE VARCHAR(50),
                            CAPACIDAD VARCHAR(50),
                            PELICULA VARCHAR(50),
                            FORMATO VARCHAR(50))""")

          lista =[(salas,total,peliculas,dimension)]
          cursor.executemany("INSERT INTO SALAS VALUES(NULL,?,?,?,?)",lista)
          conexion.commit()
          conexion.close()

          tkMsgbox.showinfo(self.title(),"Se ha creado una nueva sala!")

    def command_exit(self):
        print("salir")
        self.destroy()
