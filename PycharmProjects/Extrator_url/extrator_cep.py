import re # Regular Expression -- RegEx

endereco = "Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

# 5 digitos + hifen (opciona) + 3 digitos

padrao = re.compile("[0-9]{5}[-]?[0-9]{3}")
busca = padrao.search(endereco)  # Match

if busca:
    cep = busca.group()
    print(cep)


nome = "Rafaela Brasil, CPF: 718.457.190-85"
padraoCPF = re.compile("[0-9]{3}[.][0-9]{3}[.][0-9]{3}[-][0-9]{2}")
buscaCPF = padraoCPF.search(nome)
CPF = buscaCPF.group()
print(CPF)

