#Identidade do valor que esta na memoria

"""
Flag (Bandeira) -Marcar um local
None = não valor
is e is not = é ou não é (tipo, valor,identidade)
id = identidade
"""

v1 ='a'
v2 ='a'

print(id(v1))
print(id(v2))

condicao = False
passou_no_if =None

if condicao:
    passou_no_if =True
    print('Faça algo')
else:
    print('Não Faça algo')
    