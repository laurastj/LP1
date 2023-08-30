numero1 = float(input('Digite o primeiro número:'))
numero2 = float(input('Digite o segundo número:'))
operacao = str(input('Digite qual operação deve ser realizada soma (+), subtração (-), multiplicação (*) ou divisão (/):'))

if operacao == '+':
    print(f'A soma dos números é: ', numero1 + numero2)
elif operacao == '-':
    print(f'A subtração dos é:  ', numero1 - numero2)
elif operacao == '*':
    print(f'A multiplicação dos números é: ', numero1 * numero2)
elif operacao == '/':
    print(f'A divisão dos números é: ', numero1 / numero2)
else:
    print('Operação inválida!')
