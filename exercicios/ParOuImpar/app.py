numUser = input("Digite um número: ")

try:
    numUser = int(numUser)
    print("Par" if numUser % 2 == 0 else "Impar")
except:
    print("Digite um número válido")