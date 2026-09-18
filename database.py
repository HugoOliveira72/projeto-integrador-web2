import os 
import sqlite3

CAMINHO_BANCO = "instance/eventos.db"

# Abre a conexao com o banco.
# O SQLite cria o arquivo, mas nao cria a pasta: por isso o makedirs.
def conectar():
    os.makedirs("instance", exist_ok=True)
    return sqlite3.connect(CAMINHO_BANCO)


# Cria as tabelas do DER da Aula 5.
def criar_tabelas():
  conexao = sqlite3.connect("instance/eventos.db")
  cursor = conexao.cursor()

#Tabela evento
cursor.execute("""
  CREATE TABLE  IF NOT EXISTS evento (
    id   INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
    )
""")

#Tabela participante
cursor.execute("""
    CREATE TABLE IF NOT EXISTS participante (
        id    INTEGER PRIMARY KEY AUTOINCREMENT,
        nome  TEXT NOT NULL,
        email TEXT NOT NULL
    )
    """)
#Tabela associativa
cursor.execute("""
    CREATE TABLE IF NOT EXISTS inscricao (
        id              INTEGER PRIMARY KEY AUTOINCREMENT,
        participante_id INTEGER NOT NULL,
        evento_id       INTEGER NOT NULL,
        data_inscricao  TEXT
    )
    """)
#Inserts a serem modificados!
cursor.execute(
  "INSERT INTO evento (nome,data) VALUES (?,?)" ,
   ("Hackathon", "2026-10-01")

               )

conexao.commit()

#cursor.execute("SELECT id, nome FROM evento")
#for id_evento, nome in cursor.fetchall():
 #   print(id_evento, nome)


conexao.close()
