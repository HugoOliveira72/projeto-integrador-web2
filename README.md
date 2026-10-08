# projeto-integrador-web2

> Repositório para o Projeto Integrador da disciplina de Desenvolvimento Web 2.


## 👥 Integrantes

- **Hugo José de Oliveira**

- **Maria Luísa Araújo da Silva**


## 📁 Estrutura do Projeto

```
projeto-integrador-web2/
├── app.py
├── requirements.txt
├── Dockerfile -- Opcional
└── .dockerignore -- Opcional
```


## 🚀 Como Executar o Projeto

### Opção 1: Execução Local (Python na máquina)

1. **Clonar/Acessar o projeto:** Abra o terminal na pasta raiz do projeto.

2. **Criar o ambiente virtual (venv):**

```
python -m venv venv
```

3. **Ativar a venv:**

   - **Windows (PowerShell):**

   - ```
.\venv\Scripts\Activate
```

   - *(Se ocorrer erro de permissão de script, execute no PowerShell: (Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned);(& "C:\Users\Nome-do-usuario\projeto-integrador-web2\venv\Scripts\Activate.ps1") *

   - *No lugar das aspas, adicionar o caminho do projeto*

4. **Instalar as dependências:**

```
pip install -r requirements.txt
```

5. **Executar a aplicação:**

```
python app.py
```

Acesse no navegador : **`http://localhost:(Porta exibida no terminal)`**


### Opção 2: Execução via Docker (Python no Docker)

1. **Pré-requisitos:** Garantir que o Docker Desktop esteja instalado e ativo.

2. **Construir a imagem Docker:**

```
docker build -t meu-flask-app:1.0 .
```

3. **Executar o contêiner:**

   - **Modo Interativo (com logs no terminal):**

   - ```
docker run --name meu-flask-container -p 5000:5000 meu-flask-app:1.0
```

   - **Modo Em Segundo Plano (Detached):**

   - ```
docker run -d --name meu-flask-container -p 5000:5000 meu-flask-app:1.0
```

4. **Acessar a aplicação:** Abra o navegador em: **`http://localhost:5000`**


## ⚙️ Configurações do Projeto

### `Dockerfile`

```
FROM python:3.14.7-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

- **Base:** Imagem Python otimizada (`slim`).

- **Flags de ambiente:** Evita geração de `.pyc` (`PYTHONDONTWRITEBYTECODE`) e garante envio imediato de logs (`PYTHONUNBUFFERED`).

- **Instalação:** Copia e instala apenas os pacotes de `requirements.txt` sem cache extra.

### `app.py`

```
from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Aplicação Flask executando no Docker!"

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
```

- **Host `0.0.0.0`:** Permite que o servidor Flask receba requisições externas através do mapeamento de porta do Docker.


## 🛠️ Comandos Úteis do Docker

| Ação | Comando |
| - | - |
| **Listar Imagens** | `docker images` |
| **Listar Contêineres Rodando** | `docker ps` |
| **Listar Todos os Contêineres** | `docker ps -a` |
| **Acompanhar Logs** | `docker logs -f meu-flask-container` |
| **Pausar / Despausar** | `docker pause meu-flask-container` / `docker unpause meu-flask-container` |
| **Parar / Iniciar / Reiniciar** | `docker stop meu-flask-container` / `docker start meu-flask-container` / `docker restart meu-flask-container` |
| **Remover Contêiner** | `docker rm meu-flask-container` |
| **Remover Imagem** | `docker rmi meu-flask-app:1.0` |
| **Acessar Terminal Interno** | `docker exec -it meu-flask-container bash` |



## 🧠 Fluxo de Funcionamento

```
requirements.txt
      │
      ▼
Dockerfile ───────► docker build ───► Imagem Docker
                                            │
                                            ▼
                                       docker run
                                            │
                                            ▼
                                        Container
                                            │
                                            ▼
                                   http://localhost:5000
```

