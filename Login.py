from tkinter import *

corBG = "#0984e3"
corButton = "#2C3E50"

login = Tk()
login.title("Login")
login['bg'] = corBG

# Centralizando tela
largura = 350
altura = 220

largura_screen = login.winfo_screenwidth()
altura_screen = login.winfo_screenheight()

posX = largura_screen/2 - largura/2
posY = altura_screen/2 - altura/2

login.geometry("%dx%d+%d+%d" % (largura, altura, posX, posY))

# DESATIVANDO O MAXIMIZAR
login.resizable(False, False)

# CRIANDO OS COMPONENTES DA TELA DE LOGIN
lbUser = Label(login, 
                text="Usuário: ", 
                font="Arial 15",
                padx=10,
                pady=10,
                bg=corBG,
                fg="#fff")

lbPass = Label(login, 
                text="Senha: ", 
                font="Arial 15",
                padx=10,
                pady=10,
                bg=corBG,
                fg="#fff")

txtUser = Entry(login, 
                font="Arial 15")

txtPass = Entry(login, 
                font="Arial 15")

lbHR = Label(login,
                text="---------",
                font="Arial 8",
                bg=corBG,
                fg="#fff")

btnLogar = Button(login,
                text="Logar",
                font="Arial 15",
                width=20,
                bg=corButton,
                fg="#fff")

btnCadastrar = Button(login,
                text="Cadastrar",
                font="Arial 15",
                width=20,
                bg=corButton,
                fg="#fff")

# ORGANIZANDO OS COMPONENTES DA TELA DE LOGIN
lbUser.grid(column=0, row=0, sticky=E)
lbPass.grid(column=0, row=1, sticky=E)
txtUser.grid(column=1, row=0)
txtPass.grid(column=1, row=1)
btnLogar.grid(columnspan=2, row=2)
lbHR.grid(columnspan=2, row=3)
btnCadastrar.grid(columnspan=2, row=4)



# SETANDO O FOCO NO CAMPO DE USUÁRIO
txtUser.focus()

login.mainloop()