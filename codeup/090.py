a, m, d, n = input().split()
sum = int(a)
i = 1
while i < int(n) :
    i += 1
    sum = (sum * int(m)) + int(d)
print(sum)
