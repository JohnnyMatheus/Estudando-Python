'''
iterando strings com while
'''

nome = 'Johnny Matheus'
novo_nome = ''

indice =0
while indice < len(nome):
    letra=(nome[indice])
    novo_nome += f'*{letra}'
    indice+=1
novo_nome +='*'
print(novo_nome)