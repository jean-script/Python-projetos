
class Materias:
  
  def __init__(self, nome,hora):
    self._nome = nome
    self._hora = hora 
    
  @property
  def nome(self):
    return self._nome
  
  @property
  def hora(self):
    return self._hora
  
  def __str__(self):
    return f'Esta materia esta na sua grade'
  

class Professor(Materias):
  def __init__(self, nome, hora):
    super().__init__(nome, hora)
  pass
    
    
Matematica = Materias('Matematica', '2h')

print(Matematica.nome)
print(Matematica.hora)
print(Matematica)

professor = Professor('Jean Carlos', '13h ')
print(professor.nome)
print(professor.hora)