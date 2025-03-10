'''
introduçao ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
'''


numero = input('Vou dobrar o numero que você digitar: ')

try:
    num_float =float(numero)
    print(f'O dobro de {numero} é {num_float *2}')
except:
    print('Isso não é um número')