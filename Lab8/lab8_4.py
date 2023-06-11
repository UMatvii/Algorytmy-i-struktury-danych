def list_sort(list, liczba):
    i = 0
    while i < len(list) and list[i] < liczba:
        i += 1

    list.insert(i, liczba)
    return list