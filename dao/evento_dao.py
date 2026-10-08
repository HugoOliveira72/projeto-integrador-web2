# DAO (Data Access Object) - concentra o acesso aos dados.
# O acesso ao banco e feito pelo ORM (db.session / Evento.query).
# O Controller nao conhece SQL nem a sessao do ORM.

from extensions import db
from models.evento import Evento


class EventoDAO:

    # Prepara a insercao do evento e confirma a transacao.
    @staticmethod
    def salvar(evento):
        db.session.add(evento)
        db.session.commit()

    # Devolve uma lista de objetos Evento.
    @staticmethod
    def listar():
        return Evento.query.all()

    # Devolve um Evento pela chave primaria, ou None se nao existir.
    # (db.session.get e a forma atual; Query.get() e considerado legado.)
    @staticmethod
    def buscar_por_id(id):
        return db.session.get(Evento, id)

    # UPDATE: basta alterar os atributos do objeto e confirmar;
    # o ORM percebe a mudanca e gera o UPDATE sozinho.
    @staticmethod
    def atualizar(evento, nome, data, local, vagas):
        evento.nome = nome
        evento.data = data
        evento.local = local
        evento.vagas = vagas
        db.session.commit()

    # DELETE: prepara a remocao do objeto e confirma.
    @staticmethod
    def deletar(evento):
        db.session.delete(evento)
        db.session.commit()
