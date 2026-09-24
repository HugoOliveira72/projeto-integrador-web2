from flask import Flask
from controllers.evento_controller import evento_bp
from database import criar_tabelas

app = Flask(__name__)
app.register_blueprint(evento_bp)

if __name__ == "__main__":
    criar_tabelas()
    app.run(debug=True)
