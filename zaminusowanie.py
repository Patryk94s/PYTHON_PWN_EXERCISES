# -*- coding: utf-8 -*-

def zaminusuj(slowo, odgadniete_litery):
    """
    Zamienia w podanym słowie wszystkie litery - oprócz tych z podanego zbioru - na minusy:
    >>> zaminusuj("czapka", [])
    '------'
    >>> zaminusuj("czapka", ['p'])
    '---p--'
    >>> zaminusuj("czapka", ['p', 'a'])
    '--ap-a'
    >>> zaminusuj("czapka", ['p', 'a', 'x'])
    '--ap-a'
    """
    zaminusowane = ''
    for litera in slowo:
        if litera in odgadniete_litery:
            zaminusowane = zaminusowane + litera
        else:
            zaminusowane = zaminusowane + '-'
    return zaminusowane

if __name__ == "__main__":
    import doctest
    doctest.testmod()
