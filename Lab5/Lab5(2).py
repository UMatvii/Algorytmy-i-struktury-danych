def p(p_i, p_j):
    e_j = p_j + 1
    e_i = p_i + 1
    ar = [[0 for y in range(e_j)] for x in range(e_i)]
    i_x = 0
    j_y = 0
    a = -1
    b = -1
    for i_x in range(e_i):
        for j_y in range(e_j):
            if i_x == 0 and j_y == 0:
                continue
            elif i_x > 0 and j_y == 0:
                ar[i_x][j_y] = 0
                continue
            elif i_x == 0 and j_y > 0:
                ar[i_x][j_y] = 1
                continue
            elif i_x > 0 and j_y > 0:
                a = ar[i_x - 1][j_y]
                b = ar[i_x][j_y - 1]
            ar[i_x][j_y] = (a + b) / 2
    return ar[i_x][j_y]


i = int(input("Podaj i: "))
j = int(input("Podaj j: "))
if i >= 0 and j >= 0:
    print(p(i, j))
else:
    print("Podane niepoprawne wartoci")