""" calculadora com while """

while True:
    sair = input("Quer sair? [s]air: ")

    if sair.lower() == 's':
        print("Fim do programa")
        break
    
    num1 = input("Número 1: ")
    num2 = input("Número 2: ")
    op = input("Sinal: ")

    if not num1.isdigit() or not num2.isdigit():
        print("Digite números válidos!")
        continue
    
    num1 = int(num1)
    num2 = int(num2)

    match op:
        case "+":
            print(f"Soma: {num1 + num2}")
        case "-":
            print(f"Subtração: {num1 - num2}")
        case "*":
            print(f"Multiplicação: {num1 * num2}")
        case "/":
            if num2 == 0:
                print("Não é possível dividir por zero!")
                continue
            else:
                print(f"Divisão: {num1 / num2}")

    

print("Fim do programa")