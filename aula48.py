"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#VIDEO AULA 81 -103
# append adiciona e pop remove 
lista = [10,20,30,40]

lista.append(50)
lista.append(60)
lista.append(70)
lista.append(80)
lista.append(90)
lista.pop()
lista.append(100)
del lista[-1]
#lista.clear()

lista.insert(0,'Johnny')
print(lista)
