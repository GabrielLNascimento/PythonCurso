hora = input("Digite as horas: ")

if not hora.isdigit():
    print("Digite um número válido")
else:
    hora = int(hora)

    if hora <= 11:
        print("Bom dia")
    elif hora <= 17:
        print("Boa tarde")
    elif hora <= 23:
        print("Boa noite")
    else:
        print("Hora inválida")
    
