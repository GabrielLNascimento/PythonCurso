"""
repetições
while (enquanto)
executa um escopo de código enquanto uma condição for verdadeira

while (True):
    // codigo //

cuidado com loop infinito:
- uma logica que nunca vai ser falsa, sempre vai ser true

podemos criar uma logica para poder quebrar o loop

"""

# condicao = True
# vai executar até ser falso
# while condicao:
#     nome = input("Qual o seu nome: ")
#     print(nome)



# while True:
#     ...
# # nao vai ser executado esse print
# print("Acabou")


# Contador de 0 até 10
contador = 0

while contador < 10:
    
    # logica para aumentar o contador
    contador = contador + 1
    print(contador)

    # quando a condicao for False, ela para de executar o loop

print("Fim do programa")