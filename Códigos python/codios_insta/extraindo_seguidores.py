from datetime import datetime
import instaloader


# Carrega a lib e faz login com a conta desejada 

log = instaloader.Instaloader()
log.login('jean.aires21','980922Ged')

#carrega os dados de seguidores e seguindo do perfil escolhido
Seguidores = instaloader.Profile(log.context, 'jean.aires21').get_followers()
seguindo = instaloader.Profile(log.context, "jean.aires21").get_followees()

# Mostra resultado
print('Seguidores: {}'.format(str(Seguidores._data["count"])))
print('Seguindo: {}'.format(str(seguindo._data["count"])))

print('Lista e informações de seguidores: ')
print('\n {}'.format(Seguidores._data['edges']))