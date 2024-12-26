# enumerate => enumera iteraveis (indices)

nomes = ['Gabriel', 'Emilly', 'Zanela', 'João']

# for i in enumerate(nomes):
    # desempacotamento
    # indice, valor = i
    # print(i) # tupla
    
for indice, valor in enumerate(nomes):
    print(indice, valor)


# converter para uma lista
listaEnumerada = list(enumerate(nomes))
# consigo ver os valores
print(listaEnumerada)