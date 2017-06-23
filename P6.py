### 

def zmiana(a = ['bialy']):
	if(a[0]=='bialy'):
		a[0] = 'czarny'
	else:
		a[0] = 'bialy'
	return a[0]

print(zmiana())
print(zmiana())
print(zmiana())
print(zmiana())
print(zmiana())


### 008
def f(argument):
	argument = 7

a = 1
f(a)
print(a)

### 120
print('Co chcesz zorbiæ?')
o = input()
if o == '1':
	def operacja(a, b):
		return(a+b)
elif(o == '2'):
	def operacja(a, b):
		return(a-b)
else:
	def operacja(a,b):
		return print('Dziêkujê za wspó³pracê!')

print(operacja(8, 2))

### 230
def x(b):
	global a
	a = a + b
	return a
a = 1
print(a)
print(x(5))
print(a)

### 240
def sumaduzych(lista):
	global res 
	res = 0
	def anonimowafunkcja(liczba):
		if (liczba>4): 
			global res
			res = res + liczba
	
	for liczba in lista: 
		anonimowafunkcja(liczba)
	return res

print (sumaduzych([1, 2, 10, 20]))