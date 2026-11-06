from flask import session, redirect, url_for, render_template
from flask import Blueprint
from functools import wraps

evento_bp = Blueprint('eventos', __name__)

@evento_bp.before_request
def exigir_login():
    # Verifica se o usuário está logado antes de acessar qualquer rota
    if 'usuario_id' not in session:
        print("Você precisa estar logado para acessar esta página.")
        return redirect(url_for('autenticacao.login'))  # Redireciona para a página de login

def verificar_perfil(perfil_necessario):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if 'usuario_perfil' not in session or session['usuario_perfil'] != perfil_necessario:
                print("Você não tem permissão para acessar esta página.")
                return render_template('fail.html')
            return func(*args, **kwargs)
        return wrapper
    return decorator

@evento_bp.route('/eventos', methods=['GET'], endpoint='listar_eventos')
@verificar_perfil('administrador')
def listar_eventos():
    # Aqui você pode adicionar a lógica para listar eventos
    return render_template('eventos.html')
