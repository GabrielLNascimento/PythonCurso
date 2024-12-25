listaA = [10, 20, 30]
listaB = [40, 50, 60]

# concatenar
listaC = listaA + listaB
print(listaC)

# extendendo a lista
listaD = listaA.extend(listaB) 
# nao retorna nada (None), mas executa uma ação
# o metodo extends, trabalha na listaA
print(listaD)
print(listaA)