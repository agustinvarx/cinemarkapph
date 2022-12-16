import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox as tkMsgbox
from tkinter import ttk
from Caccount import account
from DuserMenu import usermenu
from FcheckUser import Acces

class login(tk.Toplevel):
    def __init__(self,root,master = None):
        super().__init__(master)
        #setting title
        self.master = master
        self.root = root
        #self.root = root
        self.title("cinamerk")
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
        ft = tkFont.Font(family='calibri bold',size=14)
        etiqueta1["font"] = ft
        etiqueta1["fg"] = "#333333"
        etiqueta1["justify"] = "center"
        etiqueta1["text"] = "Cinemark App"
        etiqueta1.place(x=80,y=10,width=211,height=35)

        etiqueta2=tk.Label(self)
        etiqueta2["bg"] = "#f2f2f2"
        ft = tkFont.Font(family='calibri bold',size=12)
        etiqueta2["font"] = ft
        etiqueta2["fg"] = "#333333"
        etiqueta2["justify"] = "center"
        etiqueta2["text"] = "usuario"
        etiqueta2.place(x=30,y=90,width=125,height=30)

        etiqueta3=tk.Label(self)
        etiqueta3["bg"] = "#f2f2f2"
        ft = tkFont.Font(family='calibri bold',size=12)
        etiqueta3["font"] = ft
        etiqueta3["fg"] = "#333333"
        etiqueta3["justify"] = "center"
        etiqueta3["text"] = "password"
        etiqueta3.place(x=30,y=160,width=121,height=30)

        etiqueta4=tk.Label(self)
        etiqueta4["bg"] = "#f2f2f2"
        ft = tkFont.Font(family='calibri bold',size=12)
        etiqueta4["font"] = ft
        etiqueta4["fg"] = "#333333"
        etiqueta4["justify"] = "center"
        etiqueta4["text"] = "roles"
        etiqueta4.place(x=40,y=220,width=70,height=25)

        lista =["cliente","Cinemark Team"]
        roles = ttk.Combobox(self,state="readonly",values=lista,name="rolesc")
        roles.place(x = 55,y=250)

        entry_username=tk.Entry(self,name="user")
        entry_username["borderwidth"] = "1px"
        ft = tkFont.Font(family='calibri ',size=12)
        entry_username["font"] = ft
        entry_username["fg"] = "#333333"
        entry_username["justify"] = "center"
        entry_username["text"] = ""
        entry_username.place(x=180,y=90,width=160,height=30)

        entry_password=tk.Entry(self,name="password")
        entry_password["borderwidth"] = "1px"
        ft = tkFont.Font(family='calibri',size=12)
        entry_password["font"] = ft
        entry_password["fg"] = "#333333"
        entry_password["justify"] = "center"
        entry_password["text"] = ""
        entry_password.place(x=180,y=160,width=160,height=30)

        btn_inicio=tk.Button(self)
        btn_inicio["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='calibri bold',size=12)
        btn_inicio["font"] = ft
        btn_inicio["fg"] = "#000000"
        btn_inicio["justify"] = "center"
        btn_inicio["text"] = "iniciar sesion"
        btn_inicio.place(x=90,y=300,width=180,height=30)
        btn_inicio["command"] = self.command_iniciarsesion

        etiqueta5=tk.Label(self)
        etiqueta5["bg"] = "#009688"
        ft = tkFont.Font(family='calibri ',size=12)
        etiqueta5["font"] = ft
        etiqueta5["fg"] = "#ffffff"
        etiqueta5["justify"] = "center"
        etiqueta5["text"] = "No titnes cuenta? Registrate aqui!"
        etiqueta5.place(x=20,y=370,width=330,height=34)

        btn_registro=tk.Button(self)
        btn_registro["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='calibri bold',size=12)
        btn_registro["font"] = ft
        btn_registro["fg"] = "#000000"
        btn_registro["justify"] = "center"
        btn_registro["text"] = "registrarse"
        btn_registro.place(x=20,y=440,width=152,height=30)
        btn_registro["command"] = self.command_inicio

        btn_cancelar=tk.Button(self)
        btn_cancelar["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='calibri bold',size=12)
        btn_cancelar["font"] = ft
        btn_cancelar["fg"] = "#000000"
        btn_cancelar["text"] = "cancelar"
        btn_cancelar.place(x=200,y=440,width=150,height=30)
        btn_cancelar["command"] = self.command_salir

    def get_value(self,name):
        return self.nametowidget(name).get()

    def command_iniciarsesion(self):

      self.command()
      roles_test = self.get_value("rolesc")
      if roles_test == "cliente":
        usermenu(self.root)
      elif roles_test == "Cinemark Team":
        Acces(self.root)
      else:
        tkMsgbox.showinfo(self.title(),"debses seleccionar un rol")


    def command_inicio(self):
      account(self.root)


    def command_salir(self):
        self.destroy()
        print("salir")
