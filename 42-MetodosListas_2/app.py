lista = [10, 20, 30, 40, 50, 60]

# Limpar a lista
# lista.clear()
print(lista)


# adicionar um item no indice escolhido
# insert(indice, valor)
lista.insert(0, "Ola")
# todos os items foram movidos para frente
print(lista)


# inserir no indice que nao existe
lista.insert(99, "teste")
# nao leva em consideração o indice, apenas adiciona no final
print(lista)
