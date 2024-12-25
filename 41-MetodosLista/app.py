# CRUD - criar, ler, alterar, apagar

lista = [1, 2, 3, 4]

# alterar valores
lista[0] = 10
print(lista)


# armazenar na variavel
numero = lista[2]
print(numero)


# apagar
del lista[2]
print(lista)
# se eu deleto um item do indice, todos os itens que estão depois vão ser movidos pra frente, pra substituir o indice apagado
# o que deixa o programa lento


# adicionar itens ao final da lista
# nao requer processamento
lista.append(34)
lista.append(72)
print(lista)


# remove o ultimo elemento da lista
# posso armazenar na variavel
# nao requer processamento
ultimoValor = lista.pop()
print(lista, ultimoValor)