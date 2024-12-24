texto = "Python"


# tamanhoTexto = len(texto)
# i = 0

# while i < tamanhoTexto:
#     print(texto[i])
#     i += 1


# nós utilizamos 'for' quando sabemos q vai terminar
# mais pratico de usar

# para cada letra em texto
# letra é uma variavel q eu mesmo crio
for letra in texto:
    print(letra)


novaString = ""

for letra in texto:
    novaString += f"*{letra}"

print(novaString)