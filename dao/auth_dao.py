from extensions import db
from models.usuario import Usuario
from werkzeug.security import generate_password_hash

senha_hash = generate_password_hash("segredo123")

banco_de_usuarios = [
    {
        "id": 1,
        "email": "admin@teste.com",
        "password": senha_hash,
        "perfil": "administrador"
    }
]


def obter_perfil_usuario(email):
    usuario = buscar_usuario_por_email(email)
    if usuario:
        return usuario["perfil"]
    return None


def buscar_usuario_por_email(email):
    for usuario in banco_de_usuarios:
        if usuario["email"] == email:
            return usuario
    return None
