n = int(input("Podaj liczbę n: "))
L = [int(input("Podaj liczbę: ")) for i in range(n)]
i = 0
min = L[1]
while i < n:
    if L[i] < min:
        min = i
print(min)