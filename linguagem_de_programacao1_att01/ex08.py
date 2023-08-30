stg1 = input('Digite a primeira string:')
stg2 = input('Digite a segunda string:' )

caractcomuns = ''

for char in stg1:
    if char in stg2 and char not in caractcomuns:
        caractcomuns += char

if caractcomuns:
    print('Os caracteres em comum  são:', caractcomuns)
else:
    print('Não há caracteres em comum!')
