string = "Valor qualquer"

i = 0
while i < len(string):
    letra = string[i]

    print(letra)
    i += 1
else:
    # vai ser executado quando sair do loop
    # se der break, o else nao vai ser executado
    print("O else foi executado")

print("fora do while")