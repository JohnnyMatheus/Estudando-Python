"""
 Faça um programa que peça ao usuário para digitar um número inteiro,
 informe se este número é par ou ímpar. Caso o usuário não digite um número
 inteiro, informe que não é um número inteiro.
"""

try:
    numero = int(input('Digite um número: '))
    if numero %2 == 0:
        print('É PAR')
    else: 
        print('É IMPAR')
except ValueError:
        print('Não é um número inteiro')

 
"""
 Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
 descrito, exiba a saudação apropriada. Ex. 
 Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
try:
    hora = int(input('Que horas são: '))
    if hora >=0 and hora <=11:
        print(' Bom dia 0-11')
    elif hora >=12 and hora <=17:   
        print('Boa tarde 12-17') 
    else:
        print(' Boa noite 18-23.')
except:
    print('Valor invalido')



"""
 Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
 menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
 "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

try:
    nome = input('Informe seu primeiro nome ')
    if len(nome) <= 4:
        print('Seu nome é curto')
    elif len(nome) >= 5 and len(nome) <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
except:
    print('Valor inválido')        