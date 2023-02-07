def czytaj_liste(lista):
    #enumerate(lista) -> (i,j), i - indeks położenia elementu w liście, j - wartość elementu
    for i,j in enumerate(lista):
        print(f"Element listy nr {i+1} -> wartość: {j}")
        
def czytaj_slownik(slownik):
    for x,y in slownik.items():
        print(f"klucz: {x} -> wartość: {y}")
