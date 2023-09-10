string = input('Digite uma string:')

def caracteres(string):
    count = {}
    for caractere in string:
        if caractere in count:
            count[caractere] += 1
        else:
            count[caractere] = 1
    return count

count = caracteres(string)

def resultado(count):
    for caractere, repeticao in count.items():
        print(f'{caractere}: {repeticao}x')

resultado(count)
