#Fazer um sistema de biblioteca (Deve imprimir uma lista com 10 livros, pedir o nome do solicitante do empréstimo, pedir para selecionar um livro e imprimir o livro selecionado)
#importação de tempo
print (' BIBLIOTECA ')
name = input('Nome: ')
print('Escolha uma das opções abaixo')
print ('''1) Educação, Pobreza e Desigualdade Social: A Escola e o Direito à Educação
2) Gênero e desigualdades: Limites da democracia no Brasil
3) Aprenda A PROGRAMAR: A Arte de Ensinar O Computador
4) Algoritmos e Programação
5) Crimes Modernos: O Impacto da Tecnologia no Direito
6) Tecnologias para Transformar a Educação
7) Manifesto Comunista
8) Treinamento em Lógica de Programação
9) A tirania do mérito: O que aconteceu com o bem comum? 
10) Desigualdade & caminhos para uma sociedade mais justa
       ''')
opção = int(input('Sua escolha: '))
if opção > 10:
    print (f'{name} você não escolheu a opção correta... Tente novamente')
else: 
    print (f'{name} você escolheu o {opção}° livro') 