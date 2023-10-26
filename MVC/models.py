import sqlite3
import os
from datetime import datetime


class BancoDeDados:
    def __init__(self, dbsqlite):
        if not os.path.exists(dbsqlite):
            self.con = sqlite3.connect(dbsqlite)
            self.con.execute(
                "CREATE TABLE Tarefas(ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, Titulo TEXT NOT NULL, data DATE NOT NULL, status TEXT)"
            )
            self.con.commit()
        else:
            self.con = sqlite3.connect(dbsqlite)

    def salvar_alteracao(self, titulo, data, status="Fazer"):
        if titulo:
            # Converte a data para um objeto datetime
            data_formatada = datetime.strptime(data, "%Y-%m-%d").strftime("%d/%m/%Y")
            self.con.execute(
                "INSERT INTO Tarefas (Titulo, data, status) VALUES (?, ?, ?)",
                (titulo, data_formatada, status),
            )
            self.con.commit()

    def mostrar_tarefas(self):
        cursor = self.con.cursor()
        cursor.execute("SELECT * FROM Tarefas")
        tarefas = cursor.fetchall()
        cursor.close()
        return tarefas

    def editar_dado(self, id):
        feito = "Feito"
        cursor = self.con.cursor()
        try:
            cursor.execute("BEGIN")
            cursor.execute("UPDATE Tarefas SET status = ? WHERE id = ?", (feito, id))
            cursor.execute("COMMIT")
        except Exception as e:
            cursor.execute("ROLLBACK")
            print(f"Erro ao atualizar: {e}")
