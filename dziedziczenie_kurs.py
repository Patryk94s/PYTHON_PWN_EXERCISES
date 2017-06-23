'''
class Bazowa:
    a = 1
    def dodaj(self):
        return 'klasa bazowa'

class Potomna(Bazowa):

    def dodaj1(self):
        return 'klasa potomna'

p1 = Potomna()
print(p1.dodaj())
print(p1.dodaj1())

class A1:
    a=1
    b=2
    def __init__(self, a):
        self.a = a
    
    def zwroc(self):   
        return 'jestem w A1'
    def dodawanie(self):
        return self.a + self.a
class B1(A1):
    def __init__(self, a, b):
        super(B1,self)
        self.b = b
        print(self.a + self.b)
        
    def zwroc(self):
        return super(B1,self).zwroc() + 'jestem w B1'

    def dodawanie(self, x):
        super(B1,self)
        self.x = x
        return self.a + self.x
o1 = B1(1,4)
print(o1.zwroc())
print(o1.dodawanie(6))


class Produkt:
    def __init__(self,nazwa, cena):
        self.nazwa = nazwa
        self.cena = cena
        print('konstruktor1')
    def info(self):
        print('Produkt: '+str(self.nazwa)+' kosztuje: '+str(self.cena))

class Oprogramowanie(Produkt):
    def __init__(self, nazwa,cena, jezyk, system):
        super().__init__(nazwa,cena)
        self.jezyk = jezyk
        self.system = system
        print('konstruktor2')
    def info(self):
        print('Produkt: '+str(self.nazwa)+' kosztuje: '+str(self.cena)+'z³ (jêzyk: '+str(self.jezyk)+', system: '+str(self.system)+')')
p2 = Oprogramowanie('Aplikacja X', 4000, 'Python', 'IOS')
p2.info()

class Szkolenia(Oprogramowanie):
    def __init__(self, nazwa,cena, jezyk, system, termin):
        super().__init__(nazwa,cena, jezyk, system)
        self.termin = termin
        print('konstruktor3')
    def info(self):
        print('Produkt: '+str(self.nazwa)+' kosztuje: '+str(self.cena)+'z³ (jêzyk: '+str(self.jezyk)+', system: '+str(self.system)+'). Termin szkolenia: '+str(self.termin))    

p3 = Szkolenia('Szkolenie 1', 4000, 'Python', 'IOS','2017-05-24')
p3.info()



class Kolor:
    r = 0
    g = 0
    b = 0
    def __init__(self, r,g,b):
        self.r = r
        self.g = g
        self.b = b
    def __add__(self,other):
        return self.r + other.r, self.g + other.g, self.b + other.b
    def __str__(self):
        return '['+str(self.r)+','+str(self.g)+','+str(self.b)+']'
    
o1 = Kolor(255,0,0) # czerwony
o2 = Kolor(0,255,0) # zielony
print(o1+o2)

class AutoCalc:
    def __init__(self, marka, cena_netto, vat):
        self.marka = marka
        self.cena_netto = cena_netto
        self.vat = vat
    def calculation(self):
        self.cena_brutto = self.cena_netto*(1+self.vat)
        return self.cena_brutto
class ExtraCalc(AutoCalc):
    cena_calk = 0
    def __init__(self, marka, cena_netto, vat, dodatki):
        super().__init__(marka, cena_netto, vat)
        self.dodatki = dodatki
    def calculation(self):
        super().calculation()
        self.cena_calk = self.cena_brutto + self.dodatki*(1+self.vat)
    def __str__(self):
        return 'Kupujesz auto marki '+str(self.marka)+' cena brutto (sumaryczna): '+str(self.cena_calk)
a1 = AutoCalc('Audi',200000,0.23)
print(a1.calculation())
a = input('Podaj nazwê auta ')
b = int(input('Podaj cenê netto auta '))
c = float(input('Podaj stawkê vat '))
d = int(input('Podaj kwotê dodatków auta '))
a2 = ExtraCalc(a,b,c,d)
a2.calculation()
print(a2)





class P:
    def dodaj(self, a, b):
        self.a = a
        self.b = b
        return self.a + self.b
class K(P):
    def dodaj(self,a,b,c):
        super().dodaj(a,b)
        self.c = c
        return self.a + self.b + self.c
    
a = K()
print(a.dodaj(1,2,3))
'''

class Pracownik:
    def __init__(self, imie, nazwisko, kontrakt='staz'):
        self.imie = imie
        self.nazwisko = nazwisko
        self.kontrakt = kontrakt
        print(self.imie, self.nazwisko, self.kontrakt)

class Pensja(Pracownik):
    pensja = 1000
    def __init__(self, imie, nazwisko, kontrakt):
        super().__init__(imie, nazwisko, kontrakt)
    def zmien(self):
        if (self.kontrakt == 'staz'):
            self.kontrakt = 'etat'
            self.pensja = 5000
        elif(self.kontrakt == 'etat'):
            self.kontrakt = 'etat'    
            self.pensja = 5000        
    
    def __str__(self):
        return('Pracownik: '+str(self.imie)+' '+str(self.nazwisko)+' '+str(self.kontrakt)+' (pensja: '+str(self.pensja)+')')

empl1 = Pensja('Michal','Kruczkowski','staz')
empl1.zmien()
print(empl1)