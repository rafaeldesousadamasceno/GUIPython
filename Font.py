from tkinter import *

def negrito():
    label1["font"] = "%s %d %s" % (fontFamily, fontSize, "bold")
    label2["font"] = "%s %d %s" % ("Arial", 20, "bold")
    label3["font"] = "%s %d %s" % ("Verdana", 30, "bold")

def normal():
    label1["font"] = "%s %d" % (fontFamily, fontSize)
    label2["font"] = "%s %d" % ("Arial", 20)
    label3["font"] = "%s %d" % ("Verdana", 30)

def aumentandoFont():
    global fontSize
    fontSize += 1
    label1["font"] = "%s %d" % (fontFamily, fontSize)

def diminuindoFont():
    global fontSize
    fontSize -= 1
    label1["font"] = "%s %d" % (fontFamily, fontSize)

janela = Tk()
janela.title("Fontes")
janela.geometry("800x600+200+200")

fontFamily = "Consolas"
fontSize = 12

label1 = Label(janela, 
               text="Este é um Label que tem fonte",
               bg="#ffaa00",
               font="%s %d" % (fontFamily, fontSize))

label2 = Label(janela, 
               text="Este é um Label que tem fonte",
               bg="#ff0000",
               font="%s %d bold italic" % ("Arial", 20))

label3 = Label(janela, 
               text="Este é um Label que tem fonte",
               bg="#0000ff",
               font="%s %d bold" % ("Verdana", 30),
               fg="#aaaaaa")

aumentar = Button(janela, text="Aumentando o tamanho da fonte", command=aumentandoFont)
diminuir = Button(janela, text="Diminuindo o tamanho da fonte", command=diminuindoFont)
btnNegrito = Button(janela, text="Negrito nas Labels", command=negrito)
btnNormalFont = Button(janela, text="Fonte Normal nas Label", command=normal)

aumentar.pack()
diminuir.pack()
btnNegrito.pack()
btnNormalFont.pack()
label1.pack()
label2.pack()
label3.pack()

janela.mainloop()