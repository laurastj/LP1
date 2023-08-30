salario = float(input('Digite o valor do salário:'))
aumento = float(input('Digite a porcentagem do aumento:'))

print('O valor do aumento é de: R$', ((aumento / 100) * salario))
print('O valor do salário ficará de: R$', ((aumento / 100) * salario) + salario)
