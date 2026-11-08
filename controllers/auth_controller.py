from flask import (session, Blueprint, render_template, request, redirect,
                   url_for, flash, abort)
from dao.usuario_dao import UsuarioDAO
from werkzeug.security import check_password_hash, generate_password_hash
from models.usuario import Usuario
from werkzeug.security import check_password_hash

autenticacao_bp = Blueprint("autenticacao", __name__)


@autenticacao_bp.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        email = request.form['email'].strip().lower()
        senha = request.form['senha']
        nome = request.form['nome']

        # Verifica se o email já está cadastrado
        if UsuarioDAO.buscar_usuario_por_email(email):
            flash("Email já cadastrado. Por favor, use outro email.", "error")
            return render_template("cadastro.html")

        # Cria um novo usuário e salva no banco de dados
        usuario = Usuario(
            nome=nome,
            email=email,
            senha_hash=generate_password_hash(senha),
            perfil="comum"  # Define o perfil como "comum"
        )
        UsuarioDAO.salvar(usuario)

        flash("Cadastro realizado com sucesso! Faça login para continuar.", "success")
        return redirect(url_for("autenticacao.login"))

    return render_template("cadastro.html")


@autenticacao_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":

        # Pega o email do formulário, remove espaços e converte em minúsculas
        email = request.form['email'].strip().lower()
        senha = request.form['senha']
        if autenticar_usuario(email, senha):
            flash("Login realizado com sucesso!", "success")
            return redirect(url_for("eventos.index"))
        else:
            flash("Email ou senha incorretos. Por favor, tente novamente.", "error")

    return render_template("login.html")


def autenticar_usuario(email, password):
    usuario = UsuarioDAO.buscar_usuario_por_email(email)
    if usuario and check_password_hash(usuario.senha_hash, password):
        session["usuario_id"] = usuario.id
        session["usuario_perfil"] = usuario.perfil
        return True
    return False
