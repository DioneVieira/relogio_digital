from tkinter import *
import tkinter
from datetime import datetime

import pyglet
pyglet.font.add_file("digital-7.ttf")


######cores#####(https://metring.com.br/lista-de-cores-rgb#:~:text=RGB%20significa%20%22Red%2C%20Green%2C,0%2C%20azul%20%3D%200).)
cor1 = "#000000" # preta
cor2 = "#fafcff" # branca
cor3 = "#21c25c" # verde
cor4 = "#eb463b" # vermelho
cor5 = "#dedcdc" # cinza
cor6 = "#3080f0" # azul
cor7 = "#00FF00" # verde limão



fundo = cor1
cor = cor7

janela = Tk()
janela.title("Meu Relógio Python")
janela.geometry("440x180")
janela.resizable(width=FALSE, height=FALSE)
janela.configure(bg = cor1)


def relogio():
    tempo = datetime.now()

    hora = tempo.strftime("%H:%M:%S")
    dia_semana = tempo.strftime("%A")
    dia = tempo.day
    mes = tempo.strftime("%b") #B maiusculo para aparecer nome do mes sem abreviação
    ano = tempo.strftime("%Y")

    l1.config(text=hora)
    l1.after(200, relogio)
    l2.config(text=dia_semana + ", " + str(dia) + "/" + str(mes) + "/" + str(ano))

l1 = Label(janela, text="", font=("digital-7 100"), bg=fundo, fg=cor)
l1.grid(row=0, column=0, sticky=NW, padx=5)

l2 = Label(janela, text="", font=("digital-7 18"), bg=fundo, fg=cor)
l2.grid(row=1, column=0, sticky=NW, padx=5)


relogio()
janela.mainloop()
