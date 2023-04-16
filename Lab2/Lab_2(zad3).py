n = int(input("Podaj liczbę n: "))
lista = [str(input("Podaj liczbę: ")) for i in range(n)]
numbers = []
while numbers:
    lista.append(str(numbers.pop()))
lista.sort(reverse=True)
while lista:
    numbers.append(int(lista.pop()))
print(numbers)