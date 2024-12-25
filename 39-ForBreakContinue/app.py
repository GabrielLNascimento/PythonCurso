for i in range(0, 10):


    if i == 2:
        print("Pulando o 2")
        continue

    if i == 8:
        print("parando no 8")
        break

    for j in range(1, 3):
        print(i, j)
else:
    print("For completo com sucesso")