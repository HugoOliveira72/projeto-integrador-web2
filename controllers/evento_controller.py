from flask import Blueprint, render_template, request, redirect
from models.evento import Evento
from data.memory import eventos

evento_bp = Blueprint ("evento", __name__)