from tkinter import *

def mudarBackground():
    if janela['bg'] == "#000":
        janela['bg'] = "#fff"
    else:
        janela['bg'] = "#000"

def mensagem(msg):
    print(msg)

janela = Tk()

janela.title("Título")
janela.geometry("500x500+200+200")

# BUTTON PRECISA SER ASSOCIADO A UMA JANELA, TEXT, FUNÇÃO A SER EXECUTADA
btn = Button(janela, text="Mudar Background", command=mudarBackground)
btn.pack()

# UTILIZANDO UMA FUNÇÃO COM PARÂMETRO [command=lambda: Function(parâmetro)]
btn1 = Button(janela, text="Escrever Mensagem", command=lambda: mensagem("Olá Mundo"))
btn1.pack()

janela.mainloop()