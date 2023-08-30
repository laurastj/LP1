numero1 = int(input('Digite o primeiro número:'))
numero2 = int(input('Digite o segundo número:'))

resto = numero1

while resto >= numero2:
    resto -= numero2

print('O resto da divisão é:', resto)
