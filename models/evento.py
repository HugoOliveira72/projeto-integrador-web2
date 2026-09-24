# models/evento.py


class Evento:

    def __init__(self, nome, data, local, vagas, id=None):
        self.id = id
        self.nome = nome
        self.data = data
        self.local = local
        self.vagas = vagas
