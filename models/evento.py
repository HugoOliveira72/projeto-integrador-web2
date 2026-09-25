# models/evento.py
from extensions import db


class Evento(db.Model):

    def __init__(self, nome, data, local, vagas, id=None):
        id = db.Column(db.Integer, primary_key=True)
        nome = db.Column(db.String(120), nullable=False)
        data = db.Column(db.String(10),  nullable=False)
        local = db.Column(db.String(120))
        vagas = db.Column(db.Integer)

    db.create_all()

    novo = Evento(nome="Hackathon", data="2026-10-01", local="Lab 3", vagas=40)
    db.session.add(novo)
    db.session.commit()
