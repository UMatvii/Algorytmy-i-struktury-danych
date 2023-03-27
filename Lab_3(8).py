def przenies(ile, skad, dokad, przez):
   if ile >= 1:
        przenies(ile - 1, skad, przez, dokad)
        print(skad, "->", dokad)
        przenies(ile - 1, przez, dokad, skad)

ilosc = int(input("Podaj ilość krążków: "))
przenies(ilosc, "A", "B", "C")