preco = float(input('Digite o valor da mercadoria:'))
percent = float(input('Digite o valor do desconto (em porcentagem):'))


desconto = (percent/100) * preco


print(f'O valor do desconto é: R${desconto:.2f}')
print(f'O preço a pagar é: R${(preco - desconto):.2f}')