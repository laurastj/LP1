
km = float(input('Digite a quantidade de quilometros percorridos:'))
dias = float(input('Digite a quantidade de dias pelos quais o carro foi alugado:'))

total = ((km * 0.25) + (dias * 65))

print(f'O preço final a pagar é de: R${total:.2f}')