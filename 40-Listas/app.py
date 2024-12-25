"""
listas em python
tipo 'list' -> mutável
suporta valores de qualquer tipo
listas também possui indices e fatiamentos
"""

# indice  01234
string = "ABCDE" # cadeia de caracteres

# acessando elementos pelo indice
# print(string[2])


# escrever de duas formas
# lista = list('ola')
# print(lista)

# utiliza colchetes
lista = [] # lista vazia, como uma string vazia

print(lista, type(lista), bool(lista))



# colocando valores dentro da lista (qualquer tipo)
lista = [123, True, "Gabrie Liz", 2.4, []]
print(lista)


# acessando valores por indice
# estou acessando items, e nao caractere
print(lista[2], type(lista[2]))


# trocando valores
lista[2] = "FUI ALTERADO"
print(lista)