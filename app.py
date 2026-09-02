from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return "Hello, World!"

@app.route('/sobre')
def sobre():
    return "Esta é a página sobre."

@app.route('/evento')
def evento():
    return "Bem-vindo à página do evento!"

#Execução de if 
if __name__ == '__main__':
    app.run(debug=True)