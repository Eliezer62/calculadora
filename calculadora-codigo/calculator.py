from tkinter import *
from functools import partial
from math import *
import numpy as ny

class Frame_calculadora():
    def __init__(self, root):
        self.janela = root
        self.vis = ''
        self.Ans = ""
        self.radiano = False

    
    def init(self):
        self.visual()
        self.botoes_manipuladores()
        self.botoes_numericos()
        self.botoes_funcoes()
        self.mode()

    def visual(self):
        self.frame_calculadora = Frame(self.janela, bg="#FFDBAA", width=640, height=300) 
        self.frame_calculadora.place(x=0, y=93)
        self.visor = Label(self.frame_calculadora, text=self.vis, font='Arial 12', width=55, height=4, anchor='e')  
        self.visor.place(x=6, y=7)


    def manipuladores(self, botao):
        if botao == 'del':
            if len(self.vis) > 0:
                visor = list(self.vis)
                visor[(len(visor)-1)] = ''
                self.vis = str(''.join(visor))
        elif botao == 'ac':
            self.vis = ''
        elif botao == 'M+':
            self.memory = open('memory.txt', 'w+')
            self.memory.write(self.vis)
            self.memory.close()
        elif botao == 'M-':
            self.memory = open('memory.txt', 'w+')
            self.memory.write('')
            self.memory.close()
        elif botao == ".":
            self.vis += "."
        elif botao == "Ans":
            self.vis += str(self.Ans)
        self.visor["text"] = self.vis
        

    def botoes_manipuladores(self):
        self.btDel = Button(self.frame_calculadora, width=4, height=1, text="DEL", font="Arial 12 bold", bg="#499272", fg="#fff")
        self.btDel["command"] = partial(self.manipuladores, botao='del')
        self.btDel.place(x=520, y=7)
        self.btAc = Button(self.frame_calculadora, width=4, height=1, text="AC", font="Arial 12 bold", bg="#499272", fg="#fff")
        self.btAc["command"] = partial(self.manipuladores, botao='ac')
        self.btAc.place(x=580, y=7)
        self.M = Button(self.frame_calculadora, width=4, height=1, text="M+", font="Arial 12 bold", bg="#499272", fg="#fff")
        self.M["command"] = partial(self.manipuladores, botao='M+')
        self.M.place(x=520, y=50)
        self.m = Button(self.frame_calculadora, width=4, height=1, text="M-", font="Arial 12 bold", bg='#499272', fg='#fff')
        self.m["command"] = partial(self.manipuladores, botao="M-")
        self.m.place(x=580, y=50)


    def numeros(self, botao):
        self.vis += str(botao)
        self.visor["text"] = self.vis


    def botoes_numericos(self):
        self.bt9 = Button(self.frame_calculadora, width=5, height=1, text=9, font='Arial 12 bold', bg="#75AF96", fg='#fff')
        self.bt9["command"] = partial(self.numeros, botao=9)
        self.bt9.place(x=153, y=100)
        self.bt8 = Button(self.frame_calculadora, text=8, width=5, height=1, font="Arial 12 bold", fg = "#fff", bg='#75AF96')
        self.bt8["command"] = partial(self.numeros, 8)
        self.bt8.place(x=85, y=100)
        self.bt7 = Button(self.frame_calculadora, text=7, width=5, height=1, font="Arial 12 bold", bg="#75AF96", fg="#fff")
        self.bt7["command"] = partial(self.numeros, 7)
        self.bt7.place(x=17, y=100)
        self.bt6 = Button(self.frame_calculadora, text=6, width=5, height=1, font="Arial 12 bold", bg="#75AF96", fg="#fff")
        self.bt6["command"] = partial(self.numeros, 6)
        self.bt6.place(x=153, y=140)
        self.bt5 = Button(self.frame_calculadora, text=5, width=5, height=1, font="Arial 12 bold", bg="#75AF96", fg="#fff")
        self.bt5["command"] = partial(self.numeros, 5)
        self.bt5.place(x=85, y=140)
        self.bt4 = Button(self.frame_calculadora, text=4, width=5, height=1, font="Arial 12 bold", bg="#75AF96", fg="#fff")
        self.bt4["command"] = partial(self.numeros, 4)
        self.bt4.place(x=17, y=140)
        self.bt3 = Button(self.frame_calculadora, text=3, width=5, height=1, font="Arial 12 bold", bg="#75AF96", fg="#fff")
        self.bt3["command"] = partial(self.numeros, 3)
        self.bt3.place(x=153, y=180)
        self.bt2 = Button(self.frame_calculadora, text=2, width=5, height=1, font="Arial 12 bold", bg="#75AF96", fg="#fff")
        self.bt2["command"] = partial(self.numeros, 2)
        self.bt2.place(x=85, y=180)
        self.bt1 = Button(self.frame_calculadora, text=1, width=5, height=1, font="Arial 12 bold", bg="#75AF96", fg="#fff")
        self.bt1["command"] = partial(self.numeros, 1)
        self.bt1.place(x=17, y=180)
        self.bt0 = Button(self.frame_calculadora, text=0, width=5, height=1, font='Arial 12 bold', bg='#75AF96', fg="#fff")
        self.bt0["command"] = partial(self.numeros, 0)
        self.bt0.place(x=85, y=220)
        self.btfloat = Button(self.frame_calculadora, text='.', width=5, height=1, font='Arial 12 bold', bg='#75AF96', fg="#fff")
        self.btfloat["command"] = partial(self.manipuladores, botao='.')
        self.btfloat.place(x=17, y=220)
        self.btAns = Button(self.frame_calculadora, text="Ans", width=5, height=1, font='Arial 12 bold', bg='#75AF96', fg="#fff")
        self.btAns["command"] = partial(self.manipuladores, botao="Ans")
        self.btAns.place(x=153, y=220)
        

    def funcoes(self, botao):
        nothing = "Função indisponível"
        if botao == 'igual':
            if len(self.vis)>0:
                self.vis = str(eval(self.vis))
                self.Ans = str(self.vis)
        elif botao == "M":
            self.memory = open("memory.txt", "r+")
            self.vis += self.memory.read()
            self.memory.close()
        else:
            self.vis += botao
        self.visor["text"] = self.vis


    def botoes_funcoes(self):
        self.btSoma = Button(self.frame_calculadora, text="+", width=2, height=1, font="Arial 26 bold", fg="#fff", bg="#499272")
        self.btSoma["command"] = partial(self.funcoes, "+")
        self.btSoma.place(x=250, y=180)
        self.btIgual = Button(self.frame_calculadora, width=5, height=1, font='Arial 12 bold', fg="#fff", bg="#499272", text="=")
        self.btIgual["command"] = partial(self.funcoes, "igual")
        self.btIgual.place(x=318, y=220)
        self.btMulti = Button(self.frame_calculadora, width=5, height=1, font='Arial 12 bold', fg="#fff", bg="#499272", text="x")
        self.btMulti["command"] = partial(self.funcoes, "*")
        self.btMulti.place(x=250, y=140)
        self.btPor = Button(self.frame_calculadora, width=5, height=1, font='Arial 12 bold', fg="#fff", bg="#499272", text="%")
        self.btPor["command"] = partial(self.funcoes, "/100*")
        self.btPor.place(x=250, y=100)
        self.btRaiz = Button(self.frame_calculadora, width=5, height=1, font='Arial 12 bold', fg="#fff", bg="#499272", text="√¯")
        self.btRaiz["command"] = partial(self.funcoes, "sqrt(")
        self.btRaiz.place(x=318, y=100)
        self.btDiv = Button(self.frame_calculadora, width=5, height=1, font='Arial 12 bold', fg="#fff", bg="#499272", text="/")
        self.btDiv["command"] = partial(self.funcoes, "/")
        self.btDiv.place(x=318, y=140)
        self.btSub = Button(self.frame_calculadora, width=5, height=1, font='Arial 12 bold', fg="#fff", bg="#499272", text="-")
        self.btSub["command"] = partial(self.funcoes, "-")
        self.btSub.place(x=318, y=180)
        self.btPleft = Button(self.frame_calculadora, width=5, height=1, font='Arial 12 bold', fg="#fff", bg="#499272", text="(")
        self.btPleft["command"] = partial(self.funcoes, "(")
        self.btPleft.place(x=386, y=100)
        self.btPright = Button(self.frame_calculadora, width=5, height=1, font='Arial 12 bold', fg="#fff", bg="#499272", text=")")
        self.btPright["command"] = partial(self.funcoes, ")")
        self.btPright.place(x=454, y=100)
        self.btFac = Button(self.frame_calculadora, width=5, height=1, font='Arial 12 bold', fg="#fff", bg="#499272", text="x!")
        self.btFac["command"] = partial(self.funcoes, "factorial(")
        self.btFac.place(x=386, y=140)
        self.btLog = Button(self.frame_calculadora, width=5, height=1, font='Arial 12 bold', fg="#fff", bg="#499272", text="Log")
        self.btLog["command"] = partial(self.funcoes, "log(")
        self.btLog.place(x=386, y=180)
        self.btPot = Button(self.frame_calculadora, width=5, height=1, font='Arial 12 bold', fg="#fff", bg="#499272", text="^")
        self.btPot["command"] = partial(self.funcoes, "pow(")
        self.btPot.place(x=386, y=220)
        self.btVir = Button(self.frame_calculadora, width=5, height=1, font='Arial 12 bold', fg="#fff", bg="#499272", text=",")
        self.btVir["command"] = partial(self.funcoes, ",")
        self.btVir.place(x=454, y=140)
        self.btEmpty2 = Button(self.frame_calculadora, width=5, height=1, font='Arial 12 bold', fg="#fff", bg="#499272", text="Empty")
        self.btEmpty2["command"] = partial(self.funcoes, "nothing")
        self.btEmpty2.place(x=454, y=180)
        self.btEmpty3 = Button(self.frame_calculadora, width=5, height=1, font='Arial 12 bold', fg="#fff", bg="#499272", text="Empty")
        self.btEmpty3["command"] = partial(self.funcoes, "nothing")
        self.btEmpty3.place(x=454, y=220)
        self.btMemoria = Button(self.frame_calculadora, width=5, height=1, font='Arial 12 bold', fg="#fff", bg="#805215", text="M")
        self.btMemoria["command"] = partial(self.funcoes, "M")
        self.btMemoria.place(x=522, y=100)
        self.btEmpty5 = Button(self.frame_calculadora, width=5, height=1, font='Arial 12 bold', fg="#fff", bg="#499272", text="Empty")
        self.btEmpty5["command"] = partial(self.funcoes, "nothing")
        self.btEmpty5.place(x=522, y=140)
        self.btEmpty6 = Button(self.frame_calculadora, width=5, height=1, font='Arial 12 bold', fg="#fff", bg="#499272", text="Empty")
        self.btEmpty6["command"] = partial(self.funcoes, "nothing")
        self.btEmpty6.place(x=522, y=180)
        self.btEmpty7 = Button(self.frame_calculadora, width=5, height=1, font='Arial 12 bold', fg="#fff", bg="#499272", text="Empty")
        self.btEmpty7["command"] = partial(self.funcoes, "nothing")
        self.btEmpty7.place(x=522, y=220)


    def mode(self):
        self.config = Button(self.frame_calculadora, width=4, height=4, bg="#003A21", fg="#fff", command=self.configuracao)
        self.config.place(x=590, y=100)
        self.Emptyconfig = Button(self.frame_calculadora, width=4, height=4, bg="#003A21", fg="#fff")
        self.Emptyconfig.place(x=590, y=180)


    def configuracao(self):
        self.top = Toplevel()
        self.top.geometry("400x300+300+100")
        self.top["bg"] = "#FFDBAA"
        self.top.resizable(0,0)
        Label(self.top, height=3, bg="#003A21", fg="#fff", text="Configurações", font="Arial 12 bold").pack(fill="x")
        Label(self.top, height=1, font="Arial 12 underline", bg="#FFDBAA", text='Unidades do ângulo: ').place(x=5, y=65)
        self.radio_radianos1 = Radiobutton(self.top, text="Graus", variable=self.radiano, value=True, command=self.radiano_false)
        self.radio_radianos1.place(x=5, y=90)
        self.radio_radianos2 = Radiobutton(self.top, text="Radianos", variable=self.radiano, value=False, command=self.radiano_true)
        self.radio_radianos2.place(x=100, y=90)
        mainloop()
    

    def radiano_false(self):
        self.radiano = False


    def radiano_true(self):
        self.radiano = True

