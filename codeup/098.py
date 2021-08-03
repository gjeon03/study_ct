d = []
for i in range(10) :
    d.append([])
    d[i] = input().split()
i = 1
j = 1
d[i][j] = '9'
while d[i][j] != '2' and d[i][j] != '1' :
    if d[i][j + 1] != '1' :
        j += 1
    else :
        i += 1
    if i == 9 or j == 9 or d[i][j] == '2':
        break ;
    d[i][j] = '9'
if (i != 9 or j != 9) and d[i][j] != '1' :
    d[i][j] = '9'
for w in range(10) :
    for h in range(10) :
        print(d[w][h], end = ' ')
    print()
