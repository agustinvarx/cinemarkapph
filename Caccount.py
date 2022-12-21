import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox as tkMsgbox
from tkinter import ttk
import sqlite3
#from command import command_a


class Account(tk.Toplevel):
    def __init__(self,master = None):
        super().__init__(master)
        
        self.master = master
        self.root = master
        #setting title
        self.title("cinemark registro")
        #setting window size
        width=373
        height=580
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
        etiqueta1.place(x=90,y=10,width=201,height=30)

        etiqueta2=tk.Label(self)
        etiqueta2["bg"] = "#009688"
        ft = tkFont.Font(family='calibri bold',size=12)
        etiqueta2["font"] = ft
        etiqueta2["fg"] = "#ffffff"
        etiqueta2["justify"] = "center"
        etiqueta2["text"] = "nombre"
        etiqueta2.place(x=20,y=50,width=129,height=30)

        etiqueta3=tk.Label(self)
        etiqueta3["bg"] = "#009688"
        ft = tkFont.Font(family='calibri bold',size=12)
        etiqueta3["font"] = ft
        etiqueta3["fg"] = "#ffffff"
        etiqueta3["justify"] = "center"
        etiqueta3["text"] = "apellido"
        etiqueta3.place(x=20,y=110,width=130,height=30)

        etiqueta4=tk.Label(self)
        etiqueta4["bg"] = "#009688"
        ft = tkFont.Font(family='calibri bold',size=12)
        etiqueta4["font"] = ft
        etiqueta4["fg"] = "#ffffff"
        etiqueta4["justify"] = "center"
        etiqueta4["text"] = "DNi"
        etiqueta4.place(x=20,y=170,width=129,height=30)

        etiqueta5=tk.Label(self)
        etiqueta5["bg"] = "#009688"
        ft = tkFont.Font(family='calibri bold',size=12)
        etiqueta5["font"] = ft
        etiqueta5["fg"] = "#ffffff"
        etiqueta5["justify"] = "center"
        etiqueta5["text"] = "e-mail"
        etiqueta5.place(x=20,y=230,width=128,height=30)

        etiqueta6=tk.Label(self)
        etiqueta6["bg"] = "#009688"
        ft = tkFont.Font(family='calibri bold',size=12)
        etiqueta6["font"] = ft
        etiqueta6["fg"] = "#ffffff"
        etiqueta6["justify"] = "center"
        etiqueta6["text"] = "usuario"
        etiqueta6.place(x=20,y=290,width=128,height=30)

        etiqueta7=tk.Label(self)
        etiqueta7["bg"] = "#009688"
        ft = tkFont.Font(family='calibri bold',size=12)
        etiqueta7["font"] = ft
        etiqueta7["fg"] = "#ffffff"
        etiqueta7["justify"] = "center"
        etiqueta7["text"] = "contraseña"
        etiqueta7.place(x=20,y=350,width=129,height=30)

        etiqueta8=tk.Label(self)
        etiqueta8["bg"] = "#009688"
        ft = tkFont.Font(family='calibri bold',size=12)
        etiqueta8["font"] = ft
        etiqueta8["fg"] = "#ffffff"
        etiqueta8["justify"] = "center"
        etiqueta8["text"] = "conf. contraseña"
        etiqueta8.place(x=20,y=410,width=132,height=30)

        etiqueta9=tk.Label(self)
        etiqueta9["bg"] = "#009688"
        ft = tkFont.Font(family='calibri bold',size=12)
        etiqueta9["font"] = ft
        etiqueta9["fg"] = "#ffffff"
        etiqueta9["justify"] = "center"
        etiqueta9["text"] = "registrase como"
        etiqueta9.place(x=20,y=470,width=132,height=30)
        
        lista =["cliente","Cinemark Team"]
        roles = ttk.Combobox(self,state="readonly",values=lista,name="roleschoice")
        ft = tkFont.Font(family='calibri',size=12)
        roles["font"] = ft
        roles.place(x = 170,y=470,width=181,height=25)

        entry_nombre=tk.Entry(self,name="name")
        entry_nombre["borderwidth"] = "1px"
        ft = tkFont.Font(family='calibri',size=12)
        entry_nombre["font"] = ft
        entry_nombre["fg"] = "#333333"
        entry_nombre["justify"] = "center"
        entry_nombre["text"] = ""
        entry_nombre.place(x=170,y=50,width=181,height=30)

        entry_apellido=tk.Entry(self,name="lastname")
        entry_apellido["borderwidth"] = "1px"
        ft = tkFont.Font(family='calibri',size=12)
        entry_apellido["font"] = ft
        entry_apellido["fg"] = "#333333"
        entry_apellido["justify"] = "center"
        entry_apellido["text"] = ""
        entry_apellido.place(x=170,y=110,width=179,height=30)

        entry_dni=tk.Entry(self,name="dni")
        entry_dni["borderwidth"] = "1px"
        ft = tkFont.Font(family='calibri',size=12)
        entry_dni["font"] = ft
        entry_dni["fg"] = "#333333"
        entry_dni["justify"] = "center"
        entry_dni["text"] = ""
        entry_dni.place(x=170,y=170,width=182,height=30)

        etry_correo=tk.Entry(self,name="email")
        etry_correo["borderwidth"] = "1px"
        ft = tkFont.Font(family='calibri',size=12)
        etry_correo["font"] = ft
        etry_correo["fg"] = "#333333"
        etry_correo["justify"] = "center"
        etry_correo["text"] = ""
        etry_correo.place(x=170,y=230,width=180,height=30)

        entry_username=tk.Entry(self,name="username")
        entry_username["borderwidth"] = "1px"
        ft = tkFont.Font(family='calibri',size=12)
        entry_username["font"] = ft
        entry_username["fg"] = "#333333"
        entry_username["justify"] = "center"
        entry_username["text"] = ""
        entry_username.place(x=170,y=290,width=181,height=30)

        entry_password=tk.Entry(self,name="password",show="*")
        entry_password["borderwidth"] = "1px"
        ft = tkFont.Font(family='calibri',size=12)
        entry_password["font"] = ft
        entry_password["fg"] = "#333333"
        entry_password["justify"] = "center"
        entry_password["text"] = ""
        entry_password.place(x=170,y=350,width=179,height=30)

        entry_cpasword=tk.Entry(self,name="password2",show="*")
        entry_cpasword["borderwidth"] = "1px"
        ft = tkFont.Font(family='calibri',size=12)
        entry_cpasword["font"] = ft
        entry_cpasword["fg"] = "#333333"
        entry_cpasword["justify"] = "center"
        entry_cpasword["text"] = ""
        entry_cpasword.place(x=170,y=410,width=180,height=30)

        btn_exit=tk.Button(self)
        btn_exit["bg"] = "#d45858"
        ft = tkFont.Font(family='calibri bold',size=12)
        btn_exit["font"] = ft
        btn_exit["fg"] = "#ffffff"
        btn_exit["justify"] = "center"
        btn_exit["relief"] = "flat"
        btn_exit["text"] = "cancelar"
        btn_exit.place(x=20,y=530,width=158,height=30)
        btn_exit["command"] = self.btn_cancelar

        btn_inicio=tk.Button(self)
        btn_inicio["bg"] = "#009688"
        ft = tkFont.Font(family='calibri bold',size=12)
        btn_inicio["font"] = ft
        btn_inicio["fg"] = "#ffffff"
        btn_inicio["justify"] = "center"
        btn_inicio["text"] = "confirmar"
        btn_inicio["relief"] = "flat"
        btn_inicio.place(x=190,y=530,width=161,height=30)
        btn_inicio["command"] = self.btn_confirmar

    def get_value(self,name):
        return self.nametowidget(name).get()

    def btn_confirmar(self):
        nombre = self.get_value("name")
        apellido = self.get_value("lastname")
        dni = self.get_value("dni")
        user = self.get_value("username")
        email = self.get_value("email")
        password=self.get_value("password")
        print(password.isalnum())
        password_Conf = self.get_value("password2")
        roles_get = self.get_value("roleschoice")
        if nombre == None or apellido == "" or dni == "" or user == "" or email == "" or password == "" or password_Conf == "":
            tkMsgbox.showwarning(self.title(),"Todos los campos deben estar completos!")
        elif password != password_Conf:
            tkMsgbox.showerror(self.title(),"Las contraseñas no son iguales!")
        else:
            try:
                if len(password) >= 8:
                    if password == password_Conf and roles_get == "cliente":
                        conexion = sqlite3.connect("cinemark.db")
                        cursor = conexion.cursor()
                        cursor.execute("""CREATE TABLE IF NOt EXISTS 'USUARIOS'
                                        (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                        NOMBRE VARCHAR(50),
                                        APELLIDO VARCHAR(50),
                                        DNI INTEGER,
                                        USERNAME VARCHAR (20) UNIQUE,
                                        EMAIL VARCHAR(50),
                                        PASSWORDS VARCHAR(20),
                                        ROLES VARCHAR(20))""")

                        lista = [(nombre,apellido,dni,user,email,password,roles_get)]
                        cursor.executemany("INSERT INTO USUARIOS VALUES (NULL,?,?,?,?,?,?,?)",lista)
                        conexion.commit()
                        conexion.close()
                        tkMsgbox.showinfo(self.title(),"Registro existoso")
                    
                    else:
                        if password == password_Conf and roles_get == "Cinemark Team":
                            answer = tkMsgbox.askokcancel(self.title(),"Si formas parte del equipo Cinemaek se te habra otorgado una clave unica para acceder a las tareas de administracion. En caso contrario no podras acceder")
                            if answer:
                                conexion = sqlite3.connect("cinemark.db")
                                cursor = conexion.cursor()
                                cursor.execute("""CREATE TABLE IF NOt EXISTS 'USUARIOS'
                                        (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                        NOMBRE VARCHAR(50),
                                        APELLIDO VARCHAR(50),
                                        DNI INTEGER,
                                        USERNAME VARCHAR (20) UNIQUE,
                                        EMAIL VARCHAR(50),
                                        PASSWORDS VARCHAR(20),
                                        ROLES VARCHAR(20))""")

                                lista = [(nombre,apellido,dni,user,email,password,roles_get)]
                                cursor.executemany("INSERT INTO USUARIOS VALUES (NULL,?,?,?,?,?,?,?)",lista)
                                conexion.commit()
                                conexion.close()
                                tkMsgbox.showinfo(self.title(),"Registro existoso!")

                else:
                    tkMsgbox.showwarning(self.title(),"La ncontraseña no debe ser menor a 8 caracteres!")                            
            except sqlite3.IntegrityError:
                tkMsgbox.showerror(self.title(),"Ya existe un usuario con ese alias!")
        
        print("confirmar")


    def btn_cancelar(self):
        self.destroy()
        print("cancelar")