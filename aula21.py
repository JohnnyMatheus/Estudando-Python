#OPERADORES LÓGICOS 
#and / or /not

#AND
entrada = input('[E]ntrar [S]air: ')
senha = input('Senha: ')
senha_permitida = '123'

if entrada == 'E' and senha == senha_permitida:
    print('Entrou')
else:
    print('Sair')    