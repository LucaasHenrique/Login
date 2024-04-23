import customtkinter
import tkinter


# Classe para a criação da janela de teste
class Tela(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        """self.janela = customtkinter.CTk()"""
        self.title('janela mae')
        self.geometry('300x300')
        self.resizable(False, False)
        self.title('Cadastro')
        self.text1 = customtkinter.CTkLabel(self, text='CADASTRO')
        self.text1.pack(padx=10, pady=10)

        self.email = customtkinter.CTkEntry(self, placeholder_text='seu email')
        self.email.pack(padx=10, pady=10)

        self.senha = customtkinter.CTkEntry(self, placeholder_text='sua senha')
        self.senha.pack(padx=10, pady=10)

        self.botCad = customtkinter.CTkButton(self, text='Fazer Cadastro')
        self.botCad.pack(padx=10, pady=10)
        self.botLogin = customtkinter.CTkButton(self, text='fazer login')
        self.botLogin.pack(padx=10, pady=10)

    def clear(self):
        self.email.delete(0, tkinter.END)
        self.senha.delete(0, tkinter.END)

    def run(self):
        self.mainloop()
