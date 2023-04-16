def s(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n > 1:
        F = [1, 1]
        i = 2
        while i < n:
            F.append((2 * F[i - 1]) - F[i - 2])
            i += 1
        return F


x = int(input("Podaj n: "))
if x >= 0:
    print(s(x))
else:
    print("Podana niepoprawna wartość!")