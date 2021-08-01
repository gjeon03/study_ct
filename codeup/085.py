w, h, b = input().split()
sum = ((((int(w) * int(h) * int(b)) / 8) / 1024) / 1024)
print(format(sum, ".2f") + " MB")
