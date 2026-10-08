# DAO (Data Access Object) - concentra o acesso aos dados.
# Todo o SQL do projeto fica aqui. O Controller nao conhece SQL.

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
