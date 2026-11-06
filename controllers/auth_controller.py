
from flask import (session, Blueprint, render_template, request, redirect,
                   url_for, flash, abort)
from models.usuario import Usuario
from dao.auth_dao import buscar_usuario_por_email
from werkzeug.security import check_password_hash

autenticacao_bp = Blueprint("autenticacao", __name__)


@autenticacao_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":

        usuario = request.form['username']
        password = request.form['password']

        if autenticar_usuario(usuario, password):
            render_template("success.html")
        else:
            render_template("fail.html")

        return render_template("login.html")


def autenticar_usuario(email, password):
    usuario = buscar_usuario_por_email(email)
    if usuario and check_password_hash(usuario["password"], password):
        session["usuario_id"] = usuario["id"]
        session["usuario_perfil"] = usuario["perfil"]
        return True
    return False
