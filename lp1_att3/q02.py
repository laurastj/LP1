peso = float(input('Digite o seu peso (em kg):'))
altura = float(input('Digite sua altura (em metros):'))

imc = peso / (altura*altura)

if imc <= 18.5:
    print('Abaixo do peso ideal!')
elif imc > 18.5 and imc < 25:
    print('Peso ideal!')
elif imc >= 25 and imc < 30:
    print('Excesso de peso!')
elif imc >= 30 and imc < 35:
    print('Obesidade!')
elif imc > 35:
    print('Obesidade extrema!')
