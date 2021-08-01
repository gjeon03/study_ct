h, b, c, s = input().split()
sum = ((((int(h) * int(b) * int(c) * int(s)) / 8) / 1024) / 1024)
print(format(sum, ".1f") + " MB")
