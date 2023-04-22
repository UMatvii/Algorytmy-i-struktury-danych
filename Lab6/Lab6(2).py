tabl = []
n = int(input("Podaj n: "))
for liczby in range(n):
    if liczby >= 0 and liczby <= 200:
        liczby = int(input("Podaj liczby: "))
        tabl.append(liczby)
    else:
        print("Podano niepoprawne wartości!")

print(tabl)