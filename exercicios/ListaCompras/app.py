import os

listaCompras = []

while True:
    os.system("cls")

    print("------ Lista de Compras ------")
    print("1 - Ver a lista")
    print("2 - Adicionar item na lista")
    print("3 - Remover item na lista")
    op = input("Digite uma opção: ")

    if op not in '123' and len(op) == 1:
        print("Opção inválida. Tente novamente.")
        continue

    match op:
        case '1':
            os.system("cls")
            print("Lista Atual:")
            
            for indice, valor in enumerate(listaCompras):
                print(f"{indice} - {valor}")

            print(" ")
            os.system("pause")
        
        case '2':
            os.system("cls")
            valor = input("Digite um item para adicionar na lista: ")

            if valor in listaCompras or valor == "":
                print("Item inválido...")
                continue
            
            listaCompras.append(valor)
            
            print(" ")
            print("Item adicionado com sucesso!")
            print(" ")
            os.system("pause")
        
        case '3':
            os.system("cls")
            item = input("Digite o indice do item: ")

            try:
                ind = int(item)
                del listaCompras[ind - 1] 

                print(" ")
                print("Item removido com sucesso")
                print(" ")
                os.system("pause")
            except:
                print("Erro ao apagar o indice da lista")
                os.system("pause")

                
                