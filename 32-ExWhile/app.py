"""
Iterando strings com while
"""

nome = "Gabriel Liz"
tam_Nome = len(nome)

print(nome)
print(tam_Nome)
print("---------")

nova_string = ""
contador = 0

while contador < tam_Nome:
    nova_string += nome[contador] + "*"
    contador += 1

print(nova_string)