nomeUser = input("Digite o seu nome: ")
tamNome = len(nomeUser)

curto = tamNome >= 0 and tamNome <= 4
medio = tamNome >= 5 and tamNome <= 6

if curto:
    print("Seu nome é muito curto")
elif medio:
    print("Seu nome é normal")
else:
    print("Seu nome é grande")