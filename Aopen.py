import tkinter as tk
import tkinter.font as tkFont
from Blogin import Login


class App:
    def __init__(self, root, title):
        self.root = root
        #setting title
        root.title(title)
        #setting window size
        width=373
        height=130
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.iconbitmap(default="zcinemark.ico")

        etiqueta=tk.Label(root)
        etiqueta["bg"] = "#f2f2f2"
        ft = tkFont.Font(family='calibri bold',size=16)
        etiqueta["font"] = ft
        etiqueta["fg"] = "#009688"
        etiqueta["justify"] = "center"
        etiqueta["text"] = "Cinemark App"
        etiqueta["relief"] = "flat"
        etiqueta.place(x=80,y=10,width=201,height=30)

        btn_open=tk.Button(root)
        btn_open["bg"] = "#009688"
        ft = tkFont.Font(family='calibri bold',size=12)
        btn_open["font"] = ft
        btn_open["fg"] = "#ffffff"
        btn_open["justify"] = "center"
        btn_open["text"] = "iniciar"
        btn_open["relief"] = "flat"
        btn_open.place(x=20,y=80,width=157,height=30)
        btn_open["command"] = self.open_app

        btn_close=tk.Button(root)
        btn_close["bg"] = "#d45858"
        ft = tkFont.Font(family='Times',size=10)
        btn_close["font"] = ("calibri",12,"bold")
        btn_close["fg"] = "#ffffff"
        btn_close["justify"] = "center"
        btn_close["text"] = "cancelar"
        btn_close["relief"] = "flat"
        btn_close.place(x=200,y=80,width=152,height=30)
        btn_close["command"] = self.close_app

    def open_app(self):
        Login(self.root)


    def close_app(self):
        print("close")
        root.destroy()

if __name__ == "__main__":
    project = "cinemark"
    root = tk.Tk()
    app = App(root, project.capitalize())
    root.mainloop()