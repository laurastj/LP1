quantidade_num = 0
soma = 0

while True:
    num = int(input('Digite um número inteiro:'))

    if num == 0:
        break

    quantidade_num += 1
    soma += num

if quantidade_num > 0:
    media = soma / quantidade_num
else:
    media = 0

print(f'A quantidade de números digitados: {quantidade_num}')
print(f'Soma dos números: {soma}')
print(f'Média aritmética: {media}')