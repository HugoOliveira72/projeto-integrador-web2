from extensions import db
from models.usuario import Usuario
from werkzeug.security import generate_password_hash


class UsuarioDAO:
    @staticmethod
    def buscar_usuario_por_email(email):
        return db.session.query(Usuario).filter_by(email=email).first()

    @staticmethod
    def salvar(usuario):
        db.session.add(usuario)
        db.session.commit()
