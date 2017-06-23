class Example:
    a = 1
    b = 2
    wynik = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b
    def dodawanie(self):
        self.wynik = self.a+self.b
        return self.wynik 
    
    def __str__(self):
        return 'Wynik dodawania wynosi: '+str(wynik) 
    
obj1 = Example(3,4)      
wynik = obj1.dodawanie()
print(wynik)
print(obj1.a)
print(obj1.b)
print(obj1)

class Wektor(object): 
	def __init__(self, x, y): 
	    self.a = x 
	    self.b = y 
	    print("wektor zosta³ stworzony!")
	def dlugosc(self): 
	    return (self.a ** 2 + self.b ** 2) ** 0.5
	def __str__(self): 
	    return "Wektor x="+str(self.a)+" y="+str(self.b)
	def __add__(self,other):
	    return Wektor(self.a+other.a, self.b+other.b)
	def __sub__(self,other):
	    return Wektor(self.a-other.a, self.b-other.b)
	def __lt__(self,other):
	    return Wektor(self.a < other.a, self.b < other.b)
	    
	
w1 = Wektor(5, 7)
w2 = Wektor(3, 4)
print(w1+w2) 
print(w1-w2)
print(w1<w2)
print(w1.__dict__)
print(w1.__class__)

class Rodzic:
    z1 = 12
    def zwieksz(self):
	z1 +=1

class Dziecko(Rodzic):
    z2 = 2
    
obj1 = Rodzic()
obj1.z1 = 5
obj1.zwieksz()
print(obj1.z1)
obj2 =Dziecko()
print(obj2.z1)