def merge(lista1, lista2):
    n_lista = []
    i = 0
    j = 0
    while i < len(lista1) and j < len(lista2):
        if lista1[i] < lista2[j]:
            n_lista.append(lista1[i])
            i += 1
        else:
            n_lista.append(lista2[j])
            j += 1

    while i < len(lista1):
        n_lista.append(lista1[i])
        i += 1
    while j < len(lista2):
        n_lista.append(lista2[j])
        j += 1

    return n_lista
