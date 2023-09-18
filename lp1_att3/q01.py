lista = input('Digite uma lista de números inteiros (separados com espaço):')
numeros = [int(n) for n in lista.split()]

maior = menor = numeros[0]

for i in numeros:
        if i < menor:
            menor = i
        if i > maior:
            maior = i

print('Menor:', menor)
print('Maior:', maior)