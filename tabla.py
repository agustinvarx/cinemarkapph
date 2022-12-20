import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
from tkinter import ttk
from command import Command_a
import sqlite3
import tkinter.messagebox as tkMsgbox
from HsetSalas import Set_salas

class Ventana(tk.Toplevel):
    def __init__(self, master = None):
        super().__init__(master)
        self.root = master
        self.master= master
        #setting title
        self.title("undefined")
        #setting window size
        width=754
        height=448
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        vista = ttk.Treeview(self,columns=("nombre","capacidad","pelicula","formato"),name="vistatabla")
        vista.column("#0",width=100)
        vista.column("nombre",width=100,anchor="center")
        vista.column("capacidad",width=100,anchor="center")
        vista.column("pelicula",width=100,anchor="center")
        vista.column("formato",width=100,anchor="center")
        vista.heading("#0",text="ID",anchor="center")
        vista.heading("nombre",text="Sala",anchor="center")
        vista.heading("capacidad",text="Capacidad",anchor="center")
        vista.heading("pelicula",text="Pelicula",anchor="center")
        vista.heading("formato",text="Formato",anchor="center")
        vista.bind("<<TreeviewSelect>>",self.obtener_fila)
        vista.place(x=20,y=20,width=710,height=325)
        self.refresh()

        btn_editar=tk.Button(self)
        btn_editar["bg"] = "#d45858"
        ft = tkFont.Font(family='calibri bold',size=12)
        btn_editar["font"] = ft
        btn_editar["fg"] = "#ffffff"
        btn_editar["justify"] = "center"
        btn_editar["text"] = "Eliminar sala"
        btn_editar["relief"] = "flat"
        btn_editar.place(x=440,y=400,width=139,height=30)
        btn_editar["command"] = self.command_update


        btn_delete=tk.Button(self)
        btn_delete["bg"] = "#d45858"
        ft = tkFont.Font(family='calibri bold',size=12)
        btn_delete["font"] = ft
        btn_delete["fg"] = "#ffffff"
        btn_delete["justify"] = "center"
        btn_delete["text"] = "Eliminar sala"
        btn_delete["relief"] = "flat"
        btn_delete.place(x=600,y=400,width=139,height=30)
        btn_delete["command"] = self.obtener_fila

    def command_update(self):
      Set_salas(self.root)


    def obtener_fila(self, event):
        tablas = self.nametowidget("vistatabla")
        current_item = tablas.focus()
        if current_item:
            data = tablas.item(current_item)
            self.select_id = int(data["text"])
        else:
            self.select_id = -1
  
        sala = self.get_value("sala")

        conexion = sqlite3.connect("cinemark.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM SALAS NOMBRE")
        datos = cursor.fetchall() 
        conexion.commit()
        conexion.close()
        for iter in datos:
            if iter[1] == sala:
                lista_set = [sala]
                conexion = sqlite3.connect("cinemark.db")
                cursor = conexion.cursor()
                cursor.execute("DELETE FROM SALAS WHERE NOMBRE = (?)",lista_set)
                conexion.commit()
                conexion.close()
                tkMsgbox.showwarning(self.title,"Se elimino una sala!")
        print("eliminar")

    def refresh(self):
      tablas = self.nametowidget("vistatabla")
      for iter in tablas.get_children():
        tablas.delete(iter)
      salas = Command_a.lista_sala()
      for iter in salas:
        print(iter[0],type(iter))
        tablas.insert("",END,text=iter[0],values=(iter[1],iter[2],iter[3],iter[4]))

