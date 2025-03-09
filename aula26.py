'''
Formatação básica de strings

s - string
d - int
f - float
.<número de dígitos>f
x ou X - hexadecimal
(Caractere) (><^)(quantidade)
> - esquerda
< - direita
^ - centro
Sinal + ou -
ex: 0>-100, 1.f
conversion flags - !r !s !a  
'''

variavel =  'ABC'
print(f'{variavel: >10}') #preencher para a esquerda
print(f'{variavel: <10}.') #preencher para a direita
print(f'{variavel: ^10}')
print(f'{1000.4879349859:.1f}')
print(f'{1000.4879349859:,.1f}')
print(f'{1000.4879349859:-.1f}')
print(f'{1000.4879349859:+,.1f}')
print(f'O hexadecimal de 1500 é {1500:08x}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')