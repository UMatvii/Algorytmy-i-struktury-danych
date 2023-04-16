def nwd(a, b):
    while a != b:
        if a > b:
            a = a-b
            nwd(a, b)
        else:
            b = b - a
            nwd(a, b)
    return a
print(nwd(12,18))