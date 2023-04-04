def P(i,j):
    if i > 0 and j == 0:
        return 0
    elif i == 0 and j > 0:
        return 1
    elif i > 0 and j > 0:
        Tabl = [0, 0]
        while i and j >= 0:
            Tabl.append((Tabl[i - 1, j] + Tabl[i, j - 1]) / 2)
            i += 1
            j += 1
        return Tabl[]