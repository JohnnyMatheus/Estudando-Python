#formatação de Strings com format

a = 'A'
b = 'B'
c = 1.1
formato = 'a={} b={} c={:.2f}'.format(a,b,c)
print(formato)

formato2 = 'a={1} b={0} c={2:.2f}'.format(a,b,c) #indices
print(formato2)
print('-'*30)

#Parametro nomeado
string = 'a={nome1} b={nome2} c={nome3:.2f}'
formato3 = string.format(
    nome1 = a,
    nome2 = b,
    nome3 = c
)
print(formato3)

print('_' *40)

nome = 'teste'
idade = 10
formato = '{1} tem {0} anos'
print(formato.format(nome,idade))

x = 10
print(f'{x:.2f}')