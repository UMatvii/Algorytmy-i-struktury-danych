def suma(table, n):
    if n == 0:
        return 0
    elif n == 1:
        return table[0]
    else:
        mid = n // 2
        r = n - mid
        left_sum = suma(table, mid)
        right_sum = suma(table[mid:n],r)
        return right_sum + left_sum

table = []
a = int(input("Podaj ilość liczb w tablice: "))
for i in range(a):
    calk = int(input("Podaj liczby N: "))
    table.append(calk)

print(suma(table, a))
print("Максим вибач будь ласка")