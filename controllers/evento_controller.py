from flask import Blueprint, render_template, request, redirect
from models.evento import Evento
from dao.evento_dao import EventDAO

evento_bp = Blueprint("evento", __name__)


@evento_bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        evento = Evento(
            request.form["nome"],
            request.form["data"],
            request.form["local"],
            request.form["vagas"]
        )

        EventDAO.salvar(evento)
        return redirect("/")
    return render_template("index.html", eventos=EventDAO.listar())
