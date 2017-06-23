# -*- coding: utf-8 -*-

# Komentarz jednowierszowy 
zmiennaCalk = 12
zmiennaCalk1 = zmiennaCalk + 5
zmiennaPrzecinkowa = 12.5
zmiennaTekst = 'Napis do wyswietlenia'
zmiennaTekst1 = "Inna zmienna tekstowa"
zmiennaZnakowa = 'A'
zmiennaZnakowa = "a"
# del zmiennaZnakowa
print(zmiennaZnakowa)
print(5)
print('Tekst bezposrodnio w print')
print(zmiennaCalk)
print(zmiennaCalk1)
print(zmiennaPrzecinkowa, zmiennaCalk, zmiennaTekst)
print(zmiennaTekst, zmiennaTekst1)

suma = zmiennaCalk + zmiennaCalk1 + 23.5
print(suma)
print(zmiennaCalk + zmiennaCalk1 + 23)
print('w1'+' '+'w2')
print('w1','w2')

imie = 'Michal'
nazwisko = 'Kruczkowski'
rok_u = 1987
stanowisko = 'dev'
pensja = 10000
vat = 0.19

print(imie, nazwisko, rok_u, stanowisko, pensja, pensja - (pensja * vat))

pi = 3.14
# podaj wartosc promienia
r = 5
Pk = pi*r*r
print(pi*r*r)
print(type(pi))
print(type(Pk))
print(type(imie))
print(type(r))

wynik = 3//2
print(type(wynik))

print(round(1.2), round(1.5), round(1.8)) 
print(round(-1.2), round(-1.5), round(-1.8))

vat3 = 0.03
vat7 = 0.07
vat23 = 0.23
kwota_b = 1000
print(kwota_b, round(kwota_b*(1-vat3),2))
print(kwota_b, round(kwota_b*(1-vat7),2))
print(kwota_b, round(kwota_b*(1-vat23),2))

chleb = 1.99
mleko = 2.50
cukierki = 12.99

zamowienie = (2*chleb) + (0.5*mleko) + (0.3*cukierki)

print('Twoje zamowienie:', zamowienie, 'zl')

p = True
q = False
zdanie = p and q
print(zdanie)
print(bool(12))
print(bool({1,2,3}))

print('Cytat:\n"Byc albo nie byc?"')
print("I'm your father")
print('Zażółć gęślą jaźn',"")

print('Napis'+' jest'+' złączony')
print('napis x3 '*3)
imie = 'Michał'
imieS = imie + ', '
print((imie+', ')*10)
print(imieS*10)
print("Cena wynosi: "+ str(1.99) + 'zł')
napis = '12'
print(int(napis) + 2)

imie1 = 'Ala'
imie2 = 'Ola'
imie3 = 'Ela'

print(imie1 < imie2)
print(imie1 < imie3)
print(imie2 < imie3)

print(imie1 + ', ' + imie2 + ' i ' + imie3)

a = 4
b = 3
print(a % b)
print(a ** b)
print(a // b)

# Pole kwadratu
bok_kw = 4
P_kw = bok_kw ** 2
print("Pole kwadratu wynosi: "+ str(P_kw))

# Obwód koła
promien = 3
O_kol = 2 * 3.14 * promien
print("Obwód koła wynosi: "+ str(O_kol))

# Pole koła
P_kol = 3.14 * (promien**2)
print("Pole koła wynosi: "+ str(P_kol))

wynagrodzenie_n = 5500
godziny = 168
vat = 0.19
stawka_h_netto = wynagrodzenie_n/godziny
stawka_h_brutto = stawka_h_netto + (stawka_h_netto * vat)
print("Pracownik X zarobił: " + str(round(stawka_h_netto,2)) + "zł/h (" + str(round(stawka_h_brutto,2)) + "zł/h - brutto)" )

print('a' and 'b')

p = True
q = True

res1 = not (p and q)
res2 = (not p or not q)
#print(res1)
#print(res2)
print(res1 == res2)

a = False
b = False
c = True

f1 = (not a) and (not b) and (not c)
f2 = (not a) and (not b) and c
f3 = (not a) and b and (not c)
f4 = a and (not b) and (not c)

print(f1, f2, f3, f4)
f_res = f1 or f2 or f3 or f4
print(f_res)


# Zadanie urojone
podstawa = 17
multiplex = round(podstawa**(0.5),2)  
im = 1j
result = multiplex * im 
print(result)

# Zadanie z Z

Z = 17%7
print(Z**2+3*Z)

# P30
print((str(1.2e+3+34.5)+';')*20)

print('Dane użytkownika: \nTwoje imie: \t Michał nazwisko:\t Kruczkowski')
"""
# Pole kwadratu
print('Program obliczający pole kwadratu')
bok_kw = float(input("Podaj długość boku kwadratu: "))
P_kw = bok_kw ** 2
print("Pole kwadratu wynosi: "+ str(P_kw))
"""
"""
SPK = int(input("Podaj kwotę początkową"))
N = int(input("Podaj liczbę lat lokaty")) 
P = float(input("Podaj wysokość oprocentowania [%]"))
Wynik = round(SPK * (1+(P/100))**N,2) 
print('Uzbierałeś: '+ str(Wynik))
"""
napis = 'WIELKIKI NAPIS'
print(napis.capitalize())
print(napis.replace('KI', 'MI'))

lista1 = []
lista1.append('acb')
lista1.append(23)

lista1[1] = 'A'

print(lista1[0], lista1[1])

lista2 = [1,2,3,4,5]
print(lista2[0], lista2[4])
print(lista2[2:])
print(lista2[0::3])
print(len(lista2))

ListList = [ [1, 2, 3], ["Nocny", "Dzienny"] ]
#print(ListList[0][2])

liczby = [1,2,3]
napisy = ['Adam','Ewa']

print(liczby[0:])
print(napisy[0:])

liczby1 = []
napisy1 = []
liczby1.append(1)
liczby1.append(2)
liczby1.append(3)
napisy1.append('Adam')
napisy1.append('Ewa')

print(liczby1[0:])
print(napisy1[0:])
"""
listaX = [[],[]]
#listaX[0].append(input("Podaj element listy: "))

print(listaX[0][0])
"""
artykuly = ['cheleb', 'mleko', 'masło', 'czeko', 'woda']
ceny = [2.45, 3.45, 3.00, 5.45, 3.15]
print('Twoje artykuły: \n')
print(str(artykuly[0]) + '\t'+ str(ceny[0]))
print(str(artykuly[1]) + '\t'+ str(ceny[1]))
print(str(artykuly[2]) + '\t'+ str(ceny[2]))
print(str(artykuly[3]) + '\t'+ str(ceny[3]))
print(str(artykuly[4]) + '\t'+ str(ceny[4]))
print('=====================================')
print("Suma do zapłaty " + str(ceny[0]+ceny[1]+ceny[2]+ceny[3]+ceny[4]))