dias = int(input('Digite quantos cigarros são fumados por dia:'))
anos = int(input('Digite quantidade de anos fumando cigarro:'))

minTotal = (dias * (anos * 365)) * 12
minDia = 60 * 24

print(f'Serão {minTotal/minDia:.0f} dia(s) de vida perdidos!')