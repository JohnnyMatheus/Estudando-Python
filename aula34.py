"""
Repetições
while(enquanto)
Executa uma ação enquanto uma condição for verdadeira
"""

'''LOOP INFINITO'''
# condicao = True

# while (condicao):
#   nome = input('Nome: ')
#   print(f'seu nome é {nome}')


condicao = True

while (condicao):
  nome = input('Nome: ')
  print(f'seu nome é {nome}')
  if nome == 'sair':
    break
print('acabou')  