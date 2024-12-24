"""
Flag -> Bandeiras - marcar um local

preciso saber se o interpretador passou no if ou não

is ou not is -> é ou nao é
utilizo (valor, tipo ou identidade)
"""

condicao = False

# define a variavel fora do if, ela passa a valer true quando passar pelo if de fato
passou_if = None

if condicao:
    passou_if = True
    print("Faça algo")
else:
    print("Não faça algo")

print(passou_if, passou_if is None)
print(passou_if, passou_if is not None)


if passou_if is None:
    print("Não passou no if")

if passou_if is not None:
    print("Passou no if")