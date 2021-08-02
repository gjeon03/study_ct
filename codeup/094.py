n = int(input())
a = input().split()
min = int(a[0])
for i in range(1, n) :
    if min > int(a[i]) :
        min = int(a[i])
print(min)
