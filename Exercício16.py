#Fazer um sistema de Agenda de contatos (Deve criar um dicionário com Nome, Telefone e Endereço, Imprimir os dados do dicionário, ser capaz de inserir e excluir um contato)

Agenda_Contatos = []
opcoes = ['1 - Criar um novo contato',
          '2-  Lista de contatos',
          '3 - Excluir contato']
#Looping infinito
while True: 
    print ('{:=^40}'.format(' AGENDA DE CONTATOS '))
    print ('Seleione uma das opções abaixo: ')
    option = int(input(f'{opcoes} '))
    #Criar novo contato
    if option == 1:
        nome = (input('Nome do contato: '))
        telefone = (input('Telefone do contato: '))
        endereco = (input('Endereço do contato: '))
        cont_Agenda = {'nome':nome, 'telefone': telefone, 'endereço': endereco}
        Agenda_Contatos.append(cont_Agenda)
    elif option == 2:
        print ('{:=^40}'.format(' IMPRESSÃO DOS CONTATOS '))
        print (Agenda_Contatos)
    elif option == 3:
        indice = 0
        for item in Agenda_Contatos:
            print (f'{indice} - {item}')
            indice = indice + 1
        #Seção do elemento ha ser excluído
        selector = input('Item a ser excluído: ')
        if selector.isnumeric():
            #converted recebe o valor da variavel 
            converted = int(selector)
        if converted in range(0, indice):
            selector = Agenda_Contatos.pop(converted)
            print ('Elemento {selector} excluído com sucesso')
        else: 
            print ('Opção inválida')
            break

    elif (option < 1 and option > 4): 
        print ('Opção inexistente ')
        break