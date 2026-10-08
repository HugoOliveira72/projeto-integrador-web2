from flask import Flask
from controllers.evento_controller import evento_bp
from database import criar_tabelas, conectar_banco

#Cria o app Flask e 
app = Flask(__name__)

# Conecta o ORM ao app (precisa estar fora do __main__ para que outros
# arquivos, como consultar.py, tambem encontrem o ORM configurado).
conectar_banco(app)
app.secret_key = "dw2-chave-de-aula"

# Agrupa as rotas do Blueprint "evento" no app. Todas as rotas do
# Blueprint comecam com /evento.
app.register_blueprint(evento_bp)

if __name__ == "__main__":
    criar_tabelas(app)
    app.run(debug=True)
