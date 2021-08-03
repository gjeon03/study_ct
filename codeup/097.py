h, w = input().split()
p = []
for i in range(int(h)) :
    p.append([])
    for j in range(int(w)) :
        p[i].append(0)
n = int(input())
for i in range(n) :
    l, d, x, y = input().split()
    x = int(x) - 1
    y = int(y) - 1
    for j in range(int(l)) :
        if d == '0' :
            p[x][y + j] = 1
        else :
            p[x + j][y] = 1
for i in range(int(h)) :
    for j in range(int(w)) :
        print(p[i][j], end = ' ')
    print()
