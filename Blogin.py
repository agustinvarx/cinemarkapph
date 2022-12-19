import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox as tkMsgbox
from tkinter import ttk
from Caccount import Account
from DuserMenu import Usermenu
from FcheckAcces import Acces
from command import Command_a

class Login(tk.Toplevel):
    def __init__(self,master = None):
        super().__init__(master)
        #setting title
        self.master = master
        self.root = master
        #self.root = root
        self.title("cinamerk")
        #setting window size
        width=373
        height=440
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
        etiqueta1.place(x=80,y=10,width=211,height=35)

        etiqueta2=tk.Label(self)
        etiqueta2["bg"] = "#009688"
        ft = tkFont.Font(family='calibri bold',size=12)
        etiqueta2["font"] = ft
        etiqueta2["fg"] = "#ffffff"
        etiqueta2["justify"] = "center"
        etiqueta2["text"] = "usuario"
        etiqueta2.place(x=30,y=90,width=125,height=30)

        etiqueta3=tk.Label(self)
        etiqueta3["bg"] = "#009688"
        ft = tkFont.Font(family='calibri bold',size=12)
        etiqueta3["font"] = ft
        etiqueta3["fg"] = "#ffffff"
        etiqueta3["justify"] = "center"
        etiqueta3["text"] = "password"
        etiqueta3.place(x=30,y=160,width=121,height=30)

        entry_username=tk.Entry(self,name="user")
        entry_username["borderwidth"] = "1px"
        ft = tkFont.Font(family='calibri ',size=12)
        entry_username["font"] = ft
        entry_username["fg"] = "#333333"
        entry_username["justify"] = "center"
        entry_username["text"] = ""
        entry_username.place(x=180,y=90,width=160,height=30)

        entry_password=tk.Entry(self,name="password",show="*")
        entry_password["borderwidth"] = "1px"
        ft = tkFont.Font(family='calibri',size=12)
        entry_password["font"] = ft
        entry_password["fg"] = "#333333"
        entry_password["justify"] = "center"
        entry_password["text"] = ""
        entry_password.place(x=180,y=160,width=160,height=30)

        btn_inicio=tk.Button(self)
        btn_inicio["bg"] = "#009688"
        ft = tkFont.Font(family='calibri bold',size=12)
        btn_inicio["font"] = ft
        btn_inicio["fg"] = "#ffffff"
        btn_inicio["justify"] = "center"
        btn_inicio["text"] = "iniciar sesion"
        btn_inicio.place(x=90,y=240,width=180,height=30)
        btn_inicio["relief"] = "flat"
        btn_inicio["command"] = self.command_login

        etiqueta5=tk.Label(self)
        etiqueta5["bg"] = "#f2f2f2"
        ft = tkFont.Font(family='calibri',size=14)
        etiqueta5["font"] = ft
        etiqueta5["fg"] = "#009688"
        etiqueta5["justify"] = "center"
        etiqueta5["text"] = "No tienes cuenta? Registrate aqui!"
        etiqueta5.place(x=20,y=320,width=330,height=34)

        btn_registro=tk.Button(self)
        btn_registro["bg"] = "#009688"
        ft = tkFont.Font(family='calibri bold',size=12)
        btn_registro["font"] = ft
        btn_registro["fg"] = "#ffffff"
        btn_registro["justify"] = "center"
        btn_registro["text"] = "registrarse"
        btn_registro["relief"] = "flat"
        btn_registro.place(x=20,y=380,width=152,height=30)
        btn_registro["command"] = self.command_inicio

        btn_cancelar=tk.Button(self)
        btn_cancelar["bg"] = "#d45858"
        ft = tkFont.Font(family='calibri bold',size=12)
        btn_cancelar["font"] = ft
        btn_cancelar["fg"] = "#ffffff"
        btn_cancelar["text"] = "cancelar"
        btn_cancelar["relief"] = "flat"
        btn_cancelar.place(x=200,y=380,width=150,height=30)
        btn_cancelar["command"] = self.command_salir

    def get_value(self,name):
        return self.nametowidget(name).get()

    def command_login(self):
      username = self.get_value("user")
      password = self.get_value("password")
      open = Command_a.command_iniciarsesion(username,password)
      print(open,"test")
      if open == "cliente":
        Usermenu(self.root)
      elif open == "Cinemark Team":
        Acces(self.root)
      else:
        tkMsgbox.showerror(self.title(),"El usuario o contraseña son incorrectos!")

    def command_inicio(self):
      Account(self.root)


    def command_salir(self):
        self.destroy()
        print("salir")