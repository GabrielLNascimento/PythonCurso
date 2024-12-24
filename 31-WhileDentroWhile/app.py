qtd_linha = 5
qtd_coluna = 5

linha = 1

while linha <= qtd_linha:
    
    # tenho que definir a coluna dentro do loop da linha
    # pois toda vez que reiniciar o loop da linha, eu reseto a variavel coluna
    coluna = 1

    while coluna <= qtd_coluna:    
        print(linha, coluna)
        coluna += 1
    
    linha += 1
    
    print("-" * 15)

print('Acabou')