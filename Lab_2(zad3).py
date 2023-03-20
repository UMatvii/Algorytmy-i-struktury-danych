numbers = [1,11,111,2,23,3,333]
lista = []
while numbers:
    lista.append(str(numbers.pop()))
lista.sort(reverse=True)
while lista:
    numbers.append(int(lista.pop()))
print(numbers)