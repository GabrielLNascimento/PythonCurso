"""
split -> divide a string e coloca em arrays
strip -> tira os espaços em branco em volta da string
join -> une uma string
"""

frase = "Ola, tudo bem com voce?"

# ele usa espaços em branco para dividir
# listaPalavras = frase.split()

listaPalavras = frase.split(",") #  separo onde estiver virgula + espaço



listaFrases = []
for i, frase in enumerate(listaPalavras):
    # print(listaPalavras[i].strip())

    # vou alterar a propria lista
    # listaPalavras[i] = listaPalavras[i].strip()
    # metodo ruim

    listaFrases.append(listaPalavras[i].strip())

print(listaPalavras)
print(listaFrases)

# "" -> é o separador da string

# frasesUnidas = "-".join('abc')
# para cada item eu tenho um '-'

frasesUnidas = ', '.join(listaFrases)
print(frasesUnidas)