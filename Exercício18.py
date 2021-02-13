#Fazer um sistema de compras (Deve mostrar um dicionário com os objetos (Nome, Preço e Cor), pedir o nome do usuário e fazer com o que o usuário selecione um objeto e imprimir a compra na tela)

Agenda_Itens = []
Agenda_Compras = []
option = ['1 - Incluir Itens',
          '2 - Lista De Itens',
          '3 - Realizar Compras',
          '4 - Listar Compras']
while True: 
    print (option)
    opt = int(input('Escolha uma opção: '))
    if opt == 1: 
        print ('{:=^40}'.format(' INCLUSÃO DE ITENS '))
        nome = input('Nome do Item: ')
        cor = input('Cor do item: ')
        valor = float(input('Preço do Item: R$'))
        ItensDict = {'Item': nome, 'Cor':cor, 'Valor':valor}
        Agenda_Itens.append(ItensDict)
        print ('Item Adicionado com sucesso!')
    if opt == 2:
        print ('{:=^40}'.format(' LISTA DE ITENS ADICIONADOS '))
        print (Agenda_Itens)
    if opt == 3:
        print ('{:=^40}'.format(' REALIZAÇÃO DE COMPRAS '))
        i = 0
        for item in Agenda_Itens:
            print (f'{i} - item')
            i = i + 1
        Select_Item = input('Escolha o item que deseja comprar: ')
        if Select_Item.isnumeric():
            converted = item(Select_Item)
            converted = int(Select_Item)
        if converted in range(0, i):
            Shopping = {'Compra': Agenda_Itens[converted]}
            Agenda_Compras.append(Shopping)
            print ('Sua compra foi realizada com sucesso!')
        
        else: 
            print ('Opção inválida')
    if opt == 4:
        print ('{:=^40}'.format('Lista de compras realizadas'))
        print (Agenda_Compras)
    elif (opt < 1 and opt > 4): 
        print ('Opção inválida')