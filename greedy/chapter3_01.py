n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

def first_num(arr):
	first = 0
	for num in arr:
		if first < num:
			first = num
	return first

def second_num(arr, first):
	second = 0
	for num in arr:
		if second < num and num != first:
			second = num
	return second

first = first_num(arr)
second = second_num(arr, first)
count = 0
sum = 0

for i in range(m):
	if count == k:
		count = 0
		sum += second
	else:
		sum += first
	count += 1

print(sum)
