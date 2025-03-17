#Introducao ao for/in

#ex com while de iterar
# texto='Python s2'
# i=0

# while i < len(texto):
#     print(texto[i],i)
#     i+=1


# senha_salva = '123456'

# senha_digitada = ''
# repeticoes =0

# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Sua senha ({repeticoes})X:')
#     repeticoes+=1


# print(repeticoes)
###############################################################

#Exemplo com for
texto = 'Python'
novo_texto =''
i=0
for letra in texto: #para cada letra em texto exiba a letra na tela
    novo_texto += f'*{letra}'
    print(letra,i)
    i+=1
print(novo_texto + '*')



