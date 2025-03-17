"""while/else"""
string = 'Johnny'

i=0
while i < len(string):
    letra = string[i]
    if ' ' in letra:
        break
    print(letra)

    i+=1
else:
    print('Não contém espaços')