def nSilnia(n):
    '''
    Funkcja obliczaj¹ca silniê dla zadanej wartoœci n.
    '''
    wynik = 1
    i = 1
    while(i <= n):
        wynik = wynik*i
        i += 1
    print(wynik)

nSilnia(5)

print(nSilnia.__doc__)

### 002
import random

def wykres(liczby = [random.randint(1, 7) for i in range(10)], znaczek = '#'):
	for liczba in liczby:
		print (znaczek * liczba)

wykres()
wykres(znaczek = '*')
wykres(znaczek = 'x')

def podziel(liczba, stosunek = random.random()):
	a = liczba * stosunek
	b = liczba - a
	return a, b

print(podziel(10))
print(podziel(10))
print(podziel(10))

### 005
def wypisz(napis, kolor='black', size='12', weight='normal'):
    print ('<span style="color: ' + kolor + '; font-size: ' + size + '; font-weight: ' + weight + '">' + napis + '</span>')
wypisz('Ala ma Asa', size='48')
wypisz('Ala ma Asa', kolor='red', weight='bold')
