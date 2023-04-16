wiersz = int(input("Podaj ilość wierszów: "))
ar1 = []
for i in range(wiersz):
    ar1.append([])
    ar1[i].append(1)
    for j in range(1, i):
      ar1[i].append(ar1[i - 1][j - 1] + ar1[i - 1][j])
    if(wiersz != 0):
      ar1[i].append(1)
for i in range(wiersz):
    print(" " *(wiersz - i), end = " ", sep = " ")
    for j in range(0, i + 1):
      print('{0:6}'.format(ar1[i][j]), end = " ", sep = " ")
    print()