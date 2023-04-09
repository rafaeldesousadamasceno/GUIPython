from tkinter import *

janela = Tk()
janela.title("Altura de Label")

# CENTRALIZANDO A JANELA
largura = 800
altura = 800

largura_monitor = janela.winfo_screenwidth()
altura_monitor = janela.winfo_screenheight()

posX = largura_monitor/2 - largura/2
posY = altura_monitor/2 - altura/2

janela.geometry("%dx%d+%d+%d" % (largura, altura, posX, posY))

# CRIANDO LABELS E MODIFICANDO POSIÇÃO DA LABEL E ALTURA
label1 = Label(janela,
               text="Posicionamento das Labels\nBaseado na rosa dos Ventos",
               font="Arial 16",
               bd=1,
               relief="solid")

label2 = Label(janela,
               text="Label 2\nanchor=W",
               font="Arial 16",
               bd=1,
               relief="solid",
               width=20,
               height=4,
               anchor=W)

label3 = Label(janela,
               text="Label 3\nanchor=N",
               font="Arial 16",
               bd=1,
               relief="solid",
               width=20,
               height=4,
               anchor=N)

label4 = Label(janela,
               text="Label 4\nanchor=E",
               font="Arial 16",
               bd=1,
               relief="solid",
               width=20,
               height=4,
               anchor=E)

label5 = Label(janela,
               text="Label 5\nanchor=S",
               font="Arial 16",
               bd=1,
               relief="solid",
               width=20,
               height=4,
               anchor=S)

label6 = Label(janela,
               text="Label 6\nanchor=CENTER",
               font="Arial 16",
               bd=1,
               relief="solid",
               width=20,
               height=4,
               anchor=CENTER)

label7 = Label(janela,
               text="Label 7\nanchor=NE",
               font="Arial 16",
               bd=1,
               relief="solid",
               width=20,
               height=4,
               anchor=NE)

label1.pack()
label2.pack()
label3.pack()
label4.pack()
label5.pack()
label6.pack()
label7.pack()

janela.mainloop()