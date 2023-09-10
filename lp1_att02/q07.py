lista = [5, 2, 8, 1, 6, 9, 3, 7, 4]

def menor_elemento(lista):

    menor = lista[0]
    for i in lista:
        if i < menor:
            menor = i
    return menor

menor_elemento = menor_elemento(lista)

print(f"O menor elemento da lista é: {menor_elemento}")
