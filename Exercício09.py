#Elabore um algoritmo em Python que calcule a área e o perímetro de um círculo, sabendo que A = πr² e P=2πr.

from math import radians,pi
raio = float(input('Digite o raio do círculo em metros: '))
area = pi*(raio**2)
print ( 'A área do círculo é {}'.format(raio))
perimetro = 2*(pi*(raio**2))
print('O perimetro do círculo é {}'.format(perimetro))