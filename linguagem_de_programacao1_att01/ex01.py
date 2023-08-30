dias = int(input('Digite a quantidade de dias:'))
horas = int(input('Digite a quantidade de horas:'))
minutos = int(input('Digite a quantidade de minutos:'))
segundos = int(input('Digite a quantidade de segundos:'))

dias = dias * 86400
horas = horas * 3600
minutos = minutos * 60

print('O total em segundos é de: ', dias + horas + minutos + segundos)


