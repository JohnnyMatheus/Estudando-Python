"""
Qual palavra aparece mais vezes na frase
iterando strings com while
"""

frase = 'O Python é uma linguagem de programação'\
'multiparadgma'\
'python foi criado por Guido van Rossun'.lower()


i = 0
qtd_apareceu_mais_vezes= 0
letra_apareceu_mais_vezes=''
while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i+=1
        continue
       
        
    qtd_atual =  frase.count(letra_atual)
    
    if qtd_apareceu_mais_vezes < qtd_atual:
        qtd_apareceu_mais_vezes = qtd_atual
        letra_apareceu_mais_vezes = letra_atual
   
    i+=1
    

print('A LETRA QUE APARECEU MAIS VEZES FOI '
      f'"{letra_apareceu_mais_vezes}" que apareceu '
      f'{qtd_apareceu_mais_vezes}x')
