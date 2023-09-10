valor_inicial = float(input('Digite o valor inicial da dívida:'))
juro_mensal = float(input('Digite o juro mensal (em porcentagem):'))
valor_mensal = float(input('Digite o valor mensal a ser pago:'))

meses = valor_inicial / valor_mensal
juros = meses * ((juro_mensal/100) * valor_inicial)
total = juros + valor_inicial

print(f'A divida será paga em {meses:.1f} meses')
print(f'O total a ser pago será: R${total:.2f}')
print(f'Total de juros: R${juros:.2f}')
