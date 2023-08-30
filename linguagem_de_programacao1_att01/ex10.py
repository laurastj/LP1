while True:
    print('MENU:')
    print('1. Adição')
    print('2. Subtração')
    print('3. Multiplicação')
    print('4. Divisão')
    print('5. SAIR')



    opcao = input('Escolha uma das 5 opções:')

    if opcao == '5':
        print('Saindo do programa.')
        break

    numero = int(input('Digite o número para ver a tabuada:'))

    if opcao == '1':
        for i in range (0, 11):
            print(f'{numero} + {i} = {numero + i}')

    elif opcao == '2':
        for i in range (0, 11):
            print(f'{numero} - {i} = {numero - i}')
    elif opcao == '3':
        for i in range (0, 11):
            print(f'{numero} * {i} = {numero * i}')
    elif opcao == '4':
        for i in range (0, 11):
            if i != 0:
             print(f'{numero} / {i} = {numero / i}')

