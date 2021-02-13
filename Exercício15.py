#Fazer um sistema de Feira Livre(Deve imprimir uma lista com as frutas e pedir para o solicitante colocar o nome e selecionar a fruta e depois deve imprimir o nome do solicitante e a fruta)
print (' Feira livre ')
nome = input('Nome: ')
#seção de escolha
print ('{:=^40}'.format(' OPÇÕES DE FRUTAS '))
print('''1. Açaí
2. Pitaia
3. Buriti
4) Bacuri
5) Ciriguela
6) Durião
7) Jambolão
8) Cambuci
9) Lobeira
10) Umbu ''')
option = int(input('Digite o número da fruta escolhida: '))
if option > 10: 
    print (f'{nome} Temos 10 opções de frutas disponíveis.')
else: 
    print (f'{nome} Sua escolha é a {option}° fruta.')