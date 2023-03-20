n = int(input("Podaj liczbę n: "))
A = [int(input("Podaj liczbę: ")) for i in range(n)]
i = 0
ile_u = 0
for i in A:
    if i < 0:
        ile_u += 1
        i += 1
    else:
        i += 1
print(f"Ilość liczb ujemnych: {ile_u}")
