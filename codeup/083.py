a, b, c = input().split()
count = 0
for i in range(int(a)) :
    for j in range(int(b)) :
        for k in range(int(c)) :
            count += 1
            print(i, j, k, sep = ' ')
print(count)
