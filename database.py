# Conexao com o banco e criacao das tabelas.
# Usa o modulo sqlite3, que ja vem com o Python.

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
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS evento (
        id    INTEGER PRIMARY KEY AUTOINCREMENT,
        nome  TEXT NOT NULL,
        data  TEXT NOT NULL,
        local TEXT,
        vagas INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS participante (
        id    INTEGER PRIMARY KEY AUTOINCREMENT,
        nome  TEXT NOT NULL,
        email TEXT NOT NULL
    )
    """)

    # Entidade associativa: resolve o N:N entre participante e evento.
    # As colunas participante_id e evento_id guardam o id das outras
    # entidades (sao as chaves estrangeiras do DER).
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS inscricao (
        id              INTEGER PRIMARY KEY AUTOINCREMENT,
        participante_id INTEGER NOT NULL,
        evento_id       INTEGER NOT NULL,
        data_inscricao  TEXT
    )
    """)

    conexao.commit()
    conexao.close()
