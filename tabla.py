import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
from tkinter import ttk
from command import Command_a

class Ventana(tk.Toplevel):
    def __init__(self, master = None):
        super().__init__(master)
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

        btn_close=tk.Button(self)
        btn_close["bg"] = "#d45858"
        ft = tkFont.Font(family='calibri bold',size=12)
        btn_close["font"] = ft
        btn_close["fg"] = "#ffffff"
        btn_close["justify"] = "center"
        btn_close["text"] = "cancelar"
        btn_close["relief"] = "flat"
        btn_close.place(x=200,y=400,width=152,height=30)
        btn_close["command"] = self.obtener_fila


    def obtener_fila(self, event):
        tablas = self.nametowidget("vistatabla")
        current_item = tablas.focus()
        if current_item:
            data = tablas.item(current_item)
            self.select_id = int(data["text"])
        else:
            self.select_id = -1

    def refresh(self):
      tablas = self.nametowidget("vistatabla")
      for iter in tablas.get_children():
        tablas.delete(iter)
      salas = Command_a.lista_sala()
      for iter in salas:
        a = 0
        tablas.insert("",END,text=[0],values=(salas[0][0],salas[1][1],salas[2][2]))
        a += 1


