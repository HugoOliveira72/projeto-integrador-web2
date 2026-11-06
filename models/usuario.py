from extensions import db


class Usuario(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   nome = db.Column(db.String(120), nullable=False)
   email = db.Column(db.String(120), nullable=False, unique=True)
   senha_hash = db.Column(db.String(255), nullable=False)
   # "admin" ou "comum"
   perfil = db.Column(db.String(20), nullable=False)
