num = int(input('Digite um número inteiro:'))

if num ==int(str(num)[::-1]):
    print(f'O número {num} é um palíndromo!')
else:
    print(f'O número {num} NÃO é um palíndromo!')