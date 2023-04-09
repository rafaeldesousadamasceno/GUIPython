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
               text="Alinhamento de texto\nUtilização de Padding",
               font="Arial 16",
               bd=1,
               relief="solid",
               padx=50,
               pady=20)

label2 = Label(janela,
               text="justify=LEFT\nanchor=W",
               font="Arial 16",
               bd=1,
               relief="solid",
               padx=10,
               width=20,
               height=4,
               justify=LEFT,
               anchor=W)

label3 = Label(janela,
               text="justify=LEFT\nanchor=W",
               font="Arial 16",
               bd=1,
               relief="solid",
               padx=10,
               width=20,
               height=4,
               justify=RIGHT,
               anchor=E)

label4 = Label(janela,
               text="justify=LEFT\nanchor=W",
               font="Arial 16",
               bd=1,
               relief="solid",
               width=20,
               height=4,
               justify=CENTER,
               anchor=CENTER)

label1.pack()
label2.pack()
label3.pack()
label4.pack()

janela.mainloop()

