palavraSecreta = "gabriel"
letras_acertadas = ''

while True:
    letra = input("Digite uma letra: ")

    if len(letra) > 1:
        print("Digite apenas uma letra")
        continue

    if letra in palavraSecreta:
        letras_acertadas += letra
    
    palavraFormada = ""

    for letraSecreta in palavraSecreta:
        if letraSecreta in letras_acertadas:
            palavraFormada += letraSecreta
        else:
            palavraFormada += "-"
    
    print(palavraFormada)