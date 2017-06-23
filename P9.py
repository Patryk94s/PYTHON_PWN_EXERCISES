
    
def potegowanie(x,y):
    def inkrementacja():
        global wynik
        res = wynik + 1 
        return res    
    
    i = 0
    global wynik
    while (i < y):
        wynik *= x
        i += 1
    print('Wynik potegowania '+str(wynik))
    print(inkrementacja())
    
wynik = 1
potegowanie(3,2)