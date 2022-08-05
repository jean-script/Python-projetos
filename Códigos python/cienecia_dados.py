import numpy as np
import matplotlib.pyplot as plt
 
grupos = 5
anterior = (30, 20, 18, 17, 15)
atual = (40, 20, 20, 10, 10)
 
index = np.arange(grupos)
bar_width = 0.3
 
barras1 = plt.barh(index, anterior,bar_width,color='r',label='10-10-2018')
 
barras2 = plt.barh(index + bar_width, atual, bar_width,color='b',label='17-10-2018')
 
plt.ylabel('Candidato')
plt.xlabel('Percentual')
plt.title('Pesquisa Eleitoral')
plt.yticks(index + bar_width, ('Leonardo', 'Maria', 'Ana', 'Outros', 'Indecisos'))
plt.legend()
plt.show()
plt.legend()
plt.show()