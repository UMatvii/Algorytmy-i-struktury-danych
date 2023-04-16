def dziesietna_na_binarna(liczba):
    if liczba == 0:
        return "0"
    else:
        reszta = liczba % 2
        wynik = dziesietna_na_binarna(liczba // 2)
        return wynik + str(reszta)
liczba = int(input("Podaj liczbę dziesiętną: "))
print(dziesietna_na_binarna(liczba))