from tkinter import *

janelaCentralizada = Tk()
janelaCentralizada.title('Janela Centralizada')

# DIMENSÕES DA JANELA
largura = 800
altura = 600

# RESOLUÇÃO DO SISTEMA OPERACIONAL
largura_screen = janelaCentralizada.winfo_screenwidth()
altura_screen = janelaCentralizada.winfo_screenheight()

# POSIÇÃO DA JANELA
posx = (largura_screen/2) - (largura/2)
posy = (altura_screen/2) - (altura/2)

# DEFININDO GEOMETRY
janelaCentralizada.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

print(largura_screen, "X", altura_screen)

janelaCentralizada.mainloop()