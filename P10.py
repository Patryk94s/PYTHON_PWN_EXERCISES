'''
class Pierwsza:       
    def dodaj(self, a, b):
        self.a = a
        self.b = b
        return self.a+self.b
    def odejmuj(self, c, d, e):
        self.c = c
        self.d = d
        self.e = e
        print('Wynik odejmowania: '+str(self.c-self.d-self.e))
    def minus(self):
        return self.a-self.b    
o2 = Pierwsza()
print('wynik dodawania: '+str(o2.dodaj(5,4)))
o2.odejmuj(12,3,4)
print('wynik odejmowania na tych samych wartoœciach: '+str(o2.minus()))

class Druga:
    i = 1
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print('Konstruktor wywo³ano')
    def __add__(self, other):
        return self.a + other.a, self.b + other.b
    def __sub__(self, other):
        return self.a - other.a, self.b - other.b
    def __eq__ (self, other):
        return self.a == other.a, self.b == other.b
    def __str__(self):
        return 'Wynik wynosi: '+str(self.a+self.b)
    def dodaj(self):
        print('metodê wywo³ano')
        return self.a+self.b
    
d1 = Druga(5,3)
d2 = Druga(4,2)
c = d1 + d2
print(d1 + d2)
print(d1 - d2)
print(d1 == d2)
print(d1)



class Zawodnik:
    def __init__(self, imie, nazwisko, waga, wzrost):
        self.imie = imie
        self.nazwisko = nazwisko
        self.waga = waga
        self. wzrost = wzrost
    def bmi(self):
        return self.waga/((self.wzrost/100)**2)
    def __str__(self):
        return 'Zawodnik: '+str(self.imie)+' '+str(self.nazwisko)+', BMI='+ str(round(self.waga/((self.wzrost/100)**2),2))

z1 = Zawodnik('Adam','Malysz',59,168)
print(z1.bmi())
print(z1)

class Index:
    oceny = [3,4,5]
    srednia = 0
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
    def wprowadz(self):
        i = 'T'
        j = 0
        suma = 0
        wprowadzone = []
        while (i == 'T'):
            wprowadzone.append(int(input("Podaj oceny do wprowadzenia "))) 
            suma += wprowadzone[j] 
            i = input('Czy chcesz dalej wprowadzaæ oceny? (T/N)')
        self.srednia = suma / (len(wprowadzone))     
        j += 1
        #return self.srednia
    def __add__(self, other):
        return (self.srednia + other.srednia)/2
    def __str__(self):
        return 'Student: '+self.imie+' '+self.nazwisko+' otrzyma³ oceny: '+str(round(self.srednia,2))

s1 = Index('Micha³', 'Kruczkowski')
s1.wprowadz()
print(s1)
s2 = Index('Adam', 'Kowalski')
s2.wprowadz()
print(s2)
s3 = Index('Jan', 'Nowak')
s3.wprowadz()
print(s3)
print(s1 + s2)
print(s2 + s3)
'''
import random

class Lotto:
    def __init__(self):
        self.wylosowane = random.sample(range(1,50),6)            
    def sortowanie(self):    
        self.posortowane = sorted(self.wylosowane)
    def czas(self, data):
        self.data = data
    def __str__(self):
        return 'Wylosowane liczby w terminie '+str(self.data)+': '+str(self.wylosowane)+' (uporz¹dkowane: '+str(self.posortowane)+')'
los1 = Lotto()
los1.sortowanie()
los1.czas('2017-05-16')
print(los1)

class Bazowa:
    a = 1
    def wypisz(self):
        print('Jestem w klasie Bazowa')
b1 = Bazowa()
b1.wypisz()

class Potomna(Bazowa):
    b = 2
    def info(self):
        print('Jestem w klasie Potomna')



