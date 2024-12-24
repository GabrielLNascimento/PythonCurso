"""
try -> tentar executar um código
except -> ocorreu um erro ao tentar executar
"""

print(123)
print(456)
# int('a') -> erro


numero = input("Digite um número: ")

# numero_int = int(numero)
# print(numero_int * 2)

# se der erro, cai direto pro except
try:
    numero_int = int(numero)
    print(numero_int * 2)
except:
    print("Isso não é um numero")