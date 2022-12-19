import tkinter as tk
import tkinter.font as tkFont


class usermenu(tk.Toplevel):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.root = master
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
        ft = tkFont.Font(family='calibri bold',size=14)
        etiqueta["font"] = ft
        etiqueta["fg"] = "#333333"
        etiqueta["justify"] = "center"
        etiqueta["text"] = "Cinemark App"
        etiqueta.place(x=80,y=10,width=211,height=35)

        btn_salas=tk.Button(self)
        btn_salas["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='calibri bold',size=12)
        btn_salas["font"] = ft
        btn_salas["fg"] = "#000000"
        btn_salas["justify"] = "center"
        btn_salas["text"] = "Salas"
        btn_salas.place(x=90,y=80,width=200,height=30)
        btn_salas["command"] = self.command_salas

        btn_reservas=tk.Button(self)
        btn_reservas["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='calibri bold',size=12)
        btn_reservas["font"] = ft
        btn_reservas["fg"] = "#000000"
        btn_reservas["justify"] = "center"
        btn_reservas["text"] = "Realizar reserva"
        btn_reservas.place(x=90,y=150,width=200,height=30)
        btn_reservas["command"] = self.command_reservas

        btn_mod_reserva=tk.Button(self)
        btn_mod_reserva["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='calibri bold',size=12)
        btn_mod_reserva["font"] = ft
        btn_mod_reserva["fg"] = "#000000"
        btn_mod_reserva["justify"] = "center"
        btn_mod_reserva["text"] = "Modificar reserva"
        btn_mod_reserva.place(x=90,y=220,width=200,height=30)
        btn_mod_reserva["command"] = self.command_modificar

        btn_reservas_total=tk.Button(self)
        btn_reservas_total["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='calibri bold',size=12)
        btn_reservas_total["font"] = ft
        btn_reservas_total["fg"] = "#000000"
        btn_reservas_total["justify"] = "center"
        btn_reservas_total["text"] = "Ver mis reservas"
        btn_reservas_total.place(x=90,y=290,width=200,height=30)
        btn_reservas_total["command"] = self.command_mostrar

        btn_historial=tk.Button(self)
        btn_historial["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='calibri bold',size=12)
        btn_historial["font"] = ft
        btn_historial["fg"] = "#000000"
        btn_historial["justify"] = "center"
        btn_historial["text"] = "Ver mis historicos"
        btn_historial.place(x=90,y=360,width=199,height=30)
        btn_historial["command"] = self.command_historial

        btn_exit=tk.Button(self)
        btn_exit["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='calibri bold',size=12)
        btn_exit["font"] = ft
        btn_exit["fg"] = "#000000"
        btn_exit["justify"] = "center"
        btn_exit["text"] = "Volver atras"
        btn_exit.place(x=50,y=440,width=270,height=30)
        btn_exit["command"] = self.command_exit

    def command_salas(self):
        print("salas")


    def command_reservas(self):
        print("reservas")


    def command_modificar(self):
        print("modificar")


    def command_mostrar(self):
        print("ver reservas")


    def command_historial(self):
        print("historial")


    def command_exit(self):
        self.destroy()
        print("salir")
      
