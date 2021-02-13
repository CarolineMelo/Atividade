#Fazer um sistema de Loteria (Deve pedir o nome do usuário, pedir um número e comparar com um conjunto aleatório de número (de 0 a 100) e dizer se o usuário advinhou)

from random import randint
comp = randint(0,100)
num = int(input('Digite um número de 1 a 100: '))
if num == comp:
    print('Você acertou!{}'.format(num))
else:
    print('Você errou! O número digitado foi {} e o número sortiado foi{}'.format(num,comp))
