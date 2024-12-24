"""
interpolação de strings
s - string
d e i - int
f - float
x e X - hexadecimal
"""

nome = "Gabriel"
preco = 1000.9123456

variavel = "%s, o preço total foi R$:%.2f" % (nome, preco)

print(variavel)

print("O hexadecimal de %d é %04x" % (23, 23))