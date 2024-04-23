import mysql.connector


# Classe que realiza as operações no banco de dados
class Transaction:
    def __init__(self):
        self.connected = False
        self.conn = None
        self.cursor = None
        self.database = 'login'

    # Realiza a conexao com o banco de dados
    def Connect(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='',
            password='',
            database=f'{self.database}'
        )
        self.cursor = self.conn.cursor()
        self.connected = True

    # Fecha a conexao com o banco de dados
    def Disconnect(self):
        self.conn.close()
        self.cursor.close()
        self.connected = False

    # Função que executa os comando sql
    def Execute(self, sql):
        if self.connected:
            self.cursor.execute(sql)
            return True
        else:
            return False

    # Realiza a busca de items do banco de dados
    def Fetchall(self):
        return self.cursor.fetchall()

    # Salva as operações realizadas no banco
    def Commit(self):
        if self.connected:
            self.conn.commit()
            return True
        else:
            return False


def create(email, senha):
    operacoes = Transaction()
    operacoes.Connect()
    operacoes.Execute(f'INSERT INTO login (email, senha) VALUES("{email}", "{senha}")')
    operacoes.Commit()
    operacoes.Disconnect()


def read():
    operacoes = Transaction()
    operacoes.Connect()
    operacoes.Execute(f'SELECT * FROM login')
    rows = operacoes.Fetchall()
    operacoes.Disconnect()
    return rows
