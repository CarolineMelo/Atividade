#Fazer um cadastro de viagem (Deve pedir o nome do viajante, dar as opções de destino e imprimir a selecionada)
print (' AEROPORTO INTERNACIONAL ')
#leitura de nome
name = str(input('Nome: '))
print (' OPÇÕES DE DESTINO ')
print(''' Canadá
Colômbia
México
Peru
Chile
Argentina
Uruguai
Costa do Marfim	
Costa Rica
Croácia
Holanda''')
opções = input(f'{name} ,qual será o seu destino? ')
print (f'{name} o seu destino será {opções}') 