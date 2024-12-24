"""
iteravel -> str, range, etc
  - tudo que posso navegar
  - você pode percorrer seus elementos um por um
  - possui um metodo chamado (__iter__)
  - exemplo: "texto".__iter__

iterador -> quem sabe entregar um valor por vez (__iter__)
que permite percorrer os elementos de uma coleção

next -> me entregue o proximo valor
iter -> me entregue o seu iterador
"""

# texto = "Gabriel".__iter__
texto = iter("Gabriel") # objeto iterador
# não é mais uma string
# agora isso é um iterador (entregador)

print(texto)

# vai entregar valor por valor
# print(texto.__next__()) 
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())

print(next(texto)) # chama o proximo valor
print(next(texto))
print(next(texto))
print(next(texto))

# quando esgota os valores, levanta um erro


texto1 = "Gabriel"
iterador = iter(texto1)

# como for trabalha por de baixo dos panos

# for letra in texto 

# texto -> iterador

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        # quando esgotar os valores -> vai lançar um erro StopIteration
        break

print("Acabou o programa")