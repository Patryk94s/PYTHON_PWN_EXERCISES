# -*- coding: utf-8 -*-
import random

'''
print('Dane pracowników:')
index = int(input('Podaj nr. osoby'))
index -= 1 
imiona = ['Michał', 'Adam', 'Ola', 'Ela']
nazwiska = ['X', 'Y', 'Z', 'T']
data_ur = ('1987-02-01', '1986-02-01', '1957-02-01', '1981-02-01')
pesel = ('15548821621', '15548821622', '15548821623', '15548821624')

print(imiona[index], nazwiska[index], data_ur[index], pesel[index])
'''
# P42
'''
zdanie = input("Wpisz zdanie: ")
zdanie_clear = zdanie.strip()
zdanie_sep = zdanie_clear.split(' ')
print(zdanie_sep)
print(zdanie_sep[0: ])
print('Cale zdanie:')
print(zdanie_sep[0], zdanie_sep[1], zdanie_sep[2])
'''

# P43
'''
dzien = ('01','02','03', '04')
miesiac = ('01', '02', '03', '04')
rok = ('2017', '2018', '2019')

dzien_index = int(input('wprowadz dzień przydatności do spożycia: ')) - 1
miesiac_index = int(input('wprowadz miesiąc przydatności do spożycia: ')) - 1
rok_index = int(input('wprowadz rok przydatności do spożycia: [2017 - 1, 2018 - 2, 2019 - 3]')) - 1

print('Drukuję etykietę ...')
print('====================')
print(str(rok[rok_index])+'-'+str(miesiac[miesiac_index])+'-'+str(dzien[dzien_index]))
print('====================')

a = 'konto1'
dostep = {'abc' : 'konto1', 'cba' : 'konto2', 'efg' : 'konto3'}
print(dostep['abc'], dostep['cba'])
dostep['cba'] = 'kontoX'
print(dostep['abc'], dostep['cba'])
#dostep.clear()
print(dostep['abc'], dostep['cba'])
print(dostep.keys())
print(dostep.values())

# P44
liczby_konw = {'jeden':1, 'dwa':2, 'trzy':3, 'cztery':4, 'pięć':5}
liczby_konw2 = {1:'I', 2:'II', 3:'III', 4:'IV', 5:'V'}
klucz = input('podaj liczbę zapisaną słownie: ')
print('Jest to liczba: '+ str(liczby_konw[klucz])+ ' zapisana dziesiętnie')
print('Jest to liczba: '+ str(liczby_konw2[liczby_konw[klucz]])+ ' w zapisie rzymskim')
'''
# P45
'''
kody_tow = {'0o2':'produkt1', '0o3':'produkt2', '0o4':'produkt3'}
nazwa_ilosc = {'produkt1':'1l', 'produkt2':'1kg', 'produkt3':'100g'}
nazwa_cena_n = {'produkt1':150.00, 'produkt2':148.25, 'produkt3':15.50}

index = input('Podaj kod towaru: '+ str(kody_tow.keys()))
print('Wybrałeś produkt:')
print('Nazwa\t\tIlość\tCena netto\tCena brutto')
print(kody_tow[index]+'\t'+nazwa_ilosc[kody_tow[index]]+'\t'+str(nazwa_cena_n[kody_tow[index]])+'\t\t'+str(nazwa_cena_n[kody_tow[index]]*1.23))
'''
'''
set1 = set([1,2,3.5,4,'a'])
print(len(set1))
print(2 in set1)
'''
los = set()
l1 = random.randint(1,49)
l2 = random.randint(1,49)
l3 = random.randint(1,49)
l4 = random.randint(1,49)
l5 = random.randint(1,49)
l6 = random.randint(1,49)
l7 = random.randint(1,49)
l8 = random.randint(1,49)

los.add(l1)
los.add(l2)
los.add(l3)
los.add(l4)
los.add(l5)
los.add(l6)

print(los)

# P52
'''
l1 = [' ','x',' ','x',' ','x',' ','x']
l2 = ['x',' ','x',' ','x',' ','x',' ']
l3 = [' ',' ',' ',' ',' ',' ',' ',' ']
l4 = [' ',' ',' ',' ',' ',' ',' ',' ']
l5 = [' ',' ',' ',' ',' ',' ',' ',' ']
l6 = [' ',' ',' ',' ',' ',' ',' ',' ']
l7 = [' ','o',' ','o',' ','o',' ','o']
l8 = ['o',' ','o',' ','o',' ','o',' ']

print(str(l1).replace(',','|')+'\n'+str(l2).replace(',','|')+'\n'+str(l3).replace(',','|')+'\n'+str(l4).replace(',','|')+'\n'+str(l5).replace(',','|')+'\n'+str(l6).replace(',','|')+'\n'+str(l7).replace(',','|')+'\n'+str(l8).replace(',','|'))
'''
#a = int(input('Podaj dowolną liczbę naturalną'))
'''
if (a < 5): 
    print('Podałeś liczbę mniejsza od 5')
    a = a + 1
    i = 'zmienna pomocnicza'
    print(i)
    print('Jeszcze jestem w if')
elif (a >1 and a <= 5):
    print('Twoja liczba jest z przedziału od 1 do 5')
else:
    print('Twoja liczba nie spełnia wymagań')

print('Jestem poza if')    
'''

#print('Poprawnie') if (a == 1) else print('Błędnie')


# P53
'''
a = int(input('Podaj wartość do sprawdzenia'))
print('Sprawdzenie dla: '+ str(a))
if (bool(a) == True):
    print('True')
elif(bool(a) == False):
    print('False')
'''

# P55
'''
Lista = []
Lista.append(int(input('Wprowadź pierwszą liczbę')))
Lista.append(int(input('Wprowadź drugą liczbę')))

if (Lista[0] > 0 and Lista[1] >0):
    print('Liczby dodatnie')
elif (Lista[0] > 0 and Lista[1] <= 0):
    print('Tylko pierwsza liczba jest dodatnia')
elif (Lista[0] <= 0 and Lista[1] > 0):
    print('Tylko druga liczba jest dodatnia')
else:
    print('Obie liczby są ujemne')
'''
'''
a = int(input('Podaj liczbę'))
print('liczba parzysta') if (a % 2 == 0) else print('liczba nieparzysta')
'''

a = 1

while (a < 5):
    print('Jestem w pętli')
    a += 1           # a = a + 1
else:
    print('Jestem poza pętlą')
    
tablica = ['A','B','C','D','E',5,6]

for element in tablica:
    print(element)

for index, wartosc in enumerate(tablica):
    print(index, wartosc)

slownik = {1:'a',2:'b',3:'c'}

for key in slownik:
    print(slownik[key])
    
liczby = range(1,7)
print(liczby)
print(liczby[5])

for i in liczby:
    print(i)
'''
for i in liczby:
    if(i%2 == 0):
        print('Liczba '+str(i)+' jest parzysta')
    else:
        print('Liczba '+str(i)+' jest nieparzysta')
'''
'''
for i in range(1,9):
    print('l1=%4i, l2=%6i, l3=%8i' % (i, i**2, i**3))
'''


# P57
sklep_zamowienie = {'monitor1': "Monitor 16'", 'klawiatura':'Klawiatura Logitech'}
zamowienie = ['monitor1', 'monitor2']

for prod in zamowienie:
    if (prod in sklep_zamowienie.keys()):
        print(sklep_zamowienie[prod])
    else:
        print('Brak produktu '+prod+' w sklepie')

