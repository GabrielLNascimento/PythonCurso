contador = 0

while contador <= 10:
    contador += 1
    
    if contador == 4:
        print("Nao vou mostrar o 4")
        continue
    
    # nao vai mostrar o 4, ele vai pular esse loop
    print(contador)

