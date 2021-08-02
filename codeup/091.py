a, b, c = input().split()
d = 1
while d % int(a) != 0 or d % int(b) != 0 or d % int(c) != 0 :
    d += 1
print(d)
