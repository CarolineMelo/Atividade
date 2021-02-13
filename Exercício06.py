# Algoritmo para criar uma lista usando range com 100 elementos e imprimi-la
lista = list()
for c in range (1,101):
        lista.append(int(input(f'{c}° Elemento: ')))
        print('Os elementos digitados foram'.format(lista))                