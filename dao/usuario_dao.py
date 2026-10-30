@staticmethod
def buscar_por_email(email):
    return Usuario.query.filter_by(email = email).first()
