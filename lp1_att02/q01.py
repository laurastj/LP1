num = int(input('Digite um número inteiro positivo:'))

if num < 2:
    if num == 2 or num %2 != 0:
        print(f'{num} é um número primo!')
    else:
        print(f'{num} Não é um número primo!')
else:
    print(f'{num} Não é um número primo!')
