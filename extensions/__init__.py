# extensions/__init__.py
# Objeto do ORM criado em um unico lugar, sem ligacao com nenhum app ainda.
# Os models importam este "db" para declarar tabelas; o app o conecta ao
# Flask depois, em database.py (db.init_app). Isso evita import circular.

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()