from tkinter import *

def calcular():
    F = float(txtFarenheit.get())
    C = (F-32) * (5/9)
    resultado.set(str(round(C,1))+" ºC")

corBG = "#0984e3"
corButton = "#2C3E50"

janela = Tk()
janela.title("Conversor de Temperatura")
janela['bg'] = corBG

resultado = StringVar()

"""
# CENTRALIZANDO A JANELA
largura = 400
altura = 300

largura_monitor = janela.winfo_screenwidth()
altura_monitor = janela.winfo_screenheight()

posX = largura_monitor/2 - largura/2
posY = altura_monitor/2 - altura/2

janela.geometry("%dx%d+%d+%d" % (largura, altura, posX, posY))
"""

# CRIANDO OS COMPONENTES
frameFarenheit = Frame(janela, bg=corBG)
lbFarenheit = Label(frameFarenheit, text="Digite a temperatura em (ºF)",
                font="Arial 15",
                padx=10,
                pady=10,
                bg=corBG,
                fg="#fff")
txtFarenheit = Entry(frameFarenheit,
                font="Arial 15")
lbHR = Label(frameFarenheit, font="Arial 10", bg=corBG,)
btnConverter = Button(frameFarenheit, text="Converter em ºC", command=calcular,
                font="Arial 15",
                padx=10,
                pady=10,
                bg=corBG,
                fg="#fff")
lbResultado = Label(frameFarenheit, textvariable=resultado,
                font="Arial 15",
                padx=10,
                pady=10,
                bg=corBG,
                fg="#fff")

# ORGANIZANDO LAYOUT
lbFarenheit.grid(column=0, row=0)
txtFarenheit.grid(column=0, row=1)
lbHR.grid(column=0, row=2)
btnConverter.grid(column=0, row=3)
lbResultado.grid(column=0, row=4)

frameFarenheit.grid()

janela.mainloop()