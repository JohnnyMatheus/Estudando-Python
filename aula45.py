"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

# texto =  'JOHNNY'
# numeros = range(0,100,8)
# for numero in numeros:
#     print(numero)

# texto =  'JOHNNY'.__iter__()
# print(texto)
# #ou assim
# texto =  iter('JOHNNY')
# print(texto)

##################################################################################


# texto = iter('Johnny') #__iter__()
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# #ou assim
# texto2 =iter('MEDEIRO')
# print(next(texto2))
# print(next(texto2))
# print(next(texto2))
# print(next(texto2))
# print(next(texto2))
# print(next(texto2))
# print(next(texto2))


#################################################################################

mensagem = 'Ciência' #iterável
iterador = iter(mensagem) #iterator
while True:
    try:
        print(next(iterador))
    except StopIteration:
        break