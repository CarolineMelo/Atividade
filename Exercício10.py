#Fazer uma busca sequencial em uma lista (Criar uma tupla [0....20] e pedir para o usuário fazer uma busca)
lista = (1, 30, 20, 44, 999, 89, 34, 59, 98, 100, 12, 14, 33, 44, 55, 66, 77, 68, 41, 2)
user = int(input('Digite um valor inteiro: '))
if user == lista: 
    print (f'O valor {user} corresponde ao valor dentro da lista')
else: 
    print ('O valor digitado não está dentro da lista...')