from tkinter import *
from functools import partial
from calculator import Frame_calculadora
import webbrowser as web


class Gui():
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Calculadora v1.2")
        self.janela.geometry("640x480+400+100")
        self.janela["bg"] = "#FFDBAA"
        self.janela.resizable(0, 0)
        self.janela.iconbitmap("icons/cal.ico")
        Label(self.janela, text="   Calculadora v1.2", width=100, height=3, bg="#003A21", font="Arial 18 bold", fg="#fff", anchor='w').pack(fill='x') 
        self.bthelp = Button(self.janela, text="Ajuda", font="Arial 12 bold", width=5, bg="#003A21", fg="#fff", command=self.ajuda)
        self.bthelp.place(x=10, y=440)
        self.init()


    def init(self):
        frame = Frame_calculadora(self.janela)
        frame.init()

    
    def ajuda(self):
        web.open_new("ajuda.html")