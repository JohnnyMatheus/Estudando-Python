#exercício de relacionais = comparação
primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor=} é maior do que o {segundo_valor=}')
elif primeiro_valor == segundo_valor:  
     print('são iguais') 
else:
     print(f'{segundo_valor=} é maior do que o {primeiro_valor=}')