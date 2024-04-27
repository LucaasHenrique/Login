import mysql.connector


class Transaction:
    def __init__(self):
        self.connected = False
        self.conn = None
        self.cursor = None
        self.database = 'login'

    def Connect(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='',
            password='',
            database=f'{self.database}'
        )
        self.cursor = self.conn.cursor()
        self.connected = True


    def Disconnect(self):
        self.conn.close()
        self.cursor.close()
        self.connected = False


    def Execute(self, sql):
        if self.connected:
            self.cursor.execute(sql)
            return True
        else:
            return False


    def Fetchall(self):
        return self.cursor.fetchall()

  
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
