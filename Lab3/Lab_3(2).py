a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
while a != b:
    if a > b:
        a = a - b
        continue
    elif b > a:
        b = b - a
        continue
else:
    print(a)