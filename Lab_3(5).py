def f(n):
    if (n == 0):
        return 4
    else:
        return 1 / (1 - f(n - 1))
n = int(input("Wpisz n: "))
print(f(n))
