frase = "Ola a todos, sejam bem vindos ao meu codigo de python"

# qual a letra que apareceu mais vezes?

tamString = len(frase)
contador = 0

maisApareceu = ""
maisApareceuQuantidade = 0

while contador < tamString:
    letra = frase[contador]
    quantidade = frase.count(letra)

    # print(letra, quantidade)

    if letra == " ":
        contador += 1
        continue

    if quantidade > maisApareceuQuantidade:
        maisApareceuQuantidade = quantidade
        maisApareceu = letra
    
    contador += 1

print(maisApareceu, maisApareceuQuantidade)
