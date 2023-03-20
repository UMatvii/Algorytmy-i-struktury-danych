N = int(input("Podaj liczbę N: "))
x = int(input("Podaj liczbę wyszukiwaną: "))
L = [int(input("Podaj liczbę: ")) for i in range(N)]
l = 0
while l < N:
    if L[l]==x:
        print("Liczba wyszukiwana występuje w liście")
        break
    else:
        l += 1
        continue
else:
    print("Liczba wyszukiwana nie występuje w liście")
