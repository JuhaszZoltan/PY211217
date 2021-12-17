# (elemi) programozási tételek:
# - sorozatszámítás
# - megszámlálás
# - szélsőérték
# --------------
# - eldöntés
# - kiválasztás
# - keresés

# minden esetben a bemenet egy lista (avagy sorozat)
# a kimenet pedig egy érték

szamok = [11, 26, 32, 76, 60, 42, 7]

# összeszegük:
sum = 0
for e in szamok:
    sum += e
print(f'op: {sum}')

# átlaguk:
print(f'op: {sum / len(szamok)}')

# szorzatuk:
mult = 1
for e in szamok:
    mult *= e
print(f'op: {mult}')

# <T> tulajdonságú elemek száma:
# T == 7re végződik:
count = 0
for e in szamok:
    if e % 10 == 7:
        count += 1
print(f'op: {count}')

# minimum érték és hely:
# maximum érték és hely:
mini = 0
maxi = 0
for i in range(1, len(szamok)):
    if szamok[i] > szamok[maxi]:
        maxi = i
    if szamok[i] < szamok[mini]:
        mini = i
print(f'op minimum: érték: {szamok[mini]}; index: {mini}')
print(f'op maximum: érték: {szamok[maxi]}; index: {maxi}')

# -----------------------

# van-e <T> tulajdonságú elem?
for e in szamok:
    if e % 10 == 7:
        print('van')
        break
else: print('nincs')

i = 0
while i < len(szamok) and szamok[i] % 10 != 7:
    i += 1
if i < len(szamok): print('van')
else: print('nincs')

# hol van az első <T> tulajdonságú elem?
for i in range(len(szamok)):
    if szamok[i] % 10 == 7:
        print(f'első ilyen elem indexe: {i}')

i = 0
while szamok[i] % 10 != 7:
    i += 1
print(f'első ilyen elem indexe: {i}')

# van-e <T> tulajdonságú elem, és ha igen, akkor hol van az első?
for i in range(len(szamok)):
    if szamok[i] % 10 == 7:
        print('van ilyen elem')
        print(f'az első ilyen elem indexe: {i}')
        break
else: print('nincs ilyen elem')

i = 0
while i < len(szamok) and szamok[i] % 10 != 7:
    i += 1
if i < len(szamok):
    print('van ilyen elem')
    print(f'az első ilyen elem indexe: {i}')
else: print('nincs ilyen elem')