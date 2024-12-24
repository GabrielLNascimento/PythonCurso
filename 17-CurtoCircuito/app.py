# avaliação de curto circuito

# and -> para na condição que for falsa
print(True and True and 0)

# or -> para na condição que for verdadeira
print(True or False)
print(0 or False or "" or "abc")

# se o usuario nao digitar nada, a variavel recebe o valor Sem senha
senha = input("Senha: ") or "Sem senha"
print(senha)