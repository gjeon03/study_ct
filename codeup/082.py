n = int(input())
for i in range(1, n + 1) :
    x = i % 10
    xx = i // 10
    if x == 3 or x == 6 or x == 9 :
        if xx == 3 or xx == 6 or xx == 9 :
            print("XX", end = ' ')
        else :
           print("X", end = ' ')
    else :
        print(i, end = ' ')
