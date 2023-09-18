num =int(input('Digite umnúmero inteiro:'))

if num < 0:
  print('Valor inválido!')
elif num == 0:
    print('O fatorial de 0 é 1.')
else:
    fatorial = 1

    for i in range(1, num + 1):
        fatorial *= i

    print(f'O fatorial de {num} é {fatorial}.')