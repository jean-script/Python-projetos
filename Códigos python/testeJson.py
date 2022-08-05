import json 

dados = {
    'nome': 'Pycodebr',
    'instagram':'@pycodebr',
    'linguagem': 'python',
    'conteudos': [
        {'conteudo': 'codigos'},
        {'conteudo': 'curiosidades'}
    ]
}

with open(r'C:\\Users\\jean\\OneDrive - Practia\\Documentos\\estudos\\Python\\dados.json','w') as json_file:
    json.dump(dados, json_file, indent=4)
    
     