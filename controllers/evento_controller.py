from curses import flash
from flask import Blueprint, render_template, request, redirect,
                   url_for, flash
from models.evento import Evento
from dao.evento_dao import EventoDAO

evento_bp = Blueprint("evento", __name__)


@evento_bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # O __init__ do modelo do ORM aceita apenas argumentos NOMEADOS.
        evento = Evento(
            request.form["nome"],
            request.form["data"],
            request.form["local"],
            request.form["vagas"]
        )
        EventoDAO.salvar(evento)
        flash("Evento cadastrado com sucesso!")
        return redirect(url_for("evento.index"))

    return render_template("index.html", eventos=EventoDAO.listar())


@evento_bp.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    evento = EventoDAO.buscar_por_id(id)
    if evento is None:          # id inexistente -> pagina 404
        abort(404)

    if request.method == "POST":
        EventoDAO.atualizar(
            evento,
            request.form["nome"],
            request.form["data"],
            request.form["local"],
            request.form["vagas"],
        )
        flash("Evento atualizado com sucesso!")
        # "evento.index" = nome do Blueprint + nome da funcao da rota
        return redirect(url_for("evento.index"))
        #evento.index eh o nome do Blueprint 

    return render_template("editar.html", evento=evento)

