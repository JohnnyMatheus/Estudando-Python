#interpolação básica entre strings
# s - string
# d e i - int
# f - float
# x e X - Hexadecimal

nome = 'Johnny'
preco = 1000.95897643
variavel =  '%s, o preco total foi %.2f' %(nome, preco)
print(variavel)

#NÚMERO HEXADECIMAL
numero =15
numero2 = 1500
print('O número: %d em hexadecimal é %x' %(numero,numero))

print('O número: %d em hexadecimal é %X' %(numero,numero))

print('O número: %d em hexadecimal é %04x' %(numero,numero))

print('O número: %d em hexadecimal é %x' %(numero2,numero2))