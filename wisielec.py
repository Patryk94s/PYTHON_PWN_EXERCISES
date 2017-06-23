import random
from minusowanie import zaminusuj

MAKSYMALNA_ILOSC_PROB = 5

slowa = ['serek', 'biocenoza', 'michalina', 'koryfeusz', 'obrus', 'dywanik', 'poduszka', 'hemoglobina']
slowo = random.choice(slowa)
odgadniete_litery = set()
proby = 0
while (proby < MAKSYMALNA_ILOSC_PROB and set(slowo).difference(odgadniete_litery) != set()):
    print (zaminusuj(slowo, odgadniete_litery))
    print ('zgadnij kolejna litere:')
    litera = input()[0]
    if litera in set(slowo):
        odgadniete_litery.add(litera)
    else:
        print ('nie zgadles - zostaly ci jeszcze', MAKSYMALNA_ILOSC_PROB - proby, 'proby')
        proby += 1
if (proby == MAKSYMALNA_ILOSC_PROB):
    print('trudno, nie zgadles')
else:
    print(slowo)
    print('brawo!')

