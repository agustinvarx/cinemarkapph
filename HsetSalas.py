import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox as tkMsgbox
from tkinter import ttk
from command import Command_a
import sqlite3
import tkinter as tk
import tkinter.font as tkFont

lista =[]

class Set_salas(tk.Toplevel):
    def __init__(self,master = None):
        super().__init__(master)
        self.master = master
        #setting title
        self.title("undefined")
        #setting window size
        width=371
        height=505
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        etiqueta1=tk.Label(self)
        etiqueta1["bg"] = "#eaeaea"
        ft = tkFont.Font(family='calibri bold',size=16)
        etiqueta1["font"] = ft
        etiqueta1["fg"] = "#009688"
        etiqueta1["justify"] = "center"
        etiqueta1["text"] = "Cinemark App"
        etiqueta1.place(x=70,y=10,width=201,height=30)

        etiqueta2=tk.Label(self)
        etiqueta2["bg"] = "#009688"
        ft = tkFont.Font(family='calibri bold',size=12)
        etiqueta2["font"] = ft
        etiqueta2["fg"] = "#ffffff"
        etiqueta2["justify"] = "center"
        etiqueta2["text"] = "seleccionar sala"
        etiqueta2.place(x=20,y=70,width=149,height=30)

        etiqueta3=tk.Label(self)
        etiqueta3["bg"] = "#009688"
        ft = tkFont.Font(family='calibri bold',size=12)
        etiqueta3["font"] = ft
        etiqueta3["fg"] = "#ffffff"
        etiqueta3["justify"] = "center"
        etiqueta3["text"] = "Editar nombre"
        etiqueta3.place(x=20,y=130,width=150,height=31)

        etiqueta4=tk.Label(self)
        etiqueta4["bg"] = "#009688"
        ft = tkFont.Font(family='calibri bold',size=12)
        etiqueta4["font"] = ft
        etiqueta4["fg"] = "#ffffff"
        etiqueta4["justify"] = "center"
        etiqueta4["text"] = "Editar capacidad"
        etiqueta4.place(x=20,y=190,width=149,height=30)

        etiqueta5=tk.Label(self)
        etiqueta5["bg"] = "#009688"
        ft = tkFont.Font(family='calibri bold',size=12)
        etiqueta5["font"] = ft
        etiqueta5["fg"] = "#ffffff"
        etiqueta5["justify"] = "center"
        etiqueta5["text"] = "Editar pelicula"
        etiqueta5.place(x=20,y=250,width=148,height=30)

        etiqueta6=tk.Label(self)
        etiqueta6["bg"] = "#009688"
        ft = tkFont.Font(family='calibri bold',size=12)
        etiqueta6["font"] = ft
        etiqueta6["fg"] = "#ffffff"
        etiqueta6["justify"] = "center"
        etiqueta6["text"] = "Editar formato"
        etiqueta6.place(x=20,y=310,width=149,height=30)

        salas = ttk.Combobox(self,state="readonly",values=lista,name="sala")
        ft = tkFont.Font(family='calibri',size=12)
        salas["font"] = ft
        salas.place(x = 190,y=70,width=160,height=25)

        lista_f =["2D","3D"]
        fromato = ttk.Combobox(self,state="readonly",values=lista_f,name="formato")
        ft = tkFont.Font(family='calibri',size=12)
        fromato["font"] = ft
        fromato.place(x = 190,y=310,width=160,height=25)

        entry_nombre=tk.Entry(self,name="nombre")
        entry_nombre["borderwidth"] = "1px"
        ft = tkFont.Font(family='calibri',size=12)
        entry_nombre["font"] = ft
        entry_nombre["fg"] = "#333333"
        entry_nombre["justify"] = "center"
        entry_nombre["text"] = ""
        entry_nombre.place(x=190,y=130,width=160,height=30)

        entry_capacidad=tk.Entry(self,name="total")
        entry_capacidad["borderwidth"] = "1px"
        ft = tkFont.Font(family='calibri',size=12)
        entry_capacidad["font"] = ft
        entry_capacidad["fg"] = "#333333"
        entry_capacidad["justify"] = "center"
        entry_capacidad["text"] = ""
        entry_capacidad.place(x=190,y=190,width=158,height=30)

        entry_pelicula=tk.Entry(self,name="pelicula")
        entry_pelicula["borderwidth"] = "1px"
        ft = tkFont.Font(family='calibri',size=12)
        entry_pelicula["font"] = ft
        entry_pelicula["fg"] = "#333333"
        entry_pelicula["justify"] = "center"
        entry_pelicula["text"] = ""
        entry_pelicula.place(x=190,y=250,width=160,height=30)

        btn_update=tk.Button(self)
        btn_update["bg"] = "#577baa"
        ft = tkFont.Font(family='calibri bold',size=12)
        btn_update["font"] = ft
        btn_update["fg"] = "#ffffff"
        btn_update["justify"] = "center"
        btn_update["text"] = "Actualizar Sala"
        btn_update["relief"] = "flat"
        btn_update.place(x=20,y=380,width=150,height=30)
        btn_update["command"] = self.command_update

        btn_delete=tk.Button(self)
        btn_delete["bg"] = "#577baa"
        ft = tkFont.Font(family='calibri bold',size=12)
        btn_delete["font"] = ft
        btn_delete["fg"] = "#ffffff"
        btn_delete["justify"] = "center"
        btn_delete["text"] = "Eliminar Sala"
        btn_delete["relief"] = "flat"
        btn_delete.place(x=200,y=380,width=150,height=30)
        btn_delete["command"] = self.command_delete

        btn_exit=tk.Button(self)
        btn_exit["bg"] = "#d45858"
        ft = tkFont.Font(family='calibri bold',size=12)
        btn_exit["font"] = ft
        btn_exit["fg"] = "#ffffff"
        btn_exit["justify"] = "center"
        btn_exit["text"] = "Salir"
        btn_exit["relief"] = "flat"
        btn_exit.place(x=100,y=450,width=161,height=30)
        btn_exit["command"] = self.command_exite

    def get_value(self,name):
        return self.nametowidget(name).get()

    def command_update(self):
        sala = self.get_value("sala")
        nombre = self.get_value("nombre")
        capacidad = self.get_value("total")
        formato = self.get_value("formato")
        pelicula = self.get_value("pelicula")

        conexion = sqlite3.connect("CinemarkSalas.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM SALAS NOMBRE")
        datos = cursor.fetchall()
        conexion.commit()
        conexion.close()

        for iter in datos:
            if iter[1] == sala:
                if nombre != "":
                    lista_set = [nombre,sala]
                    conexion = sqlite3.connect("CinemarkSalas.db")
                    cursor = conexion.cursor()
                    cursor.execute("UPDATE SALAS SET NOMBRE = (?) WHERE NOMBRE =(?)",lista_set)
                    conexion.commit()
                    conexion.close()
                    #pass
                if capacidad != "":
                    set_lista= [capacidad,nombre]
                    conexion = sqlite3.connect("CinemarkSalas.db")
                    cursor = conexion.cursor()
                    cursor.execute("UPDATE SALAS SET CAPACIDAD = (?) WHERE NOMBRE =(?)",set_lista)
                    conexion.commit()
                    conexion.close()
                if pelicula != "":
                    set_lista= [pelicula,nombre]
                    conexion = sqlite3.connect("CinemarkSalas.db")
                    cursor = conexion.cursor()
                    cursor.execute("UPDATE SALAS SET PELICULA = (?) WHERE NOMBRE =(?)",set_lista)
                    conexion.commit()
                    conexion.close()
                if pelicula != "":
                    set_format= [formato,nombre]
                    conexion = sqlite3.connect("CinemarkSalas.db")
                    cursor = conexion.cursor()
                    cursor.execute("UPDATE SALAS SET FORMATO = (?) WHERE NOMBRE =(?)",set_format)
                    conexion.commit()
                    conexion.close()
                    tkMsgbox.showinfo(self.title,"Se actualizo una sala!")
                else:
                    pass


    def command_delete(self):

        sala = self.get_value("sala")

        conexion = sqlite3.connect("CinemarkSalas.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM SALAS NOMBRE")
        datos = cursor.fetchall() 
        conexion.commit()
        conexion.close()
        for iter in datos:
            if iter[1] == sala:
                lista_set = [sala]
                conexion = sqlite3.connect("CinemarkSalas.db")
                cursor = conexion.cursor()
                cursor.execute("DELETE FROM SALAS WHERE NOMBRE = (?)",lista_set)
                conexion.commit()
                conexion.close()
                tkMsgbox.showwarning(self.title,"Se elimino una sala!")
        print("eliminar")


    def command_exite(self):
        self.destroy()
