"""
Variaveis, constantes e complexidade de codigo
CONSTANTE = 'Variáveis que não vão mudar' letra maiuscula
"""

velocidade = 62
local_carro = 100

RADAR_1 =61     # VELOCIDADE MAXIMA DO RADAR
LOCAL_1 = 100   # LOCAL ONDE O RADAR 1 ESTÁ
RADAR_RANGE = 1 # A distancia onde o radar pega

vel_carro_passou_radar_1 = velocidade >RADAR_1
carro_multado_radar_1 = local_carro >=(LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)


if vel_carro_passou_radar_1:
    print('velocidade carro passou do radar 1')
if  carro_multado_radar_1 and vel_carro_passou_radar_1:
    print('Carro multado radar 1')