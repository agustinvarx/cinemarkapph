import tkinter as tk
import tkinter.font as tkFont
from Eadmin import Adminmenu
import tkinter.messagebox as tkMsgbox
class Acces(tk.Toplevel):
    def __init__(self,master = None):
        super().__init__(master)
        self.master = master
        self.root = master
        #setting title
        self.title("Cinemark")
        #setting window size
        width=374
        height=197
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        eqtiqueta=tk.Label(self)
        eqtiqueta["bg"] = "#f2f2f2"
        ft = tkFont.Font(family='calibri bold',size=14)
        eqtiqueta["font"] = ft
        eqtiqueta["fg"] = "#009688"
        eqtiqueta["justify"] = "center"
        eqtiqueta["text"] = "Cinemark App"
        eqtiqueta.place(x=80,y=10,width=211,height=35)

        eqtiqueta1=tk.Label(self)
        eqtiqueta1["bg"] = "#009688"
        ft = tkFont.Font(family='calibri bold',size=12)
        eqtiqueta1["font"] = ft
        eqtiqueta1["fg"] = "#ffffff"
        eqtiqueta1["justify"] = "center"
        eqtiqueta1["text"] = "clave de acceso"
        eqtiqueta1.place(x=20,y=70,width=120,height=30)

        entry_password=tk.Entry(self,name="clave",show="*")
        entry_password["borderwidth"] = "1px"
        ft = tkFont.Font(family='calibri',size=12)
        entry_password["font"] = ft
        entry_password["fg"] = "#333333"
        entry_password["text"] = ""
        entry_password.place(x=160,y=70,width=191,height=30)

        btn_cancelar=tk.Button(self)
        btn_cancelar["bg"] = "#d45858"
        ft = tkFont.Font(family='calibri bold',size=12)
        btn_cancelar["font"] = ft
        btn_cancelar["fg"] = "#ffffff"
        btn_cancelar["justify"] = "center"
        btn_cancelar["text"] = "cancelar"
        btn_cancelar["relief"] = "flat"
        btn_cancelar.place(x=20,y=140,width=153,height=30)
        btn_cancelar["command"] = self.command_cancelar

        btn_acces=tk.Button(self)
        btn_acces["bg"] = "#009688"
        ft = tkFont.Font(family='calibri bold',size=12)
        btn_acces["font"] = ft
        btn_acces["fg"] = "#ffffff"
        btn_acces["justify"] = "center"
        btn_acces["text"] = "entrar"
        btn_acces["relief"] = "flat"
        btn_acces.place(x=200,y=140,width=152,height=30)
        btn_acces["command"] = self.command_acces

    def get_value(self,name):
        return self.nametowidget(name).get()

    def command_cancelar(self):
        print("cancelar")
        self.destroy()


    def command_acces(self):
        password = "cinemark2022"
        c_password = self.get_value("clave")
        if c_password == password:
            Adminmenu(self.root)
        else:
            tkMsgbox.showerror(self.title(),"Contraseña incorrecta!")
        print("acces")

