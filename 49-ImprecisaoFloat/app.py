import decimal

num1 = 0.1
num2 = 0.7

res = num1 + num2

print(res)

# formas de contornar esse problema

print(f"{res:.1f}") # arredondando para uma casas decimais
print(round(res, 1)) # metodo dentro do python

n1 = decimal.Decimal('0.1')
n2 = decimal.Decimal('0.7')
print(n1 + n2)