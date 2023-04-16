def nwd(a, b):
    while b != 0:
        c = b
        b = a % b
        a = c
        nwd(a, b)
    return a
print(nwd(12,18))