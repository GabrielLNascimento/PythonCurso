# aponto para o mesmo valor na memória
# mas possui ids diferentes

listaA = [1, 2, 3]
listaB = listaA


# vai alterar nas duas listas
# por que aponta para o mesmo valor na memória
listaA[0] = 99

print(listaA, listaB)


# copiando valores
# nao vai ser afetada, se alterar os valores da lista A
listaC = listaA.copy()
print(listaC)