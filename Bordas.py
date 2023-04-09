from tkinter import *

janela = Tk()
janela.title("Label")
janela.iconbitmap("img/icon_002.ico")

# CENTRALIZANDO JANELA
largura = 800
altura = 600

larguraDaTela = janela.winfo_screenwidth()
alturaDaTela = janela.winfo_screenheight()

posX = larguraDaTela/2 - largura/2
posY = alturaDaTela/2 - altura/2

janela.geometry("%dx%d+%d+%d" % (largura, altura, posX, posY))
# FIM DO CÓDIGO DE CENTRALIZAÇÃO DA JANELA

# CRIANDO LABEL
label1 = Label(janela, text="LABEL COM RELIEF solid",
               font="Arial 20",
               bd=5,
               relief="solid")

label2 = Label(janela, text="LABEL COM RELIEF flat",
               font="Arial 20",
               bd=5,
               relief="flat")
label3 = Label(janela, text="LABEL COM RELIEF groove",
               font="Arial 20",
               bd=5,
               relief="groove")
label4 = Label(janela, text="LABEL COM RELIEF raised",
               font="Arial 20",
               bd=5,
               relief="raised")
label5 = Label(janela, text="LABEL COM RELIEF ridge",
               font="Arial 20",
               bd=5,
               relief="ridge")
label6 = Label(janela, text="LABEL COM RELIEF sunken",
               font="Arial 20",
               bd=5,
               relief="sunken")

# CRIANDO UM BOTÃO
btn = Button(janela, text="My Button")

# MOSTRANDO LABELS NA ORDEM QUE EU DEFINIR O PACK DE CADA ELEMENTO
btn.pack()
label1.pack()
label2.pack()
label3.pack()
label4.pack()
label5.pack()
label6.pack()

janela.mainloop()