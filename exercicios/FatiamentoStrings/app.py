nomeUser = input("Digite o seu nome: ")
idadeUser = input("Digite a sua idade: ")

if nomeUser and idadeUser:
    print(f'Seu nome é: {nomeUser}')
    print(f'Seu nome invertido é: {nomeUser[::-1]}')
    print(f'Seu nome contem espaços: {" " in nomeUser}')
    print(f"Seu nome tem {len(nomeUser)} letras")
    print(f"A priemira letra do seu nome: {nomeUser[0]}")
    print(f"A utlima letra do seu nome: {nomeUser[-1]}")
else:
    print("Digite algo")