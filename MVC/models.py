import sqlite3
import os


class BancoDeDados:
    def __init__(self, dbsqlite):
        if not os.path.exists("dbsqlite"):
            self.con = sqlite3.Connection("dbsqlite")
            self.con.execute(
                "CREATE TABLE Tarefas(ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT ,Titulo TEXT NOT NULL, data DATE NOT NULL)"
            )
            self.con.commit()
        else:
            self.con = sqlite3.Connection("dbsqlite")

    def salvar_alteracao(self, titulo, data):
         if titulo:
            self.con.execute("INSERT INTO Tarefas (Titulo, data) VALUES (?, ?)", (titulo, data))
            self.con.commit()



    def mostrar_tarefas(self):
        cursor = self.con.cursor()
        cursor.execute("SELECT * FROM Tarefas")
        tarefas = cursor.fetchall()
        cursor.close()
        return tarefas
