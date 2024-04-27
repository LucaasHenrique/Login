import front as ft
import backend as bk
from tkinter import messagebox

app = None


def insert():
    bk.create(app.email.get(), app.senha.get())
    messagebox.showinfo('cadastro', 'cadastro feito com sucesso')
    app.clear()


def verificarLogin():
    dados_login = bk.read()
    login = False
    for rows in dados_login:
        if app.email.get() in rows and app.senha.get() in rows:
            login = True
    if login:
        messagebox.showinfo('OK', 'Login feito com sucesso')
        app.clear()
    else:
        messagebox.showerror('ERROR', 'Senha ou email incorretos')


if __name__ == '__main__':
    app = ft.Tela()
    app.botCad.configure(command=insert)
    app.botLogin.configure(command=verificarLogin)
    app.run()
