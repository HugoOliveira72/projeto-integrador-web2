# DAO (Data Access Object) - concentra o acesso aos dados.
# Todo o SQL do projeto fica aqui. O Controller nao conhece SQL.


# class EventDAO:
#     # Insere um evento no banco e confirma a transacao.
#     @staticmethod
#     def salvar(evento):
#         conexao = conectar()
#         cursor = conexao.cursor()
#         cursor.execute("INSERT INTO evento (nome, data, local, vagas) VALUES (?, ?, ?, ?)",
#                        (evento.nome, evento.data, evento.local, evento.vagas)
#                        )
#         conexao.commit()
#         conexao.close()

#     # Consulta os eventos e devolve uma lista de objetos Evento.
#     @staticmethod
#     def listar():
#         conexao = conectar()
#         cursor = conexao.cursor()
#         cursor.execute("SELECT id, nome, data, local, vagas FROM evento")
#         linhas = cursor.fetchall()
#         conexao.close()

#         # O banco devolve tuplas. Convertemos cada tupla em um objeto
#         # para a View escrever e.nome em vez de linha[1].
#         eventos = []
#         for linha in linhas:
#             evento = Evento(linha[1], linha[2], linha[3],
#                             linha[4], id=linha[0])
#             eventos.append(evento)
#         return eventos

from extensions import db
from models.evento import Evento


class EventoDAO:

    @staticmethod
    def salvar(evento):
        db.session.add(evento)
        db.session.commit()

    @staticmethod
    def listar():
        return Evento.query.all()
