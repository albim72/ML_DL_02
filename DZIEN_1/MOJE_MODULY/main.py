#import dane
#import dane as dn
from dane import book,nr_filia
from dane import book as ksiazka
from dane import nr_filia as filia
from funkcje.bfunkcje import czytaj_liste, czytaj_slownik
from klasy.cdane import CDane

print("_________________________________________")
print(nr_filia)
print(book)
print("_________________________________________")

print(filia)
print(ksiazka)

print("____________________użycie funkcji bfunkcje_____________________")
czytaj_liste(filia)
czytaj_slownik(ksiazka)

print("____________________użycie obiektu klasy CDane_____________________")
d = CDane(filia,ksiazka)
d.czytaj_l()
d.czytaj_d()
