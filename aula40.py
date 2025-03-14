"""CALCULADORA COM while"""

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')
    numeros_validos = None
    num1_float = 0
    num2_float = 0

    try:
        num1_float = float(numero_1)
        num2_float = float(numero_2)
        numeros_validos = True
    except:
         numeros_validos = None
    
    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'
    if operador not in operadores_permitidos:
        print('Operador inválido')
        continue

    if len(operador)>1:
        print('Digite apenas um operador.')
        continue

    if operador == '+':
        print(f'{num1_float} + {num2_float} = ',num1_float+num2_float)
    elif operador == '-':
        print(f'{num1_float} - {num2_float} = ',num1_float-num2_float)
    elif operador == '/':
        print(f'{num1_float} / {num2_float} = ',num1_float/num2_float)
    elif operador == '*':
        print(f'{num1_float} * {num2_float} = ',num1_float*num2_float)

    

    sair = input('Deseja sair? [s]im: ').lower().startswith('s')
    if sair is True:
        break