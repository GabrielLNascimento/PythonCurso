"""
interpolação de strings
s - string
d e i - int
f - float
x e X - hexadecimal
"""

# .<numero de digitos>f -> casas decimais

"""
(caractere)(><^)(quantidade)
> - esquerda
< - direita
^ - centro

Ex: 0>-100,.1f
"""

variavel = "ABC"
numero = 1000.8281873217321
print(f".{variavel: >10}.")
print(f".{variavel: <10}.")
print(f".{variavel: ^10}.")

print(f"{numero:.2f}") # casas decimais
print(f"{numero:,.2f}") # virgula como separador
print(f"{numero:+,.2f}") # mostrando positivo

print(f"{numero:0>10,.2f}") # preencher com zeros