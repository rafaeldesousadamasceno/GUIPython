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
label1 = Label(janela, text="Meu primeiro Label")
label2 = Label(janela, text="Meu segundo Label")
label3 = Label(janela, text="Meu terceiro Label")

# CRIANDO UM BOTÃO
btn = Button(janela, text="My Button")

# MOSTRANDO LABELS NA ORDEM QUE EU DEFINIR O PACK DE CADA ELEMENTO
label3.pack()
label1.pack()
btn.pack()
label2.pack()

janela.mainloop()