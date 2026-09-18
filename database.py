import os 
import sqlite3

conexao = sqlite3.connect("instance/eventos.db")
cursor = conexao.cursor()

cursor.execute("""
  CREATE TABLE  IF NOT EXISTS evento (
    id   INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
    )
""")

cursor.execute(
  "INSERT INTO evento (nome,data) VALUES (?,?)" ,
   ("Hackathon", "2026-10-01")

               )

conexao.commit()

cursor.execute("SELECT id, nome FROM evento")
for linha in cursor.fetchall():
  print(linha)
