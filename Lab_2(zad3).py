for a in range(int(input("Wpisz ilość elementów listy: "))):
    liczby = int(input("Wpisz liczby: "))
numbers1 = []
numbers2 = []
numbers3 = []
lista = []
numbers1.append(liczby)
numbers3.append(numbers1 + numbers2)
while numbers3:
    lista.append(str(numbers3.pop()))
lista.sort(reverse=True)
while lista:
    numbers3.append(int(lista.pop()))
print(numbers3)