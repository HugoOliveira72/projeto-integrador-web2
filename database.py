from extensions import db
from models.evento import Evento

# Abre a conexao com o banco.
#Agora não precisa mais do CAMINHO_BANCO = "instance/eventos.db", pq o SQLAlchemy ja sabe onde fica o banco. 
# Ele automaticamente cria o arquivo do banco se ele nao existir. em instance/eventos.db
def conectar_banco(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///eventos.db"
    db.init_app(app)

# Cria as tabelas do banco, caso nao existam.
def criar_tabelas(app):
    with app.app_context():
        db.create_all()
