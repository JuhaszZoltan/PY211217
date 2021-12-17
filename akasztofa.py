import filmek
import random
import os
film_lista = filmek.get_film_lista()

feladvany = film_lista[random.randrange(len(film_lista))]

jo_tippek = []
rossz_tippek = []

hibalehetosegek = 10

while hibalehetosegek > 0:
    os.system('cls')
    felkesz = ''
    for k in feladvany:
        if k in jo_tippek: felkesz += k
        elif k == ' ': felkesz += ' '
        else: felkesz += '*'
    print(felkesz, end='\0')
    print(f'\t\t{rossz_tippek}', end='\0')
    print(f'\t\thibalehetőségek: {hibalehetosegek}')
    if felkesz == feladvany:
        print('NYERTÉL!!')
        break
    tipp = input('a következő tipped: ')
    if tipp in feladvany.lower():
        jo_tippek.append(tipp.upper())
        jo_tippek.append(tipp.lower())
    elif tipp not in rossz_tippek:
        rossz_tippek.append(tipp)
        hibalehetosegek -= 1
else: print('VESZETTÉL!')