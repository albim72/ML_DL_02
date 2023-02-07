liczby = [56,12,-99,122,78,90,109,899,0,-3,23,-145,9,-2,111]

def pokaz_stat(lista):
    minimum = min(lista)
    maksimum = max(lista)
    rozstep = maksimum - minimum
    liczba_el = len(lista)
    sumael = sum(lista)
    sr_arytm = sumael/liczba_el
    return minimum,maksimum,rozstep,liczba_el,sumael,sr_arytm


wynik = pokaz_stat(liczby)
print(wynik)

mini, maxi, roz, lel,sumel,sred = pokaz_stat(liczby)
print(f"wartość maksymalna: {mini}, wartość minimalna: {maxi}, rozstęp: {roz}, liczba elementów: {lel}, "
      f"suma elementów: {sumel}, średnia arytmetyczna: {sred}")
