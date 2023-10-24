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
        self.con.execute(
            "INSERT INTO Tarefas (Titulo, data) Values (?, ?)", (titulo, data)
        )
        self.con.commit()
