def tabliczka(x1, x2, y1, y2):
    n = abs(x2 - x1)
    m = abs(y2 - y1)
    tab = [[0 for x in range(n+2)] for i in range(m+2)]
    tab[0][0] = ""
    for i in range(1,n+2):
        tab[0][i] = x1 + i - 1 if x2 > 0 else x1 - i + 1
    for i in range(1,m+2):
        tab[i][0] = y1 + i - 1 if y2 > 0 else y1 - i + 1
    
    for i in range(1, m+2):
        for j in range(1, n+2):
            tab[i][j] = tab[i][0] * tab[0][j]

    for b in range(m+2):
        for v in range(n+2):
            print(tab[b][v], end='\t')
        print('\t')


tabliczka(3, 5, 2, 4)
print()
tabliczka(-1, -4, -2, -5)
