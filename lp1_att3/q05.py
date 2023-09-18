valor_casa = float(input('Digite o valor da casa a ser comprada:'))
salario = float(input('Digite o salário:'))
anos = float(input('Digite a quantidade de anos a pagar:'))

prestacao = valor_casa / (anos * 12)

if prestacao > (0.3 * salario):
    print('Empréstimo NÃO Aprovado!')
else:
    print('Empréstimo Aprovado!')