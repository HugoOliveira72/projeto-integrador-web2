from flask import Flask
from controllers.evento_controller import evento_bp
from controllers.auth_controller import autenticacao_bp
from database import criar_tabelas, conectar_banco
from extensions import db 

# Cria o app Flask e
app = Flask(__name__)
app.secret_key = 'chave secreta'

# Conecta o ORM ao app (precisa estar fora do __main__ para que outros
# arquivos, como consultar.py, tambem encontrem o ORM configurado).
#conectar_banco(app)
# Agrupa as rotas do Blueprint "evento" no app. Todas as rotas do
# Blueprint comecam com /evento.

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eventos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db.init_app(app)

app.register_blueprint(evento_bp)
app.register_blueprint(autenticacao_bp)

if __name__ == "__main__":
    with app.ap.context():
        db.create_all()

     app.run(debug = True)
    
