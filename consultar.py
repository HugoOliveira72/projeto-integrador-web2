from dao.evento_dao import EventoDAO

eventos = EventoDAO.lista()

print("Eventos gravados no banco:",len(eventos))
print()

for e in eventos:
  print(e.id, e.data, e.nome, e.local, e.vagas)

print()
print("Os dados sobreviveram ao encerramento da aplicação.")
