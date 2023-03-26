a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
if b == 0:
    print("NWD to: ", a)
elif a or b < 0:
    print("Nie jest możliwe do wykonania!")
else:
    while b > 0:
        reszta = a % b
        a = b
        b = reszta
    print("NWD to: ", a)