# listák

# alapból vannak benne elemek:
lista_1 = ['babzsák', 'jékcsákány', 'bukósisak']

# üres:
lista_2 = []

# hossza:
egesz_szam = len(lista_1)

# elemeire lehet hivatkozni az ún. indexekkel:
# az indexelés 0-nál kezdődik
lista_egyik_eleme = lista_1[1]

# a lista utolsó elemének indexe a lista hossza mínusz egy
utolso_elem = lista_1[len(lista_1) - 1]

# listához új elemet hozzáadni:
lista_1.append('serpenyő')
# az így hozzáadott elem mindig a lista végére kerül

lista_1.insert(0, 'esernyő')
print(lista_1)

# lista elemeinek bejárása:
for elem in lista_1:
    print(elem)

# lista indexeinek bejárása:
for index in range(len(lista_1)):
    print(lista_1[index])

# lista össze elemének kiírása:
print(lista_1)

#lista elemeinek rendezése:
lista_1.sort()

# a stringek valójában karakterek listái,
# tehát minden fenti dolog rájuk is érvényes:

szoveg = 'már csak két munkanap van hátra...'
szoveg_hetedik_karaktere = szoveg[6]
szoveg_karaktereinek_szama = len(szoveg)
for karakter in szoveg:
    print(karakter, end='-')

#kivéve új karakter hozzáadása, azt így:
szoveg += '!!!'

# szövegekre pár metódus:
# csupa kisbetű:
kisbetus_szoveg = szoveg.lower()
# csupa nagybetű:
nagybetus_szoveg = szoveg.upper()
# feldarabolás (pl. szóközök mentén):
stringeket_tartalmazo_lista = szoveg.split(' ')
# trimmelés aka. leszedi az elejéről és a végéről a whitespace karaktereket:
trimmelet_szoveg = szoveg.strip()