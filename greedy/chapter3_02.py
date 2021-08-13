n, m = map(int, input().split())

"""" my code 1
arr = []
result = 0

for i in range(n):
	arr.append([])
	arr[i] = input().split()

for i in range(n):
	for j in range(m):
		arr[i][j] = int(arr[i][j])
	min = 10000
	for j in range(m):
		if min > arr[i][j]:
			min = arr[i][j]
	if min > result:
		result = min

print(result)
"""
""" my code 2
arr = [list(map(int, input().split())) for i in range(n)]
result = 0

for n_arr in arr:
	n_arr.sort()
	if result < n_arr[0]:
		result = n_arr[0]

print(result)
"""
#aswer 1
result = 0
for i in range(n):
	data = list(map(int, input().split()))
	min_value = min(data)
	result = max(result, min_value)
print(result)

#aswer 2
result = 0
for i in range(n):
	data = list(map(int, input().split()))
	min_value = 10001
	for a in data:
		min_value = min(min_value, a)
	result = max(result, min_value)

print(result)
