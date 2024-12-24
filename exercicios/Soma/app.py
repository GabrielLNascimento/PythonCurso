n1 = input("Digite o primeiro número: ")
n2 = input("Digite o segundo número: ")

try:
    n1 = int(n1)
    n2 = int(n2)
    print(n1 + n2)
except:
    print("Isto não é um erro")

