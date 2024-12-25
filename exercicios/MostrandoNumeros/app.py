numeros = []

while True:
    num = input("Digite um numero: ")

    if num not in numeros:
        numeros.append(num)
    
    if num == '-1':
        break

print(numeros)