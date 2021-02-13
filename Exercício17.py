#Fazer um sistema de Agenda de revisão do Carro (Deve pedir o nome do carro, ano e modelo, nome do proprietário, data e hora da revisão. Depois deve guardar os dados em um dicionário e mostrar a lista de dicionários (agendamentos) na tela)

Agendamento_Carros = []
opcoes = ['1 - Agendar Revisão ',
          '2 - Listas de agendamentos', 
          '3 - Sair']
while True: 
    print (opcoes)
    opção = int(input('Escolha uma opção: '))
    if opção == 1:
        print ('{:=^40}'.format(' AGENDAMENTO DE REVISÃO '))
        
        nome = input('Nome do carro: ')
        model = int(input('Ano do carro: '))
        proprietario = input('Nome do(a) proprietário(a): ')
        dia = int(input('Dia do agendamento: '))
        hora = int(input('Horario para a revisão: '))
        
        lista_agendamentos = {'Proprietário': proprietario, 'Veículo': nome, 'Ano/Modelo': model, 'Horario': hora, 'Data': dia}
        Agendamento_Carros.append(lista_agendamentos)
        print ('Seu agendamento foi realizado com sucesso!')
    elif opção == 2:
        print ('{:=^40}'.format(' LISTAS DE AGENDAMENTOS '))
        print (Agendamento_Carros)
    elif opção == 3:
        print ('Encerrando o programa')
       
        break
    #valor > 3
    else: 
        print ('Opção inexistente')
        
