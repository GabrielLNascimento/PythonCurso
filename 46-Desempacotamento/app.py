nomes = ["Gabriel", "Emilly", "Zanela"]

# tem que ter a mesma quantidade do tamanho da lista
nome1, nome2, nome3 = nomes
print(nome1 ,nome2, nome3)

# nome4, nome5 = nomes -> erro, muitos valores para desempacotar

# nome4, nome5, nome6, nome7 = nomes -> erro, poucos valores para desempacotar


# pegar somente o primeiro nome
# utiliza "*" para pegar o resto da lista
nome1, *resto = nomes
print(nome1)
print(resto)

# quando nao vou utilizar variavel, eu escrevo "_"
# nome1, *_ = nomes


# pegar o segundo valor
_, nome2, *_ = nomes
print(nome2) 