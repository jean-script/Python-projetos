import json

with open("file.json") as file:
    content = json.load(file)
    
    lista = content.get("Lista")
    numero_indica = 1
    
    for itens in lista:
        print(f'Usuario {numero_indica}: {lista[itens]}')
        numero_indica += 1 
        
