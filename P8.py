# -*- coding: utf-8 -*-
lista = [1,5,2,8,13]

for element in lista:
    print('Rozpoczynam nowe obejście')
    if (element % 2 != 0):
        continue
    print('Liczba '+str(element)+' jest parzysta')
    
###
    '''
text = 'przykladowy napis'
#print(text[0])

szukana = input('Podaj małą literkę alfabetu ')

for index, value in enumerate(text):
    if (value != szukana):
        continue
    print('Literka '+value+' jest '+str(index+1)+' w alfabecie')
    break
else:
    print('Brak szukanej literki ('+szukana+') w alfabecie')
    '''
###
    '''
slownie = {'1':'jeden', '2':'dwa', '3':'trzy', '4':'cztery', '5':'pięć'}
liczba = input('Podaj liczbę ')

for element in liczba:
    if(element not in slownie.keys()):
        continue
    print(slownie[element])
'''    
###
'''
tabliczka = [1,2,3,4,5]

for iter in tabliczka:
    print("%4i %4i %4i %4i %4i" % ((iter*1),(iter*2),(iter*3),(iter*4),(iter*5)))
    
print('%4i%4i%4i%4i%4i%4i%4i%4i%4i%4i' % (1,2,3,4,5,6,7,8,9,10))
print('_______________________________________________________')
for i in range(1,11):
    for j in range(1,11):
        print('%4i' % (i*j), end='')
    print('')
'''    
tablica = range(-20,45,1)
print(tablica)

for licz in tablica:
    print('| %+5.2f | %+5.2f |' % (licz, (32+(9/5)*licz)))


###
def indexStudenta():    
    oceny = ['3','4','5']
    i = ','
    j = 0
    suma = 0
    wprowadzone = []
    niepopr = 0
    while (i == ','):
        wprowadzone.append(input("Podaj oceny do wprowadzenia (po przecinku)"))
        if (wprowadzone[j] in oceny):
            suma += int(wprowadzone[j])
            print(wprowadzone[j])
        else:
            print('Podałeś niepoprawną ocenę!')
            niepopr += 1
    i = input('Czy chcesz dalej wprowadzać oceny?')
    j += 1

    srednia = round(float(suma / (len(wprowadzone)-niepopr)),2)
    print('Twoje oceny: '+str(wprowadzone))
    print(srednia)

### FUNKCJE

def wyswietl():
    print('Wyświetlam informacje po wywołaniu')

def suma(a,c,b=0):
    sum1 = a + b+c
    add1 = a - b-c
    return sum1, add1

wyswietl()
wyswietl()
wyswietl()
wyswietl()
liczba1 = 1
liczba2 = 5
suma(15,4)
suma(liczba1,liczba2)
print(suma(1,2))
print(suma(5,2,1))
print(suma(a=5,b=4,c=1))
#indexStudenta()

def dowolnaLiczbaParametrow(*arg):
    suma = 0
    for i in arg:
        suma += i
    return suma

print(dowolnaLiczbaParametrow(2,5,8,4,4,6,7,8))

### Silnia
'''
def silnia(n):
    res = 1
    i = 1
    while(i <= n):
        res *= i
        i += 1
    return res

print(silnia(int(input('Podaj n '))))    
'''
### fib

def fib(x):
    ciag = [1,1]
    i = 0
    fibSuma = 2
    while(i<(x-2)):
        ciag.append(ciag[i]+ciag[i+1])
        fibSuma += ciag[i]+ciag[i+1]
        i += 1    
    return ciag[x-1], fibSuma
print(fib(4))

### Losowanie
import random
'''
def losuj(l = 5):
    wyrazy = ['Ala','ma','kota', 'a', 'kot', 'ma', 'Ale']
    losowe = []
    i = 0
    while (i < l):
        losowe.append(random.choice(wyrazy))
        i += 1
    losowe[0] = losowe[0].capitalize()
    losowe[len(losowe)-1] = losowe[len(losowe)-1]+'.'
    for z in losowe:
        print(str(z)+' ',end='')
    

losuj(5)
'''
### Wykresy
'''
def wykresy(symbol='*'):
    a = input('Chcesz lowowo wygenerować liczby? (T/N)? ')          
    if (a == 'N' or a == 'n'):
        zakres = range(1,11)
        wartosci = []
        for val in zakres:
            wartosci.append(int(input('Podaj liczbę')))
        print(wartosci)
        for i in wartosci:
            print(symbol*i)
    elif(a == 'T' or a == 't'):
        zakres = range(1,11)
        wartosci = []
        for val in zakres:
            wartosci.append(random.choice(range(1,11)))
        print(wartosci)
        for i in wartosci:
            print(symbol*i)    
    else:
        wykresy()

wykresy('#') 
'''
### HTML
'''
def htmlGenerator(napis, color='black', size='12px', weight='6px'):
    out = '<span style=color: '+str(color)+'; font-size: '+str(size)+'; font-weight:'+str(weight)+'>'+str(napis)+'</span>'
    return out

print('gotowy html')
print(htmlGenerator('Witaj!'))


### zmiana
a = 'czarny'
def zmiana():
    global a
    if (a == 'czarny'):
        a = 'bialy'
        return a
    else:
        a = 'czarny'
        return a
def wywolaj():
    i = 1
    while(i <= 10):
        print(zmiana())
        i +=1
wywolaj()

###
def liczDuze():
    liczby = [1,3,4,65,35,3,5,7]
    suma = 0
    for i in liczby:
        if(i >= 5):
            suma += i
    return suma

print(liczDuze())
'''
### zmienne globalne

def potegowanie(x,y):
    i = 0
    wynik = 1
    while (i <= y):
        wynik *= x
    print('Wynik potegowania '+str(wynik))

potegowanie(2,3)