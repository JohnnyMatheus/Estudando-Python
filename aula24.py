#OPERADORES in e not in
#esta entre e não esta entre
##########################################################
# nome = 'johnny'

# print(nome[2])  #strings em python são iteraveis
# print(nome[-2])

# print('j' in nome)
# print('x' in nome)
# print('joh' in nome)

# #not in

# print('ohnn' not in nome)


# print('-'*40)
##########################################################

nome = input('Digite o nome do nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} esta em {nome}')

else:
    print(f'{encontrar} não esta em {nome}')

print('-'*40)
nome2 = 'joao joao'
if ' ' in nome:
    print(f'o nome contem espaços')
else:
    print('o nome não contém espaços')