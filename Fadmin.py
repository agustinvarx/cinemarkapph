import tkinter as tk
import tkinter.font as tkFont
from Hsalas import salas
from IsetSalas import Set_salas
class adminmenu(tk.Toplevel):
    def __init__(self,master = None):
        super().__init__(master)
        self.root = master
        self.master = master
        #setting title
        self.title("Cinemark")
        #setting window size
        width=373
        height=505
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        etiqueta=tk.Label(self)
        etiqueta["bg"] = "#f2f2f2"
        ft = tkFont.Font(family='calibri bold',size=16)
        etiqueta["font"] = ft
        etiqueta["fg"] = "#009688"
        etiqueta["justify"] = "center"
        etiqueta["text"] = "Cinemark App"
        etiqueta.place(x=80,y=10,width=211,height=35)

        btn_all_resarvas=tk.Button(self)
        btn_all_resarvas["bg"] = "#009688"
        ft = tkFont.Font(family='calibri bold',size=12)
        btn_all_resarvas["font"] = ft
        btn_all_resarvas["fg"] = "#ffffff"
        btn_all_resarvas["justify"] = "center"
        btn_all_resarvas["text"] = "todas las reservas"
        btn_all_resarvas["relief"] = "flat"
        btn_all_resarvas.place(x=90,y=80,width=200,height=30)
        btn_all_resarvas["command"] = self.command_ver_reservas

        btn_reserva=tk.Button(self)
        btn_reserva["bg"] = "#009688"
        ft = tkFont.Font(family='calibri bold',size=12)
        btn_reserva["font"] = ft
        btn_reserva["fg"] = "#ffffff"
        btn_reserva["justify"] = "center"
        btn_reserva["relief"] = "flat"
        btn_reserva["text"] = "Ver reserva particular"
        btn_reserva.place(x=90,y=150,width=200,height=30)
        btn_reserva["command"] = self.command_reserva

        btn_sala=tk.Button(self)
        btn_sala["bg"] = "#009688"
        ft = tkFont.Font(family='calibri bold',size=12)
        btn_sala["font"] = ft
        btn_sala["fg"] = "#ffffff"
        btn_sala["justify"] = "center"
        btn_sala["relief"] = "flat"
        btn_sala["text"] = "Crear sala"
        btn_sala.place(x=90,y=220,width=200,height=30)
        btn_sala["command"] = self.command_sala

        btn_set_sala=tk.Button(self)
        btn_set_sala["bg"] = "#009688"
        ft = tkFont.Font(family='calibri bold',size=12)
        btn_set_sala["font"] = ft
        btn_set_sala["fg"] = "#ffffff"
        btn_set_sala["justify"] = "center"
        btn_set_sala["relief"] = "flat"
        btn_set_sala["text"] = "Modificar sala"
        btn_set_sala.place(x=90,y=290,width=200,height=30)
        btn_set_sala["command"] = self.command_set_sala

        btn_set_descuento=tk.Button(self)
        btn_set_descuento["bg"] = "#009688"
        ft = tkFont.Font(family='calibri bold',size=12)
        btn_set_descuento["font"] = ft
        btn_set_descuento["fg"] = "#ffffff"
        btn_set_descuento["justify"] = "center"
        btn_set_descuento["relief"] = "flat"
        btn_set_descuento["text"] = "Modificar descuentos"
        btn_set_descuento.place(x=90,y=360,width=200,height=30)
        btn_set_descuento["command"] = self.commad_descuentos

        btn_exit=tk.Button(self)
        btn_exit["bg"] = "#d45858"
        ft = tkFont.Font(family='calibri bold',size=12)
        btn_exit["font"] = ft
        btn_exit["fg"] = "#ffffff"
        btn_exit["relief"] = "flat"
        btn_exit["justify"] = "center"
        btn_exit["text"] = "Volver atras"
        btn_exit.place(x=50,y=440,width=270,height=30)
        btn_exit["command"] = self.command_exit

    def command_ver_reservas(self):
        print("ver reservas")


    def command_reserva(self):
        print("reserva")


    def command_sala(self):
        salas(self.root)
        print("sala")


    def command_set_sala(self):
        print("set sala")
        Set_salas(self.root)


    def commad_descuentos(self):
        print("descuentos")


    def command_exit(self):
        self.destroy()
        print("salir")
