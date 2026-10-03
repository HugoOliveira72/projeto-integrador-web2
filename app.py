from flask import Flask
from controllers.evento_controller import evento_bp
from database import criar_tabelas

app = Flask(__name__)
#Onde fica o banco de fato.
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///eventos.db"


app.secret_key = "dw2-chave-de-aula"

app.register_blueprint(evento_bp)

app.app.context().push()

if __name__ == "__main__":
    #criar_tabelas()
    db.create_all() #cria as tabelas que ainda não tem
    app.run(debug=True)

# if __name__ == "__main__":
#     app.run(
#         host="0.0.0.0",
#         port=5000,
#         debug=True
#     )
