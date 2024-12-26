import os

listaCompras = []

while True:
    os.system("cls")
    print("Lista de Compras")
    print("1 - Adicionar Item")
    print("2 - Remover Item")
    print("3 - Listar Itens")
    op = input("Escolha uma opção: ")

    if op not in '123' or len(op) != 1:
        print("Opção inválida. Tente novamente.")
        os.system("pause")
        continue

    match op:
        case '1':
            os.system("cls")

            valor = input("Digite um item para adicionar: ")

            if valor in listaCompras or not valor:
                print("Erro ao adicionar")
                os.system("pause")
                continue
            
            listaCompras.append(valor)
            print("Item adicionado com sucesso!")
            os.system("pause")
            continue
            
        case '2':
            os.system("cls")

            indice = input("Digite o indice do item para remover: ")

            try:
                indice = int(indice)
                del listaCompras[indice]
                print("Item removido com sucesso")
            except:
                print("Erro ao remover")
            
            os.system("pause")
            continue

        case '3':
            os.system("cls")

            for indice, valor in enumerate(listaCompras):
                print(f'{indice} - {valor}')
            
            os.system("pause")
            continue
