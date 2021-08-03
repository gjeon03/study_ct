a = []
for i in range(19) :
    a.append([])
    a[i] = input().split()
n = int(input())
for i in range(n) :
    x, y = input().split()
    x = int(x) - 1
    y = int(y) - 1
    for j in range(19) :
        if a[j][y] == '1' :
            a[j][y] = '0'
        else :
            a[j][y] = '1'
    for j in range(19) :
        if a[x][j] == '1' :
            a[x][j] = '0'
        else :
            a[x][j] = '1'
for i in range(19) :
    for j in range(19) :
        print(a[i][j], end = ' ')
    print()
