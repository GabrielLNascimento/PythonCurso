"""
CONSTANTE -> "Variaveis" que não vão mudar
- São escritas de letras maiusculas

Muitas condições no mesmo if (ruim)
Muitos if's
Quanto mais longe da margem, mais complexo o código é

"""

velocidade = 70 # velocidade atual do carro
local_carro = 100 # local em que o carro está

RADAR = 60 # velocidade maxima
LOCAL = 100 # local onde está o radar
RADAR_RANGE = 1 # distancia onde o radar pega

velCarroPassouRadar = velocidade > RADAR
carroMultadoRadar = local_carro >= (LOCAL - RADAR_RANGE) and \
    local_carro <= (LOCAL + RADAR_RANGE)

if velCarroPassouRadar:
    print("Passou do radar")

if carroMultadoRadar and velCarroPassouRadar:
    print("carro multado")