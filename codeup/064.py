a, b, c = input().split()
d = a if int(a) < int(b) else b
print(d if int(d) < int(c) else c)
