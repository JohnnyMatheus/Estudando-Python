#OPERADORES LÓGICOS 
#and / or /not

# OR
entrada = input('[E]ntrar [S]air: ')
senha = input('Senha: ')
senha_permitida = '123'

if entrada == 'E' or entrada =='e' and senha == senha_permitida:
    print('Entrou')
else:
    print('Sair')    



if (entrada == 'E' or entrada =='e') and senha == senha_permitida: 
    print('Entrou')
else:
    print('Sair')    

print('eu sou um teste', 0 or 'abc')

#Avaliação de curto circuito
print(0 or False or 0 or 'abc' or True) #a primeira vez que ele achar um valor vedadeiro ele retorna o valor no caso abc