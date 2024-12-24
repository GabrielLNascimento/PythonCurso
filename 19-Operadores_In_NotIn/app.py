# strings são iteraveis

# 0 1 2 3 4 5 6
# G A B R I E L

# in -> esta entre..
# not in -> não esta entre

nome = "Gabriel"

# print(nome[2]) # b

# b está dentro do nome?
print("b" in nome)

# z está dentro do nome?
print("z" in nome)

# z não esta dentro do nome?
print("z" not in nome)


nome = input("Digite o seu nome: ")
encontrar = input("Digite o que quer encontrar: ")

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
