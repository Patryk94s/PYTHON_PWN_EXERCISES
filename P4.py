'''
# P57
sklep_zamowienie = {'monitor1': "Monitor LG 16'", 'klawiatura':'Klawiatura Logitech'}
sklep_ilosc = {'monitor1': 10, 'klawiatura':5}
sklep_cena ={'monitor1': 1000, 'klawiatura':500}
zamowienie = {'monitor1': 4, 'monitor2':2, 'klawiatura':6}
do_zaplaty = 0
for prod in zamowienie:
    if (prod in sklep_zamowienie.keys() and zamowienie[prod] <= sklep_ilosc[prod]):
        print('Produkt jest w sklepie')
        print('Zam�wi�e�: '+sklep_zamowienie[prod])
        sklep_ilosc[prod] = sklep_ilosc[prod] - zamowienie[prod]
        do_zaplaty += zamowienie[prod]*sklep_cena[prod]
    elif(prod in sklep_zamowienie.keys() and zamowienie[prod] > sklep_ilosc[prod]):
        print('Produkt jest w sklepie, ale zam�wienie jest zbyt du�e')
    else:
        print('Brak produktu '+prod+' w sklepie')
print('Do zap�aty: '+ str(do_zaplaty))
print('Pozpsta�o w sklepie: ' + str(sklep_ilosc))

x = int(input('Podaj podstaw� pot�gi'))
y = int(input('Podaj wyk�adnik pot�gi'))

wynik = 1
i = 0
while (i < y):
    wynik *= x
    i += 1
print('Wynik pot�gowania '+str(x)+' do '+str(y)+' wynosi: '+str(wynik))
'''
a = int(input('Podaj pierwszy wyraz ciagu geometrycznego'))
q = int(input('Podaj ioraz ciagu geometerycznego'))
n = int(input('Podaj liczb� wyraz�w do zliczenia'))

i = 0
suma = 0
while (i < n):
    suma += a*(q**i)
    i += 1
print('Suma '+str(n)+' wyraz�w ci�gu geometrycznego wynosi: '+str(suma))



